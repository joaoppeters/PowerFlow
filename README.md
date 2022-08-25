# Newton-Raphson Power-Flow 

O principal objetivo deste projeto é fornecer um código Python base para `apoiar estudantes e pesquisadores` em estudos de `análise de regime permanente de sistemas de potência`.

Esse projeto tem como base a leitura de dados de `Sistemas Elétricos de Potência via arquivos ANAREDE` do tipo `.pwf`.

Serão desenvolvidos aqui diferentes ferramentas para análise de SEPs, como por exemplo:
- Solução de Fluxo de Potência Não-Linear via Método de Newton-Raphson
- Solução de Fluxo de Potência Não-Linear via Método de Gauss-Seidel
- Solução de Fluxo de Potência Linearizado
- Solução de Fluxo de Potência Desacoplado
- Solução de Fluxo de Potência Desacoplado Rápido
- entre outros...

> **Para todos os efeitos, considere que este é um projeto em desenvolvimento e que tais ferramentas serão integradas em partes.**



## Requisitos Mínimos
`Bibliotecas de Python` empregadas no projeto e necessárias para o correto funcionamento das ferramentas:
```
numpy
os
pandas
```



## Leitura de Dados
Os `dados do Sistema Elétrico de Potência` em estudo devem estar organizados em um arquivo `.pwf`.

Alguns dados de Sistemas Elétricos de Potência estão disponibilizados na pasta entitulada [sistemas](sistemas).

Um exemplo de inicialização de variável para leitura de dados do arquivo `.pwf` é mostrado abaixo:

```Python
arqv = os.path.join(os.getcwd() + '/sistemas/ieee14.pwf')
```

> **Ao inicializar a variável de arquivo, lembre-se de referenciar ao diretório correto onde está presente. Para isso, use a biblioteca `os`.**



## Matriz Admitância
A matriz admitância (Y<sub>BARRA</sub>) é calculada antes da inicialização do fluxo de potência.

Para mais detalhes sobre o cálculo e montagem dessa matriz, [clique aqui](docs/Admitancia/admitancia.md).



## Formulação da Matriz Jacobiana
A Matriz Jacobiana é modelada de uma única maneira:

- `'Completa':` Configuração tradicional, vetor coluna `∆P-∆Q` associado ao vetor coluna de `variáveis de estado ∆θ-∆V` ([Ver formulação](docs/Jacobiana/completa.md)).
    - Para `equações de controle y` adicionais, associadas a `variáveis de estado x`, essa formulação é reestruturada para associar `∆P-∆Q-∆y` ao vetor de variáveis de estado `∆θ-∆V-∆x`.

> No entanto a Matriz Jacobiana pode ser configurada nas formulações [`Alternada`](docs/Jacobiana/alternada.md) ou mesmo [`Reduzida`](dosc/exemplos/Jacobiana/reduzida.md) (**essas formulações ainda não foram implementadas**).



## Fluxo de Potência
Para realizar a análise de fluxo de potência em regime permanente, `utilize a chamada da classe PowerFlow()` e passe os `parâmetros da classe` que gostaria de analisar.

```Python
from powerflow import PowerFlow

PowerFlow(system=system, method=method, jacobi=jacobi, options=options, control=control, mon=mon, rel=rel,)
```
- `system: str, obrigatório, valor padrão ''`
    - **Variável que indica o nome do arquivo do SEP em estudo.**
    - **Utilize arquivos `.pwf` presentes dentro da pasta [sistemas](sistemas).**

- `method: str, obrigatório, valor padrão 'NEWTON'`
    - **Apenas uma opção poder ser escolhida por vez.**
    - **Opções:**
        - `'NEWTON'` - soluciona o SEP através do método de Newton-Raphson.
        - `'GAUSS'` - soluciona o SEP através do método de Gauss-Seidel.
        - `'LINEAR'` - soluciona o SEP através do método de Newton Raphson Linearizado.
        - `'DECOUP'` - soluciona o SEP através do método Desacoplado.
        - `'fDECOUP'` - soluciona o SEP através do método Desacoplado Rápido.
        - `'CPF'` - soluciona o SEP através do método de Fluxo de Potência Continuado.

- `jacobi: str, opcional, valor padrão 'COMPLETA'`
    - **Apenas uma opção poder ser escolhida por vez.**
    - **Opções:**
        - `'Completa'` - organiza a matriz Jacobiana pela formulação [Completa](docs/Jacobiana/completa.md).
        - `'Alternada'`- organiza a matriz Jacobiana pela formulação [Alternada](docs/Jacobiana/alternada.md).
        - `'Reduzida'` - organiza a matriz Jacobiana pela formulação [Reduzida](docs/Jacobiana/reduzida.md).

- `options: dict, opcional, valor padrão None`
    - **Opções:**
        - `itermx` - número máximo de iterações:
            - **valor padrão 15.**
        - `tolP` - tolerância de convergência para potência ativa:
            - **valor padrão 1E-6.**
        - `tolQ` - tolerância de convergência para potência reativa:
            - **valor padrão 1E-6.**
        - `tolY` - tolerância de convergência para equações de controle adicionais:
            - **valor padrão 1E-6.**
        - `vmax` - valor de magnitude de tensão máximo para todas as barras do SEP:
            - **valor padrão 1.05.**
        - `vmin` - valor de magnitude de tensão mínimo para todas as barras do SEP:
            - **valor padrão 0.95.**
        - `cpfL` - passo para solução do fluxo de potência continuado por meio da variável λ (1a parte da curva PV):
            - **valor padrão 1E-1.**
        - `cpfV` - passo para solução do fluxo de potência continuado por meio da variável V (2a parte da curva PV):
            - **valor padrão 1E-3.**
        - `cpfV2L` - transição da variável V para variável λ (3a parte da curva PV):
            - **valor padrão 85%.**

- `control: str, opcional, valor padrão ''`
    - **Os controles só serão aplicados caso seja selecionado o método de Newton-Raphson.**
    - **Opções:**
        - `'CREM'` - controle remoto de magnitude de tensão de barras remotas.
        - `'CST'` - controle secundário de tensão de magnitude de tensão de barras remotas.
        - `'CTAP'` - controle automático de taps de transformadores em fase.
        - `'CTAPd'` - controle automático de taps de transformadores defasadores.
        - `'FREQ'` - regulação primária de frequência.
        - `'QLIM'` - tratamento de limite de geração de potência reativa.
        - `'SVC'` - controle de magnitude de tensão por meio de compensador estático de potência reativa.
        - `'VCTRL'` - controle de magnitude de tensão de todas as barras.

- `mon: str, opcional, valor padrão ''`
    - **Opções:**
        - `'PFLOW'` - monitoramento do fluxo de potência ativa nas linhas de transmissão.
        - `'PGMON'` - monitoramento do fluxo de potência ativa gerado por geradores.
        - `'QGMON'` - monitoramento do fluxo de potência reativa gerado por geradores.
        - `'VMON'` - monitoramento da magnitude de tensão de barras do SEP.

- `rel: str, opcional, valor padrão ''`
    - **Determina o conjunto de relatórios a serem gerados.**
    - **Apresentação de 1, 2 ou mesmo todas as opções de relatório.**
    - **Os relatórios serão salvos automaticamente em pasta gerada dentro da pasta [sistemas](/sistemas).**
    - **Opções:**
        - `'RBARRA':` Gera o relatório de Dados de Barra em caso Convergente ou Divergente.
            > [Consulte o arquivo exemplo.](docs/Relatorios/rbarra.md)

        - `'RLINHA':` Gera o relatório de Dados de Linha em caso Convergente ou Divergente.
            > [Consulte o arquivo exemplo.](docs/Relatorios/rlinha.md)

        - `'RGERA':` Gera o relatório de Dados de Barras Geradoras em caso Convergente ou Divergente. 
            > [Consulte o arquivo exemplo.](docs/Relatorios/rgera.md)

        - `'RSVC':` Gera o relatório de Dados de Compensadores Estáticos de Potência Reativa (SVC) em caso Convergente ou Divergente.
            > [Consulte o arquivo exemplo.](docs/Relatorios/rsvc.md)

        - `'RCPF':` Gera o relatório do processo iterativo do Fluxo de Potência Continuado em caso Convergente ou Divergente.
            > [Consulte o arquivo exemplo.](docs/Relatorios/rcpf.md)


> PASSE OS PARÂMETROS DA CLASSE `PowerFlow()` DA FORMA COMO MELHOR DESEJAR. 
> O CÓDIGO ABAIXO SE TRATA DE UM EXEMPLO, NÃO CONDIZ COM  

```Python
from powerflow import PowerFlow

PowerFlow(
    system='ieee14.pwf', 
    method='NEWTON', 
    jacobi='COMPLETA, 
    options={
        'itermx': 20,
        'tolP': 1E-4,
        'tolQ': 1E-4,
        'tolY': 1E-4,
        'vmax': 1.045,
        'vmin': 0.965,
        'cpfL': 5E-2,
        'cpfV': 5E-4,
        'cpfV2L': 0.90,
    },
    control='CREM CST CTAP CTAPd FREQ QLIM SVC VCTRL', 
    mon='PFLOW PGMON QGMON VMON', 
    rel='RBARRA RLINHA RGERA RSVC RCPF',
    )
```
# !/usr/bin/env python3
# -*- coding_ctrl: utf-8 -*-

# ------------------------------------- #
# Created by: Joao Pedro Peters Barbosa #
# email: joao.peters@engenharia.ufjf.br #
# ------------------------------------- #

from os.path import dirname, exists
from os import mkdir

class Folder:
    """classe para criação automática de diretórios para armazenar resultados"""

    def __init__(
        self,
        setup,
    ):
        """inicialização

        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        # Diretório de Sistemas
        dirSistemas = dirname(setup.dirSEP)

        # Criação de diretório Resultados
        dirResultados = dirname(dirSistemas) + '/resultados/'
        if exists(dirResultados) is False:
            mkdir(dirResultados)
        
        setup.dirResultados = dirResultados


    
    def admittance(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados de matriz admitância
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dirRadmittance = setup.dirResultados + 'MatrizAdmitancia/'
        if exists(dirRadmittance) is False:
            mkdir(dirRadmittance)
        
        setup.dirRadmittance = dirRadmittance



    def convergence(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados da trajetória de convergência
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dirRconvergence = setup.dirResultados + 'TrajetoriaConvergencia/'
        if exists(dirRconvergence) is False:
            mkdir(dirRconvergence)

        setup.dirRconvergence = dirRconvergence



    def continuation(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados de fluxo de potência continuado
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        self.dirRcpf = setup.dirResultados + 'Continuado/'
        if exists(self.dirRcpf) is False:
            mkdir(self.dirRcpf)
        
        setup.dirRcpf = self.dirRcpf

        self.continuationsystem(setup,)



    def continuationsystem(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados de fluxo de potência continuado (arquivos e imagens)
        específico para cada sistema analisado
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dircpfsys = self.dirRcpf + setup.name + '/'
        if exists(dircpfsys) is False:
            mkdir(dircpfsys)

        dircpfsysimag = dircpfsys + 'imagens/'
        if exists(dircpfsysimag) is False:
            mkdir(dircpfsysimag)

        dircpfsystxt = dircpfsys + 'txt/'
        if exists(dircpfsystxt) is False:
            mkdir(dircpfsystxt)

        setup.dircpfsys = dircpfsys
        setup.dircpfsysimag = dircpfsysimag
        setup.dircpfsystxt = dircpfsystxt



    def jacobi(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados de matriz jacobiana
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dirRjacobi = setup.dirResultados + 'MatrizJacobiana/'
        if exists(dirRjacobi) is False:
            mkdir(dirRjacobi)
        
        setup.dirRjacobi = dirRjacobi



    def reports(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados de relatórios
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dirRreports = setup.dirResultados + 'Relatorios/'
        if exists(dirRreports) is False:
            mkdir(dirRreports)
        
        setup.dirRreports = dirRreports


    
    def statevar(
        self,
        setup,
    ):
        """criação de diretório para armazenar resultados finais de convergência das variáveis de estado
        
        Parâmetros
            setup: self do arquivo setup.py
        """

        ## Inicialização
        dirRstatevar = setup.dirResultados + 'VariaveisEstado/'
        if exists(dirRstatevar) is False:
            mkdir(dirRstatevar)
        
        setup.dirRstatevar = dirRstatevar
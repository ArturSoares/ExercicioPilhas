import operator

class AvaliadorAritimetico:
    __expressao = ""

    __pilhaValores = []

    __pilhaOperadores = []

    def avaliarExpressao(self, expressao):
        __expressao = expressao

        numeroAtual = ""

        for i in range(len(__expressao), 0, -1):
            
            if(self.__eNumeral(__expressao[i - 1])):
                
                numeroAtual = numeroAtual + __expressao[i - 1]
            
            else:

                if(numeroAtual != ""):
                    numeroAtual = numeroAtual[::-1]
                    self.__pilhaValores.append(numeroAtual)
                    numeroAtual = ""

                if(self.__eOperador(__expressao[i - 1])):

                    self.__pilhaOperadores.append(__expressao[i - 1])

                if(self.__eFechamentoDeOperacao(__expressao[i - 1])):

                    self.__calcularExpressao()

    def __eNumeral(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __eOperador(self, s):
        if(s == "+" or s == "-" or s == "*" or s == "/"):
            return True
        else:
            return False

    def __eFechamentoDeOperacao(self, s):
        
        s = s.strip()

        if(s == "("):
            return True

        return False

    def imprimirValores(self):
        for x in self.__pilhaValores:
            print(x)

    def __executarOperacao(self, numero1, operador, numero2):

        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

        return ops[operador](numero1, numero2)

    def __calcularExpressao(self):

        copiaOperadores = self.__pilhaOperadores[:]

        try:
            copiaOperadores.pop()
        except  :
            return

        numero1 = self.__pilhaValores.pop()
        operador = self.__pilhaOperadores.pop()
        numero2 = self.__pilhaValores.pop()


        if(operador == "-"):
            numero2 = float(numero2) * -1
            operador = "+"

        if(operador == "/"):
            x = numero2
            numero2 = numero1
            numero1 = x
        
        self.__pilhaValores.append(self.__executarOperacao(float(numero2),operador,float(numero1)))

        copiaOperadores = self.__pilhaOperadores[:]

        try:
            copiaOperadores.pop()
            self.__calcularExpressao()
        except  :
            pass


x = AvaliadorAritimetico()

x.avaliarExpressao("((10/5)*(4-2))")
x.imprimirValores()

#x.avaliarExpressao("(1+((2+3)*(4*5)))")
#x.imprimirValores()

#x.avaliarExpressao("( (1 - 2 + 1) * (2 - 1 - 1) * (2 - 4 + 2) )")
#x.imprimirValores()
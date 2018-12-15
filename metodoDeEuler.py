# -*- coding: utf-8 -*-

"""
    Programa para implementar o metodo de Euler para o trabalho 3 de Calculo Numerico 2018.2
"""

import matplotlib.pyplot as plt

# y1 = y0 + h*ylinha(y)
k = 0.8109302162

def eulerModificado(y0, h):
    y1 = y0 + h*ylinha(y0)
    return y0 + (h/2)*(ylinha(y0) + ylinha(y1))


def ylinha(y):
    """ 
        y' = -k(T - Tm)
    """

    return -k*(y - 10)

def T(t):
    """
        Calcula o valor da funcao exata
        T(t) = 60 * e^(-k*t) + 10
    """
    e = 2.71828182845       #9045235360287471352662497757
    return 60 * e**(-k*t) + 10


def questao1():
    # primeiro valor de y
    y = 70

    # calculando nossa funcao exata no ponto 0
    t = T(0)

    # printa os valores de Euler modificado e da funcao exata em x = 0
    print("[Euler modificado = {}]".format(y))
    print("[T(0)]            = {}]".format(0, t))

    # printa o erro nesso ponto 0 (que será 0) para a questao 2 do trabalho
    print("erro:", abs(y-t))
    print("===========")

    # iterando a quantidade de vezes necessaria de acordo com o enunciado
    # no nosso caso são 6 iteracoes pedidas:
    # 0.5, 1.0, 1.5, 2.0, 2.5, 3.0
    # tive que usar inteiros por causa de erro de arredondamento do Python
    # que poderia dar problemas mais a frente
    for _ in range(5, 35, 5):       # para tempo igual 0 ate tempo 3 pulando 0,5 usando inteiro por limitacao do python
        # calculando o valor de Euler modificado seguinte
        y = eulerModificado(y, 0.5)

        # printando esse valor calculado acima
        print("[Euler modificado = {}]".format(y))

        # calculando o valor exato da funcao
        t = T(_/10)

        # printando esses valores para sabermos o que esta acontecendo
        print("[T({})]          = {}]".format(_/10, t))

        # printando o erro em modulo para a questao 2 do trabalho
        print("erro:", abs(y-t))
        print("===========")

def questao4(h):
    # primeiro valor de y
    y = 70

    # calculando o valor da funcao exata em x = 0
    t = T(0)

    # X sera uma lista de pontos no eixo x para plotarmos mais a frente
    X = [0]

    # Y_y sera uma lista com os valores que o Euler modificado nos retorna
    Y_y = [y]

    # Y_t sera uma lista com os valores da funcao exata para plotarmos mais a frente tambem
    Y_t = [t]

    # printando os valores iniciais e o erro
    print("[Euler modificado = {}]".format(y))
    print("[T(0)]            = {}]".format(0, t))
    print("erro:", abs(y-t))
    print("===========")

    # Como o Python tem uma limitacao de nao poder usar numeros decimais na funcao range
    # preciso fazer um workaround para conseguir executar a quantidade de vezes necessaria
    # sem muito trabalho
    # Tambem fiz isso na funcao da questao1(), mas tinha menos relevancia no codigo
    _h = int(h*10)
    for _ in range(_h, 30 + _h, _h):       # para tempo igual 0 ate tempo 3 pulando h por meio de um workaround que usa inteiro por limitacao do python
        # adicionando o h atual na lista do eixo x
        # faco _/10 pois tivemos que multiplicar por 10 acima a fim de fazer a funcao range() funcionar corretamente
        X.append(_/10)

        # calculando o valor de Euler modificado seguinte
        y = eulerModificado(y, h)

        # e adicionando esse valor aquela nossa lista
        Y_y.append(y)

        # calculando o valor exato da funcao no ponto atual e adicionando a sua lista respectiva
        t = T(_/10)
        Y_t.append(t)
        
        # printando os valores relevantes na tela
        print("[Euler modificado = {}]".format(y))
        print("[T({})]          = {}]".format(_/10, t))

        # printando o erro
        print("erro:", abs(y-t))
        print("===========")

    # agora que ja calculamos os valores, iremos plotar no grafico para resolver a questao 4
    plt.plot(X, Y_t, color='blue')
    plt.scatter(X, Y_y, color='red')
    plt.show()

if __name__ == '__main__':
    questao1()
    questao4(0.2)       # h = 0.2
    questao4(0.1)       # h = 0.1

    print("Como podemos ver, os valores do grafico são extremamente proximos e nos dão uma otima aproximação")
    print("Quanto mais diminuimos o h, melhor será a aproximação")
    print("No entanto, já temos uma aproximação com erro de 10^-1 que pode ser suficiente dependendo da sua aplicação.")

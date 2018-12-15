# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

""" 
    Programa para implementar o metodo de Runge-Kutta de quarta ordem
    para o trabalho 3 de Calculo Numerico 2018.2
"""

k = 0.8109302162

def T(t):
    """
        T(t) = 60 * e^(-k*t) + 10
    """
    e = 2.71828182845       #9045235360287471352662497757
    return 60 * e**(-k*t) + 10

def ylinha(y):
    """ 
        y' = -k(T - Tm)
    """

    return -k*(y - 10)

def RK4(y, h):
    # calculando os valores de k necessários para a fórmula
    k1 = ylinha(y)
    k2 = ylinha(y + h/2 * k1)
    k3 = ylinha(y + h/2 * k2)
    k4 = ylinha(y + h   * k3)
    
    # printando esses valores para melhor compreensão
    print("k1:", k1)
    print("k2:", k2)
    print("k3:", k3)
    print("k4:", k4)

    # retornado o valor da fórmula
    return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def questao3():

    # valor inicial de y
    y = 70

    # valor da exato da função no ponto inicial (que será 70 tambem como já sabemos)
    t = T(0)

    # variavel para sabermos qual o maior erro encontrado
    erro = 0

    # printando os valores achados e o valor do erro (que claramente será 0)
    print("[Runge Kutta = {}]".format(y))
    print("[T(0)        = {}]".format(t))
    print("erro:", abs(y-t))
    print("==========")

    # iterando a quantidade necessária de vezes, assim como fizemos no programa do metodo de Euler.
    for _ in range(5, 35, 5):
        # calculando o proximo valor do RK4, passando como parametro o valor antigo do y e o valor de h
        y = RK4(y, 0.5)

        # calculando o valor exato da função nesse mesmo ponto
        t = T(_/10)

        # printando os valores achados e o erro
        print("[Runge Kutta = {}]".format(y))
        print("[T({})      = {}]".format(_/10, t))
        print("erro:", abs(y-t))
        if abs(y-t) > erro:
            erro = abs(y-t)
        print("==========")

    print("Maior erro:", erro)

def questao4(h):

    # valor inicial de y
    y = 70

    # valor da exato da função no ponto inicial (que será 70 tambem como já sabemos)
    t = T(0)

    # X sera uma lista de pontos no eixo x para plotarmos mais a frente
    X = [0]

    # Y_y sera uma lista com os valores que o RK4 nos retorna
    Y_y = [y]

    # Y_t sera uma lista com os valores da funcao exata para plotarmos mais a frente tambem
    Y_t = [t]

    # variavel que irá salvar o maior valor do erro
    erro = 0

    # printando os valores achados e o valor do erro (que claramente será 0)
    print("[Runge Kutta = {}]".format(y))
    print("[T(0)        = {}]".format(t))
    print("erro:", abs(y-t))
    print("==========")

    # fazendo a mesma coisa que foi explicada no codigo do Método de Euler
    _h = int(h*10)

    # iterando a quantidade necessária de vezes, assim como fizemos no programa do metodo de Euler.
    for _ in range(_h, 30 + _h, _h):
        # adicionando o valor de h atual à lista que iremos usar para o eixo x
        X.append(_/10)

        # calculando o proximo valor do RK4, passando como parametro o valor antigo do y e o valor de h
        y = RK4(y, h)

        # adicionando o valor de y encontrado à lista para plotarmos mais a frente
        Y_y.append(y)

        # calculando o valor exato da função nesse mesmo ponto
        t = T(_/10)

        # adicionando o valor exato da função à sua lista respectiva
        Y_t.append(t)

        # printando os valores achados e o erro
        print("[Runge Kutta = {}]".format(y))
        print("[T({})      = {}]".format(_/10, t))
        print("erro:", abs(y-t))
        if abs(y-t) > erro:
            erro = abs(y-t)
        print("==========")

    # printando o maior valor de erro encontrado
    print("Maior erro:", erro)

    # após termos realizados as iterações necessárias, plotamos o gráfico
    # plotando os valores exatos da função para criarmos uma reta da cor azul
    plt.plot(X, Y_t, color='blue')

    # plotando os valores encontrados pelo RK4 como pontos, usando a cor vermelha
    plt.scatter(X, Y_y, color='red')

    # agora chamamos o matplotlib para mostrar o gráfico
    plt.show()

if __name__ == '__main__':
    questao3()
    questao4(0.2)           # executando o RK4 para h = 0.2
    questao4(0.1)           # executando o RK4 para h = 0.1

    print("Como podemos ver pelo resultado, os números são extremamente próximos.")
    print("Consideravelmente mais próximos do que foi encontrado pelo Método de Euler modificado.")
    print("Pela saída do programa conseguimos ver que o maior erro encontrado foi da ordem de 10^-6 para h = 0.1.")
    print("Enquanto isso, no Método de Euler modificado, tivemos um erro, para h = 0.1 de 10^-1.")
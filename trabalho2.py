import sys
# De acordo com os dados do enunciado, temos
# maximo de iteracoes = 100
# erro de 10^-6

max_iter = 100
erro     = 0.000001

# Dados da formula
Ka       = 0.88
cs       = 9
c0       = 2
e        = 2.71828          #1828459045235360287471352662497757
nivel_OD = 8

# Metodo de Newton
# x1 = x0 - funcao(x0)/derivada(x0)

# da pra fazer recursivamente facilmente, mas acho que sera mais lento
def newton(funcao, derivada, x0):
    print "i        t               c(t)            c'(t)"
    print "0        {}              {}              {}".format(x0, funcao(x0), derivada(x0))
    for i in range(1,max_iter+1):
        x1 = x0 - funcao(x0)/derivada(x0)
        print "{}\t{}\t{}\t{}".format(i, x1, funcao(x1), derivada(x1))

        if abs(funcao(x1)) <= erro:
            return x1   # encontramos o x1 que nos retorna um valor da funcao tao proximo quanto queremos (da ordem de 10^-6)
        # caso o if acima tenha sido falso, precisamos continuar com o metodo e ir para o proximo valor de x1
        x0 = x1

    print "[ultrapassei o numero maximo de iteracoes, nao foi possivel encontrar um valor utilizando o metodo de Newton]"

def c(t):
    return cs - (cs-c0)*(e**(-Ka*t)) - nivel_OD

def derivada(t):
    return Ka*(cs-c0)*(e**(-Ka*t))

def main():
    # Fazendo para t = 1, que eh o primeiro caso pedido no trabalho
    t = int(sys.argv[1])
    print "Resultado: {}".format(newton(c, derivada, t))

if __name__ == '__main__':
    main()

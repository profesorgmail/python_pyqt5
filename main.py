""" 
fichero principal

author: Santiago Díaz
user_github: @profesorgmail
"""
from modulo import operations as op
import doctest

def main():
    valor = op.sumatoria(1,2,3,4,5)
    print("valor de la sumatoria ", valor)

if __name__ == '__main__':
    print("Principal")
    doctest.testmod()
    main()
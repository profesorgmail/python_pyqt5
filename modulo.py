"""
Clase que realiza operaciones básicas

:operaciones
    - suma
    - resta
    - multiplica
    - division
"""
import doctest

class operations():
    """Realizará operaciones básicas de matemáticas"""
    def sumatoria(*args):
        """Suma todo los argumentos que se pase, 
        :input 
            valor entero o real
        :retorno 
            un valor númerico entero o real

        >>> sumatoria(2,4)
        6
        """
        return sum(args)


if __name__ == "__main__":
    doctest.testmod()
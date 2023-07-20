#<literales> = 1, 'abc', 2.0, True
#<operadores> = +, -,*,**,%, ==, =
#<literal> <operador> <literal>

'''
>>> 1 + 2
>>> 1 3.0 #error sintactico
>>> 5 / 'abc' #error semantico estatico
>>> 5 * 'abc' #abc abc abc abc abc 

#statement o enunciado
>>> print(1 + 2)
>>> print('Hello, world!')

#¿Que es un objeto?
    Concepto, abstracción o cosa con límites bien definidos y con significado para el problema que se está manejando

    Escalares vs No escalares
    -Tipos
    int.
    float.
    bool.
    str.
#Definiendo variables
    my_int  = 1
    my_float = 1.0
    my_bool = True
    my_none = None
    my_str = 'Hola'

#Imprimiendo el tipo
    type(my_int)
    >>> <class 'int'>
    type(my_float)
    >>> <class 'float'>
    type(my_bool)
    >>> <class 'bool'>
    type(my_none)
    >>> <class 'NoneType'>
    type(my_str)
    >>> <class 'str'>
#¿Que pasa si ejecutas esto?
1 + 1 
2 - 5
2.0 * 3
6 // 2
6 // 4
6 / 4
7 % 2
2 ** 2

Resultado
>>> 1 + 1
2
>>> 2 - 5
-3
>>> 2.0 * 3
6.0
>>> 6 // 2
3
>>> 6 // 4
1
>>> 6 / 4
1.5
>>> 7 % 2
1
>>> 2 ** 2
4

#¿Qué sucede cuando sumamos True + True o True + False?
True + True
True + False

#Resultado
>>> True + True
2
>>> True + False
1

#Esto sucede porque internamente los booleanos True y False tienen asignados valores de 1 y 0 respectivamente.

'''
import functools
nums = [1, 2, 3, 4, 5]
nums2 = [2, 4, 6, 8, 10]
str_nums = ['1', '2', '3', '4', '5']
str_nums2 = ['1.0', '2.5', '3.2', '4.7', '5.9']

#Elevar al cuadrado cada elemento en una lista utilizando map.
squared_nums = list(map(lambda x: x**2, nums))
print(squared_nums)

#Multiplicar los elementos correspondientes de dos listas y sumar los resultados utilizando map.
nums3 = list(map(lambda x, y: x*y , nums, nums2))
print(nums3)


#Convertir una lista de cadenas a una lista de enteros utilizando map.
int_nums = list(map(lambda x: int(x), str_nums))
print(int_nums)

#Convertir una lista de cadenas a una lista de flotantes utilizando map.
new_float = list(map( lambda x: float(x), str_nums2))
print(str_nums2)
print(new_float)

#Aplicar una función personalizada a cada elemento de una lista utilizando map.
def add_five(x):
    return x+5

new_number = list(map(add_five, nums))
print(new_number)

#Multiplicar cada elemento en una lista por una constante utilizando map.
cons = 6
multi_constante = list(map(lambda x: x*cons, nums ))
print(multi_constante)

#Calcular el producto de todos los elementos en una lista utilizando map y reduce.
producto = functools.reduce(lambda counter, x: counter*x,nums)
print(producto)

#Crear una nueva lista que contenga sólo los elementos únicos de otra lista utilizando map.
numeros = [ 1, 2, 3, 1, 2, 3, 4, 5, 1, 3, 5, 6, 9, 16 ]
numeros_unicos = list(set(map(lambda x: x, numeros)))
print(numeros_unicos)

#Crear una nueva lista que contenga el cuadrado de cada número impar en una lista utilizando map y filter.
numeros = [ 1, 2, 3, 1, 2, 3, 4, 5, 1, 3, 5, 6, 9, 16 ]
impares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros)))
print(impares)

#Convertir una lista de tuplas en una lista de diccionarios utilizando map.
people = [('Andres',25),('Alvaro',50), ('Johana', 42,),('Sebastian', 23), ('Luisa', 20)]
diccionario = list(map( lambda x: {'name':x[0], 'edad':x[1]}, people))
print(diccionario)

#Devuelve un tipo de dato serie, si el indice no esta especificado lo toma desde el 0 hasta el numero de elementos de la lista
import pandas as pd
s=pd.Series(['Matematicas', 'Historia', 'Economia', 'Programacion', 'Ingles'])
print(s)
print(s.dtype)
print("---------")

#Devuelve una serie de tipo diccionario con los valores de cada elemento del objeto
import pandas as pd
s=pd.Series({'Matemáticas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print(s)

print("---------")
import pandas as pd
s=pd.Series([1,2,2,3,3,3,4,4,4,4])
print("numero de valores de la lista")
print(s.size)
print("propidedades del indice de la lista")
print(s.index)
print("Tipo de los datos de la lista")
print(s.dtype)

print("---------")
import pandas as pd
s=pd.Series({'Matemáticas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print("acceder por index")
print(s[1:2])
print("acceder por nombre")
print(s[['Programacion']])
#importante los dos "[", sino no funciona xDdDDdD

print("---------")
import pandas as pd
s=pd.Series(["hola ", "xd"])
print(s.sum())

import pandas as pd
s=pd.Series([1,1,1,1,2,2,2,3,3,4])
print("s.count() Devuelve la suma de todos los valores válidos (no nulos ni not a number)")
print(s.count())

print("cumsum acumula la suma de los elementos a su vez que muestra el index de cada uno hasta llegar a la posicion del elemento final")
print(s.cumsum())

print("s.value_counts() Devuelve la frecuencia de repeticiones de los valores de la serie")
print(s.value_counts()) #para frecuencias absolutas
print(s.value_counts(normalize=True)) #para frecuencias relativas

print("s.min sirve para mostrar el numero minimo de la serie, asi como s.max para mostrar el numero maximo")
print(s.min(), s.max())

print("s.mean sirve lara devolver la media de los datos solo cuando la lista es de tipo numerico")
print(s.mean())

print("s.var() sirve para devolver la varianza de los datos, solo cuando la lista es de tipo numerico")
print(s.var())

print("s.std() sirve para devolver la desviacion tipica, tambien solo cuando los elementos de la lista son numericos")
print(s.std())

print("s.describe() es un resumen de las funciones anteriores, devuelve numero de datos, suma, minimo y maximo, ademas de la media, desviacion tipica y los cuartiles")
print(s.describe())

print("---------")
import pandas as pd
s=pd.Series([1,2,3,4])
#se pueden aplicar las operaciones *,+,/ etc.
print("para multiplicar cada elemento en el index de la lista por 2")
print(s*2)

print("Para sacar el residuo de la division entre X numero")
print(s%2)

print("tambien se pueden multiplicar letras xd")
s=pd.Series(['sexoo ', 'sexoo '])
print(s*3)

print("---------")
print("Para agregar funciones a una serie: s.apply()")
import pandas as pd
s=pd.Series(['hola'])
print(s.apply(str.upper))


print("----------")
print("filtrar una serie")
import pandas as pd
s=pd.Series({'objeto1':6, 'objeto2':2, 'objeto3':7})
print(s[s>=6])


print("----------")
print("Ordenar una serie")
import pandas as pd
s=pd.Series([1,2,3,4,5])
print(s.sort_values())
print(s.sort_index(ascending=False))
print(s.sort_index(ascending=True))

print("----------")
print("Dataframe")
import pandas as pd 
datos={
'nombre': ['Maria','Luis','Carmen','Antonio'],
'edad':[18,22,20,21],
'correo':['maria@gmail.com','luis@yahoo.com', 'carmen@gmail.com', 'antionio@gmail.com']
}

dataFrame=pd.DataFrame(datos)
print(dataFrame)


print("----------")
print("Dataframe con listas (arrays xd)")
import pandas as pd 
dataFrame=pd.DataFrame([['Maria', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(dataFrame)

print("----------")
import pandas as pd
dataFrame=pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(dataFrame.head())

print("----------")
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
# imprime el valor de la columna que se especifique


# el valor medio de la columna 'colesterol'
# colesterol=df['colesterol']
# print(colesterol.mean())




print("----------")
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
# imprime el valor de la columna que se especifique
print(df.loc[7, 'colesterol'])
print(df.colesterol.mean())
df.loc[7,'colesterol']=df.colesterol.mean()

print("----------")


df.loc[2, "peso"]=df.peso.mean()
# fichero con las filas desconocidas llenadas como valor medio de su respectiva columna
print(df)

# agregar otra columna al dataframe
# df['diabetes']=pd.Series([True, False, True, True, False, True, True, False, True, True, False, True, False, False])
# print (df)


# df.to_csv(df.csv, sep=';', columns=True, index=True)

print('filtro en las filas de un dataframe')
print(df[(df['sexo']=='H')])

print('agrupacion de un dataframe')
print(df.groupby('sexo').get_group('M'))
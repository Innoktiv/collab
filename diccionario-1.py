post = {"user_id":209, "message":"D5 G3 H8", "language": "english", "datetime": 13424534534, "location": (44.345345, -545.453453)}

# En DICCIONARIOS
# Imputs are called KEYS
# Outputs are called VALUES

# Que tipo de objeto es el especificado como argumento de type() function?
x = type(post)
print(x)
# El diccionario post es una instancia de la clase dict

print("___________________________________")
# POr tanto podemos usar -- .dict() constructor -- para crear otro diccionario
post2 = dict(secuencia1= 12123, secuencia2= 1234123123 )
print(post2)

print("___________________________________")
# Agregar nueva informacion al diccionario
post2["secuencia3"] = 928340982340
post2["secuencia4"] = 7573454763
print(post2)

print("___________________________________")
# Entrar a recoger informacion
print(post["message"])
print(post2["secuencia4"])

# Si intentamos recoger informacion inexistente tendremos un "KeyError"
#print(post2["location"])

# Para evitar el error y obtener un alerta
if 'location' in post2:
    print[post2('location')]
else:
    print("El diccionario no contiene el Key = location")

# Otra posibiidad de manejar el error is con un Try 
try:
    print(post2["location"])
except KeyError:
    print("Post2 no tiene un key = location")

print("___________________________________")
# Otra forma de acceder informacion en un diccionario
# Primero obtenemos todos los atributos del objeto post2
print(dir(post2))
#print(help(post2.get))
print("___________________________________")
loc = post2.get('location', None)
print(loc)

# Obtener todos los keys
print("___________________________________")
print(post2)
for key in post2.keys():
    value = post2[key]
    print(key, '=', value)
def slice_simple():
    texto = "Awesome"
    primeras = texto[0:3].lower()
    medio = texto[2:5].lower()
    combinado = texto[0:4].lower() + texto[-3:].lower()
    print(primeras)
    print(medio)
    print(combinado)
slice_simple()



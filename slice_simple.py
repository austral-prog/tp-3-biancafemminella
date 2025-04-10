def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
	primeras = texto[0:3].lower()
	medio = texto[2:5].lower()
	combinado = texto[0:4].lower() + texto[-3:].lower()
	print(primeras)
	print(medio)
	print(combinado)
slice_simple()


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

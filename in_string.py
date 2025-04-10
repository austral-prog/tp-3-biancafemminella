def check_vowels():
    # Código a implementar utilizando input.
	nombre = str(input("Ingrese un nombre:").lower())
	print (f"Contiene a: {"a" in nombre}")
	print (f"Contiene e: {"e" in nombre}")
	print (f"Contiene e: {"i" in nombre}")
	print (f"Contiene e: {"o" in nombre}")
	print (f"Contiene e: {"u" in nombre}")
check_vowels()


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

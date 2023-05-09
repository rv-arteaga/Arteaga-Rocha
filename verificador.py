import sys
import os

path = sys.argv[1]
pathCompressed = "descomprimido-elmejorprofesor.txt"


def getSize(filename):
	st = os.stat(filename)
	return st.st_size


def comparar_arreglos(arr1, arr2):
	"""
    Compara dos arreglos y devuelve las diferencias encontradas.
    """
	# Verificar que ambos arreglos tengan la misma longitud
	if len(arr1) != len(arr2):
		raise ValueError("Los arreglos no tienen la misma longitud")

	# Inicializar una lista para almacenar las diferencias
	diferencias = []

	# Recorrer los arreglos y comparar cada elemento
	for i in range(len(arr1)):
		if arr1[i] != arr2[i]:
			diferencias.append((i, arr1[i], arr2[i]))

	# Devolver la lista de diferencias encontradas
	return diferencias


# Function that reads two files, checks if files are equal by comparing lists
def verifyFile(path, decompressed):
	fileSize = getSize(path)
	fileSizeDecompressed = getSize(decompressed)
	file = open(path, 'r', encoding='latin-1')
	fileDecompressed = open(decompressed, 'r', encoding='latin-1')
	lines = file.readlines()
	linesDecompressed = fileDecompressed.readlines()
	file.close()

	fileDecompressed.close()
	#print(comparar_arreglos(lines,linesDecompressed))
	if lines == linesDecompressed:
		print('ok')
	else:
		print('nok')


"""    if fileSize == fileSizeDecompressed:
        print('ok tam')
    else:
        print('nok tam')"""

verifyFile(path, pathCompressed)

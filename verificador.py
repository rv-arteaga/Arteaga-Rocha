import sys
import os


def getSize(filename):
	st = os.stat(filename)
	return st.st_size


def get_file_encoding(path):
	# Patrones de bytes característicos de algunas codificaciones
	encodings = [
	 ("utf-8", b"\xef\xbb\xbf"),
	 ("utf-16", b"\xff\xfe"),
	 ("utf-16be", b"\xfe\xff"),
	 ("utf-32", b"\xff\xfe\x00\x00"),
	 ("utf-32be", b"\x00\x00\xfe\xff"),
	 ("iso-8859-1", b"\x80"),
	 ("windows-1252", b"\x80"),
	]

	# Leer los primeros bytes del archivo
	with open(path, "rb") as f:
		first_bytes = f.read(4)

	# Buscar coincidencias con los patrones de bytes
	for encoding, pattern in encodings:
		if first_bytes.startswith(pattern):
			return encoding

	# Intentar leer el archivo con varias codificaciones
	for encoding in [
	  "utf-8", "utf-16", "utf-16be", "utf-32", "utf-32be", "iso-8859-1",
	  "windows-1252"
	]:
		try:
			with open(path, "r", encoding=encoding) as f:
				f.read()
			return encoding
		except UnicodeDecodeError:
			pass

	return None


# Function that reads two files, checks if files are equal by comparing lists
def verifyFile(path1, path2):
	fileSize1 = getSize(path1)
	fileSize2 = getSize(path2)
	file1 = open(path1, 'r', encoding=get_file_encoding(path1))
	file2 = open(path2, 'r', encoding=get_file_encoding(path2))
	lines1 = file1.readlines()
	lines2 = file2.readlines()
	file1.close()
	file2.close()

	if lines1 == lines2:
		print('ok')
	else:
		print('nok')

	if fileSize1 == fileSize2:
		print('ok tam')
	else:
		print('nok tam')
		print(fileSize2 - fileSize1)


path1 = sys.argv[1]
path2 = sys.argv[2]
# pathCompressed = "descomprimido-elmejorprofesor.txt"
verifyFile(path1, path2)

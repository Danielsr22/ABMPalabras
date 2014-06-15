import pickle
import os


def menu_principal():
	print('--------------------- MENÚ PRINCIPAL ---------------------')
	print('\t 1. Crear categoría.')
	print('\t 2. Eliminar categoría.')
	print('\t 3. Modificar categoría.')
	print('\t 4. Categorias disponibles.')
	print('\t 5. Salir.')
	opc = input('\n>> Opción deseada: ')
	while (opc < 1) or (opc > 6):
		print('>> ERROR. Valor fuera de rango.')
		opc = input('\n>> Opción deseada:')
	if (opc in range(1,6)):
		if (opc == 1):
			crear_categoria(leer_categoria())
		elif (opc == 2):
			eliminar_categoria(leer_categoria())
		elif (opc == 3):
			menu_categoria()
		elif (opc == 4):
			ver_categorias()
		else:
			return



def leer_categoria():
	cat = input('>> Nombre de la categoría a trabajar (nueva o existente): ')
	cat = cat.upper()
	return cat



def alta_categoria(cat):
	try:
		f = open('categorias.bin','rb')
		dic = pickle.load(f)
		dic[cat] = []
		try:
			f = open('categorias.bin','wb')
			pickle.dump(dic,f)
			print('>> La categoría {0} se creó correctamente!'.format(cat))
		except:
			print('>> ERROR al escribir en el archivo.')
	except:
		print('>> ERROR al intentar abrir el archivo como lectura.')
	input('\n-- Presione <ENTER> para continuar --')
	menu_principal()


def crear_archivo():
	try:
		f = open('categorias.bin','wb')
		f.close()
		print('>> El archivo "categorias.bin" se creó correctamente.')
		input('\n-- Presione <ENTER> para continuar --')
	except:
		print('>> ERROR. No se pudo crear el archivo.')


def crear_categoria(cat):
	if (os.path.exists('categorias.bin')):
		try:
			f = open('categorias.bin','rb')
			dic = pickle.load(f)
			if (cat in dic):
				print('>> La categoría ya existe en el archivo!')
			else:
				resp = input('>> La categoría {0} no existe en el archivo. ¿Desea crearla? [s/n]'.format(cat))
				resp = resp.lower
				if (resp == 's'):
					alta_categoría(cat)
				elif (resp == 'n'):
					print('>> No se creó la nueva categoría. Presione <ENTER> para volver al menú principal.')
					input()
				else:
					pass
			f.close()
		except:
			print('>> ERROR al abrir el archivo "categorias.bin".')
			return
	else:
		print('>> ERROR, el archivo "categorias.bin" no existe. ¿Desea crearlo? [s/n]')
		if (evaluar_resp() == 's'):		 ## IMPLEMENTAR
			crear_archivo()		## IMPLEMENTAR
			menu_principal()
		else:
			print('\n>> No se puede continuar sin el archivo. Abortando programa...')
			return

menu_principal()
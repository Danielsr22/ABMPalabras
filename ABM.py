import pickle
import os


def leer_categoria():
	cat = input('>> Nombre de la categoría con la que desea trabajar: ')
	cat = cat.upper()
	return cat



def alta_categoria(cat):
	try:
		f = open('categorias.bin','rb')
		dic = pickle.load(f)
		dic[cat] = []
		if not(os.path.exists('categorias.bin')):
			try:
				f = open('categorias.bin','wb')
				pickle.dump(dic,f)
				print('>> La categoría {0} se creó correctamente!'.format(cat))
			except:
				print('>> ERROR al escribir en el archivo.')
		else:
			print('>> El archivo "categorias.bin" ya existe en el directorio.')
	except:
		print('>> ERROR al intentar abrir el archivo como lectura.')
	input('\n-- Presione <ENTER> para continuar --')
	menu_principal()


def crear_archivo():
	try:
		f = open('categorias.bin','wb')
		dic = {}
		pickle.dump(dic,f)
		f.close()
		print('>> El archivo "categorias.bin" se creó correctamente.')
		input('\n-- Presione <ENTER> para continuar --')
	except:
		print('>> ERROR. No se pudo crear el archivo.')


def evaluar_resp(resp):
	resp = resp.lower()
	if (resp == 's'):
		return (resp)
	elif (resp == 'n'):
		return(resp)
	else:
		resp = input('>> ERROR. Sólo se admiten los caracteres indicados. Ingrese nuevamente su respuesta: ')
		resp = resp.lower()
		if (resp == 's'):
			return (resp)
		elif (resp == 'n'):
			return(resp)
		else:
			print('\n>> ERROR. Usted necesita anteojos o es bobo. Intente nuevamente desde el comienzo...')
			input('\n-- Presione <ENTER> para continuar --\n')
			menu_principal()


def eliminar_categoria(cat):
	if (os.path.exists('categorias.bin')):
		try:
			f = open('categorias.bin','rb')
			dic = pickle.load(f)
			if (cat in dic):
				resp = input('>> ¿Está seguro que desea eliminar la categoría {0}? [s/n]: '.format(cat))
				if (evaluar_resp(resp) == 's'):
					del dic[cat]
					try:
						f = open('categorias.bin','wb')
						pickle.dump(dic,f)
					except:
						print('>> ERROR. No se puede escribir en el archivo.')
					print('>> La categoría {0} se eliminó correctamente.'.format(cat))
				elif (evaluar_resp(resp) == 'n'):
					print('>> Buena elección.')
				else:
					pass
			else:
				print('>> La categoría {0} no se encuentra en el archivo. No se puede eliminar.'.format(cat))
		except:
			print('>> ERROR al abrir el archivo "categorias.bin".')
			return
		f.close()
	else:
		print('>> ERROR. No existe el archivo "categorias.bin". No se puede continuar.')
	input('\n-- Presione <ENTER> para continuar --\n')
	menu_principal()


def crear_categoria(cat):
	if (os.path.exists('categorias.bin')):
		try:
			f = open('categorias.bin','rb')	
			dic = pickle.load(f)
			if (cat in dic):
				print('>> La categoría ya existe en el archivo!')
				input('\n-- Presione <ENTER> para continuar --\n')
				menu_principal()
			else:
				resp = input('>> La categoría {0} no existe en el archivo. ¿Desea crearla? [s/n]: '.format(cat))
				if (evaluar_resp(resp) == 's'):
					alta_categoría(cat)
				elif (evaluar_resp(resp) == 'n'):
					print('>> No se creó la nueva categoría. Presione <ENTER> para volver al menú principal.')
					input()
				else:
					pass
			f.close()
		except:
			print('>> ERROR al abrir el archivo "categorias.bin".')
			return
	else:
		resp = input('>> El archivo "categorias.bin" no existe. ¿Desea crearlo? [s/n]: ')
		if (evaluar_resp(resp) == 's'):
			crear_archivo()
			try:
				f = open('categorias.bin','rb')	
				dic = pickle.load(f)
				dic[cat] = []		## CREO LA NUEVA CATEGORIA SIN NINGUNA PALABRA EN LA LISTA
				try:
					f = open('categorias.bin','wb')		## CAMBIO EL MODO DE APERTURA DEL ARCHIVO
					pickle.dump(dic,f)		## ESCRIBO EL DICCIONARIO EN EL ARCHIVO
					print('>> La categoría {0} fue agregada correctamente.'.format(cat))
				except:
					print('\n>> ERROR. No se puede escribir en el archivo.')
					return
			except:
				print('\n>> ERROR. No se puede leer el archivo.')
			f.close()
			menu_principal()
		if (evaluar_resp(resp) == 'n'):
			print('\n>> No se puede continuar sin el archivo. Abortando programa...')
			return

def agregar_palabra(cat):
	try:
		f = open ('categorias.bin','rb')
		dic = pickle.load(f)
		pal = input('>> Por favor, ingrese la nueva palabra: ')
		pal = pal.lower()
		dic[cat].append(pal)
		dic[cat].sort()
		try:
			f = open ('categorias.bin','wb')
			pickle.dump(dic,f)
			print ('>> La palabra "{0}" se agregó correctamente a la categoría {1}.'.format(pal,cat))
		except:
			print('>> ERROR. No se puede abrir el archivo para escritura.')
		f.close()
	except:
		print('>> ERROR. No se puede leer el archivo "categorias.bin".')
	input('\n-- Presione <ENTER> para continuar --\n')
	menu_categoria(cat)

def eliminar_palabra(cat):
	try:
		f = open('categorias.bin','rb')
		dic = pickle.load(f)
		lista = dic[cat]
		pal = input('>> Por favor, ingrese la palabra que desea eliminar: ')
		pal = pal.lower()
		if (pal in lista):
			lista.remove(pal)
			dic[cat] = lista
			try:
				f = open('categorias.bin','wb')
				pickle.dump(dic,f)
				print('>> La palabra "{0}"" se ha eliminado correctamente.'.format(pal))
			except:
				print('>> ERROR. No se puede escribir en el archivo.')
				return
		else:
			print('>> ERROR. La palabra "{0}" no se encuentra en la categoría {1}.'.format(pal,cat))
		f.close()
	except:
		print('>> ERROR. No se puede leer el archivo "categorias.bin".')
	input('\n-- Presione <ENTER> para continuar --\n')
	menu_categoria(cat)


def mod_palabra(cat):
	try:
		f = open('categorias.bin','rb')
		dic = pickle.load(f)
		lista = dic[cat]
		pal = input('>> Por favor, ingrese la palabra a modificar: ')
		pal = pal.lower()
		if (pal in lista):
			palNueva = input('>> Ingrese la palabra modificada: ')
			palNueva = palNueva.lower()
			resp = input('\n>> ¿Está seguro que desea cambiar la palabra "{0}" por {1}? [s/n]: '.format(pal,palNueva))
			if (evaluar_resp(resp) == 's'):
				lista.remove(pal)
				lista.append(palNueva)
				lista.sort()
				dic[cat] = lista
				try:
					f = open('categorias.bin','wb')
					pickle.dump(dic,f)
					print('>> La modificación se realizó correctamente.')
				except:
					print('>> ERROR. No se puede escribir en el archivo.')
			elif (evaluar_resp(resp) == 'n'):
				print('\n>> No se realizaron modificaciones. La palabra "{0}" no se encuentra en la categoría "{1}".'.format(pal,cat))
			else:
				pass
			f.close()
	except:
		print('>> ERROR. No se puede leer el archivo "categorias.bin".')
	input('\n-- Presione <ENTER> para continuar --\n')
	menu_categoria(cat)


def ver_palabras(cat):
	try:
		f = open('categorias.bin','rb')
		dic = pickle.load(f)
		lista = dic[cat]
		f.close()
		print('\n>> Palabras en la categoría "{0}":'.format(cat))
		for i in lista:
			print('\t- {0}'.format(i))
	except:
		print('>> ERROR. No se puede leer el archivo "categorias.bin".')
	input('\n-- Presione <ENTER> para continuar --\n')
	menu_categoria(cat)		

		
def verificar_cat(cat):
	if (os.path.exists('categorias.bin')):
		try:
			f = open('categorias.bin','rb')
			dic = pickle.load(f)
			if (cat in dic):
				return True
			else:
				return False
			f.close()
		except:
			print('>> ERROR. No se puede leer el archivo.')
			return
	else:
		print('>> ERROR. El archivo "categorias.bin" aún no fue creado. Por favor seleccione la opción 1 para crearlo.')
		input('\n-- Presione <ENTER> para continuar --\n')
		menu_principal()



def menu_categoria(cat):
	print('\n--------------------- CATEGORÍA {0} ---------------------'.format(cat))
	print('\t 1. Agregar palabra a categoría.')
	print('\t 2. Eliminar palabra de categoría.')
	print('\t 3. Modificar palabra en categoría.')
	print('\t 4. Ver palabras en categoría.')
	print('\t 5. Ver palabra aleatoria.')
	print('\t 6. Menú anterior.')
	opc = int(input('\n>> Opción deseada: '))
	while(opc < 1) or (opc > 6):
		print('>> ERROR. Valor fuera de rango.')
		opc = int(input('\n>> Opción deseada: '))
	if (opc in range(1,7)):
		if (opc == 1):
			agregar_palabra(cat)	
		elif (opc == 2):	
			eliminar_palabra(cat)
		elif (opc == 3):
			mod_palabra(cat)
		elif (opc == 4):
			ver_palabras(cat)	## IMPLEMENTAR
		elif (opc == 5):
			palabra_random(cat)		## IMPLEMENTAR
		elif (opc == 6):
			menu_principal()


def menu_principal():
	try:
		print('--------------------- MENÚ PRINCIPAL ---------------------')
		print('\t 1. Crear categoría.')
		print('\t 2. Eliminar categoría.')
		print('\t 3. Modificar categoría.')
		print('\t 4. Categorias disponibles.')
		print('\t 5. Salir.')
		opc = int(input('\n>> Opción deseada: '))
		while (opc < 1) or (opc > 5):
			print('>> ERROR. Valor fuera de rango.')
			opc = int(input('\n>> Opción deseada:'))
		if (opc in range(1,6)):
			if (opc == 1):
				crear_categoria(leer_categoria())
			elif (opc == 2):
				eliminar_categoria(leer_categoria())
			elif (opc == 3):
				cat = leer_categoria()
				if (verificar_cat(cat) == True):
					menu_categoria(cat)
				else:
					print('>> ERROR. La categoría ingresada no existe. Intente nuevamente.\n')
					menu_principal()
			elif (opc == 4):
				ver_categorias()
			else:
				print('\n>> Fin de programa, vuelva pronto.')		
				return
	except(KeyboardInterrupt):
		print('\n\n>> Fin de programa, vuelva pronto.')

menu_principal()
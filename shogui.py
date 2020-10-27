#!/usr/bin/env python
# -*- coding: utf-8 -*

# Implementacion del juego Shogui por Veronica Gonzalez para Eventbrite

import random

# Se crea el tablero vacio
tablero = ['00'] * 9
for i in range(9):
	tablero[i] = ['00'] * 9

ronda = 0 # Contador de rondas
turno = '0' # v jugador blanco - ^ jugador negro
valido = False # Variable para controlar si la casilla elegida random a mover es valida (tiene una ficha que corresponde al jugador que tiene el turno)
estado = 0 # Variable para controlar si la casilla a la que se mueve una ficha esta ocupada por el mismo jugador (0) o vacia u ocupada por el jugador contrario (1)
completada = False # Variable para controlar si se ha completado la jugada de un jugador
victoria = False # Variable para controlar si algun jugador ha ganado el juego

# Funcion que controla los movimientos de las fichas
def move(x, y):
	
	global completada	
	pieza = tablero[x][y] # La pieza elegida es la que se encuentra en esa posicion

	# Se divide pieza en el nombre y la orientacion
	nombre = pieza[0]
	orientacion = pieza[1]
	
	# Rey 
	if nombre == 'K':

		# Se elige de forma random entre los 8 posibles movimientos del rey
		r = random.randint(1,8)

		# 1 se corresponde con la posicion (x+1, y+1)
		if r == 1:
			pos_x = x+1
			pos_y = y+1
		# 2 se corresponde con (x+1, y)
		if r == 2:
			pos_x = x+1
			pos_y = y
		# 3 se corresponde con (x, y+1)
		if r == 3:
			pos_x = x
			pos_y = y+1
		# 4 se corresponde con (x-1, y-1)
		if r == 4:
			pos_x = x-1
			pos_y = y-1
		# 5 se corresponde con (x-1, y)
		if r == 5:
			pos_x = x-1
			pos_y = y
		# 6 se corresponde con (x, y-1)
		if r == 6:
			pos_x = x
			pos_y = y-1
		# 7 se corresponde con (x+1, y-1)
		if r == 7:
			pos_x = x+1
			pos_y = y-1
		# 8 se corresponde con (x-1, y+1)
		if r == 8:
			pos_x = x-1
			pos_y = y+1

		# Se checkea si la posicion a la que se moveria es valida
		val_pos = check_pos(pos_x, pos_y)
		# Se puede mover
		if val_pos == 1:
			
			print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + ", " + str(y) + " a la posicion " + str(pos_x) + "," + str(pos_y))
			if tablero[pos_x][pos_y] != '00':
				print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][pos_y])

			# Se actualizan las posiciones
			tablero[pos_x][pos_y] = tablero[x][y]
			tablero[x][y] = '00'
			# Se indica que la jugada esta se ha completado
			completada = True
		else:
			completada = False

		return completada
	

	# General oro
	if nombre == 'G':

		# Se elige de forma random entre los 6 posibles movimientos del general de oro
		r = random.randint(1,6)

		# 1 se corresponde con la posicion (x-1, y)
		if r == 1:
			pos_x = x-1
			pos_y = y
		# 2 se corresponde con (x, y+1)
		if r == 2:
			pos_x = x
			pos_y = y+1
		# 3 se corresponde con (x, y-1)
		if r == 3:
			pos_x = x
			pos_y = y-1
		# 4 se corresponde con (x+1, y)
		if r == 4:
			pos_x = x+1
			pos_y = y

		if r == 5:
			# 5 se corresponde con (x+1, y-1) para el turno v
			if turno == 'v':
				pos_x = x+1
				pos_y = y-1
			# 5 se corresponde con (x-1, y-1) para el turno ^
			else:
				pos_x = x-1
				pos_y = y-1
		if r == 6:
			# 6 se corresponde con (x+1, y+1) para el turno v
			if turno == 'v':
				pos_x = x+1
				pos_y = y+1
			# 6 se corresponde con (x-1, y+1) para el turno ^
			else:
				pos_x = x-1
				pos_y = y+1

		# Se checkea si la posicion a la que se moveria es valida
		val_pos = check_pos(pos_x, pos_y)
		# Se puede mover
		if val_pos == 1:
			print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(pos_x) + "," + str(pos_y))
			if tablero[pos_x][pos_y] != '00':
				print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][pos_y])

			# Se actualizan las posiciones
			tablero[pos_x][pos_y] = tablero[x][y]
			tablero[x][y] = '00'
			# Se indica que la jugada esta se ha completado
			completada = True
		else:
			completada = False

		return completada

	# General plata
	if nombre == 'S' :

		# Se elige de forma random entre los 5 posibles movimientos del general de plata
		r = random.randint(1,5)

		# 1 se corresponde con la posicion (x-1, y-1)
		if r == 1:
			pos_x = x-1
			pos_y = y-1
		# 2 se corresponde con (x+1, y+1)
		if r == 2:
			pos_x = x+1
			pos_y = y+1
		# 3 se corresponde con (x+1, y-1)
		if r == 3:
			pos_x = x+1
			pos_y = y-1
		# 4 se corresponde con (x-1, y+1)
		if r == 4:
			pos_x = x-1
			pos_y = y+1

		if r == 5:
			# 5 se corresponde con (x+1, y) para el turno v
			if turno == 'v':
				pos_x = x+1
				pos_y = y
			# 5 se corresponde con (x-1, y) para el turno ^
			else:
				pos_x = x-1
				pos_y = y


		# Se checkea si la posicion a la que se moveria es valida
		val_pos = check_pos(pos_x, pos_y)
		# Se puede mover
		if val_pos == 1:
			print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(pos_x) + "," + str(pos_y))
			if tablero[pos_x][pos_y] != '00':
				print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][pos_y])

			# Se actualizan las posiciones
			tablero[pos_x][pos_y] = tablero[x][y]
			tablero[x][y] = '00'
			# Se indica que la jugada esta se ha completado
			completada = True
		else:
			completada = False

		return completada


	# Caballo
	elif nombre == 'H':
		# Se elige de forma random entre los 2 posibles movimientos del caballo
		r = random.randint(1,2)

		if r == 1:
			# 1 se corresponde con (x+2, y+1) para el turno v
			if turno == 'v':
				pos_x = x+2
				pos_y = y+1
			# 1 se corresponde con (x-2, y+1) para el turno ^
			else:
				pos_x = x-2
				pos_y = y+1
		if r == 2:
			# 2 se corresponde con (x+2, y-1) para el turno v
			if turno == 'v':
				pos_x = x+2
				pos_y = y-1
			# 2 se corresponde con (x-2, y-1) para el turno ^
			else:
				pos_x = x-2
				pos_y = y-1


		# Se checkea si la posicion a la que se moveria es valida
		val_pos = check_pos(pos_x, pos_y)
		# Se puede mover
		if val_pos == 1:
			print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(pos_x) + "," + str(pos_y))
			if tablero[pos_x][pos_y] != '00':
				print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][pos_y])

			# Se actualizan las posiciones
			tablero[pos_x][pos_y] = tablero[x][y]
			tablero[x][y] = '00'
			# Se indica que la jugada esta se ha completado
			completada = True
		else:
			completada = False

		return completada

	# Lancero
	if nombre == 'L':
		
		# Array para guardar las posiciones ocupadas en la fila que no sean lanceros
		ocupado = []

		# Variable auxiliar para ver cuantas casillas se puede mover el lancero
		casillas = 0

		# Se elige de forma random un numero de casillas que avanzar hacia delante
		r = random.randint(1,8)

		# Se almacenan las fichas que hay en la columna del lancero elegido
		for j in range(0,8):
			if turno == 'v':
				if tablero[j][y] != '00' and tablero[j][y] != 'Lv':
					ocupado.append(j)
			else:
				if tablero[j][y] != '00' and tablero[j][y] != 'L^':
					ocupado.append(j)

		# La columna esta vacia asi que se avanzan r posiciones 
		if len(ocupado) == 0:
			casillas = r
			# La direccion de movimiento en x difiere segun el jugador
			if turno == 'v':
				pos_x = x+casillas
			else:
				pos_x = x-casillas
		
		# Hay una ficha asi que solo se puede avanzar hasta donde este esa ficha para comerla
		else:
			if turno == 'v':
				ficha = tablero[ocupado[0]][y]		
				casillas = ocupado[0]
				pos_x = casillas
				if ficha[1] == turno:
					pos_x = casillas-1
				else:
					pos_x = casillas
			else:
				ficha = tablero[ocupado[len(ocupado)-1]][y]
				casillas = ocupado[len(ocupado)-1]
				if ficha[1] == turno:
					pos_x = casillas+1
				else:
					pos_x = casillas
		
		# Se checkea si la posicion a la que se moveria es valida
		val_pos = check_pos(pos_x, y)
		# Se puede mover
		if val_pos == 1:
			print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(pos_x) + "," + str(y))
			if tablero[pos_x][y] != '00':
				print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][y])

			# Se actualizan las posiciones
			tablero[pos_x][y] = tablero[x][y]
			tablero[x][y] = '00'
			# Se indica que la jugada esta se ha completado
			completada = True
		else:
			completada = False

		return completada

	# Alfil
	#if nombre == 'A':

		# NO PROGRAMADO

	
	# Torre
	if nombre == 'T':

		# Array para guardar las posiciones ocupadas en la fila
		ocupado = []

		# Variable auxiliar para ver cuantas casillas se puede mover la torre
		casillas = 0

		# Se elige de forma random un numero de casillas que se puede avanzar
		r = random.randint(1,8)

		# Se elige de forma random la orientacion del movimiento de la torre (vertical (1) o horizontal (2))
		orientacion = random.randint(1,2)
		
		# Direccion vertical
		if orientacion == 1:
			# Se almacenan las fichas que hay en la columna de la torre elegida
			for j in range(0,8):
				if turno == 'v':
					if tablero[j][y] != '00' and tablero[j][y] != 'Tv':
						ocupado.append(j)
				else:
					if tablero[j][y] != '00' and tablero[j][y] != 'T^':
						ocupado.append(j)

			# Se elige de forma random la direccion del movimiento (hacia abajo (1) o hacia arriba (2))
			direccion = random.randint(1,2)
			# La columna esta vacia asi que se avanzan r posiciones 
			if len(ocupado) == 0:
				casillas = r
				# La direccion de movimiento en x difiere segun el jugador
				if direccion == 1:
					pos_x = x+casillas

				else:
					pos_x = x-casillas
			
			# Hay una ficha asi que solo se puede avanzar hasta donde este esa ficha para comerla
			else:
				if turno == 'v':
					ficha = tablero[ocupado[0]][y]		
					casillas = ocupado[0]
					pos_x = casillas
					if ficha[1] == turno:
						pos_x = casillas-1
					else:
						pos_x = casillas
				else:
					ficha = tablero[ocupado[len(ocupado)-1]][y]
					casillas = ocupado[len(ocupado)-1]
					if ficha[1] == turno:
						pos_x = casillas+1
					else:
						pos_x = casillas
			
			# Se checkea si la posicion a la que se moveria es valida
			val_pos = check_pos(pos_x, y)
			# Se puede mover
			if val_pos == 1:
				print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(pos_x) + "," + str(y))
				if tablero[pos_x][y] != '00':
					print("La pieza " + pieza + " se ha comido a " + tablero[pos_x][y])

				# Se actualizan las posiciones
				tablero[pos_x][y] = tablero[x][y]
				tablero[x][y] = '00'
				# Se indica que la jugada esta se ha completado
				completada = True
			else:

				completada = False

		# Direccion horizontal
		else:
			# Se almacenan las fichas que hay en la fila de la torre elegida
			for j in range(0,8):
				if turno == 'v':
					if tablero[x][j] != '00' and tablero[x][j] != 'Tv':
						ocupado.append(j)
				else:
					if tablero[x][j] != '00' and tablero[x][j] != 'T^':
						ocupado.append(j)

			# Se elige de forma random la direccion del movimiento (izquierda (1) o derecha (2))
			direccion = random.randint(1,2)
			
			# La columna esta vacia asi que se avanzan r posiciones 
			if len(ocupado) == 0:
				casillas = r
				
				# La direccion de movimiento en x difiere segun el jugador
				if direccion == 1:
					pos_y = y-casillas
				else:
					pos_y = y+casillas
			
			# Hay una ficha asi que solo se puede avanzar hasta donde este esa ficha para comerla
			else:
				# Si el obstaculo esta a la derecha de la torre
				if ocupado[0] > y:
					ficha = tablero[x][ocupado[0]]		
					casillas = ocupado[0]
					pos_y = casillas
					if ficha[1] == turno:
						pos_y = casillas-1
					else:
						pos_y = casillas

				# Si el obstaculo esta a la izquierda de la torre
				else:
					ficha = tablero[x][ocupado[0]]		
					casillas = ocupado[0]
					pos_y = casillas
					if ficha[1] == turno:
						pos_y = casillas+1
					else:
						pos_y = casillas
		
			
			# Se checkea si la posicion a la que se moveria es valida
			val_pos = check_pos(x, pos_y)
			# Se puede mover
			if val_pos == 1:
				print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(x) + "," + str(pos_y))
				if tablero[x][pos_y] != '00':
					print("La pieza " + pieza + " se ha comido a " + tablero[x][pos_y])

				# Se actualizan las posiciones
				tablero[x][pos_y] = tablero[x][y]
				tablero[x][y] = '00'
				# Se indica que la jugada esta se ha completado
				completada = True
			else:
				completada = False
		return completada
	
	# Peon
	if nombre == 'P':
		# Si el jugador es v
		if turno == 'v':
			# Se checkea si la posicion a la que se moveria es valida
			val_pos = check_pos(x+1, y)
			# Se puede mover
			if val_pos == 1:
				print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(x+1) + "," + str(y))
				if tablero[x+1][y] != '00':
					print("La pieza " + pieza + " se ha comido a " + tablero[x+1][y])

				# Se actualizan las posiciones
				tablero[x+1][y] = tablero[x][y]
				tablero[x][y] = '00'
				# Se indica que la jugada esta se ha completado
				completada = True
			else:
				completada = False
		# Si el jugador es ^
		else:
			# Se checkea si la posicion a la que se moveria es valida -- si es asi se actualiza el estado del tablero
			val_pos = check_pos(x-1, y)
			# Se puede mover
			if val_pos == 1:
				print("Se mueve la pieza " + pieza + " de la posicion " + str(x) + "," + str(y) + " a la posicion " + str(x-1) + "," + str(y))
				if tablero[x-1][y] != '00':
					print("La pieza " + pieza + " se ha comido a " + tablero[x-1][y])

				# Se actualizan las posiciones
				tablero[x-1][y] = tablero[x][y]
				tablero[x][y] = '00'
				# Se indica que la jugada se ha completado
				completada = True
			else:
				completada = False
		return completada

# Funcion para elegir una casilla con ficha valida para mover (no esta vacia y corresponde al jugador que tiene el turno)
def check_casilla():
	
	global turno, valido

	x = random.randint(0, 8)
	y = random.randint(0, 8)

	ficha = tablero[x][y]

	# Se ha elegido una casilla vacia
	if ficha == '00':	
		return -1, -1

	# Se ha elegido una casilla no vacia
	else:
		# Si la ficha elegida no corresponde al jugador que tiene el turno
		if ficha[1] != turno:
			return -1, -1 

		# Si la ficha elegida corresponde al jugador que tiene el turno se devuelve
		else:
			valido = True			
			return x, y

# Funcion para checkear si se puede mover a cierta posicion
def check_pos(x,y):
	global estado

	# Posicion invalida (fuera de los limites)
	if x < 0 or x > 8 or y < 0 or y > 8:
		estado = 0 
		return estado

	valor_ficha = tablero[x][y]

	# Posicion invalida (posicion con una ficha del mismo jugador)
	if valor_ficha[1] == turno:
		estado = 0 
		return estado

	# Posicion vacia u ocupada por el jugador contrario
	else:
		estado = 1
		return estado

# Funcion para generar la jugada de cada jugador
def jugada():
	global valido 

	# Se elige una casilla valida
	while(valido == False):
		x, y = check_casilla()

	# Se mueve la ficha elegida
	move(x, y)

	valido = False # Se reseta la variable valido para el siguiente jugador

# Funcion para cambiar turno
def cambiar_turno():
	global turno

	if turno == '^':
		turno = 'v'
	else:
		turno = '^'

	return turno

# Funcion para comprobar si se ha ganado la partida
def check_ganar():
	global victoria

	# Se declaran variables para almacenar si existen los dos reyes en la partida
	Kv = False
	K = False
	# Se recorre todo el tablero
	for i in range(9):
		for j in range(9):
			if tablero[i][j] == 'Kv':
				Kv = True
			if tablero[i][j] == 'K^':
				K = True

	# Ha ganado el jugador ^
	if Kv == False:
		print("Ha ganado el jugador ^")
		print("¡FIN DE LA PARTIDA!")
		victoria = True

	# Ha ganado el jugador v
	if K == False:
		print("Ha ganado el jugador v")
		print("¡FIN DE LA PARTIDA!")	
		victoria = True
	return

def main():

	global ronda, turno, valido, completada, victoria

	# Si es la ronda inicial se inicializa el tablero
	if ronda == 0:
		# Inicializacion del tablero
		# Para el jugador de arriba (blanco - v)
		tablero[0][4] = 'Kv' # Rey
		tablero[0][3] = 'Gv' # General de oro 
		tablero[0][5] = 'Gv' # General de oro 
		tablero[0][2] = 'Sv' # General de plata 
		tablero[0][6] = 'Sv' # General de plata 
		tablero[0][1] = 'Hv' # Caballo 
		tablero[0][7] = 'Hv' # Caballo 
		tablero[0][0] = 'Lv' # Lancero 
		tablero[0][8] = 'Lv' # Lancero
		tablero[1][7] = 'Av' # Alfil 
		tablero[1][1] = 'Tv' # Torre

		# Peones
		for i in range(9):
			tablero[2][i] = 'Pv'

		# Para el jugador de abajo (negro - ^)
		tablero[8][4] = 'K^' # Rey
		tablero[8][3] = 'G^' # General de oro 
		tablero[8][5] = 'G^' # General de oro 
		tablero[8][2] = 'S^' # General de plata 
		tablero[8][6] = 'S^' # General de plata 
		tablero[8][1] = 'H^' # Caballo 
		tablero[8][7] = 'H^' # Caballo 
		tablero[8][0] = 'L^' # Lancero 
		tablero[8][8] = 'L^' # Lancero
		tablero[7][1] = 'A^' # Alfil 
		tablero[7][7] = 'T^' # Torre

		# Peones
		for i in range(9):
			tablero[6][i] = 'P^'

		ronda += 1

		# Se imprime el tablero inicial
		print("TABLERO INICIAL")
		for i in range(9):
			print(tablero[i])

		print("-----------------------------------")

		# Se inicializa el turno de forma aleatoria
		turno = random.choice(['^', 'v'])

	# Mientras ninguno de los dos jugadores haya ganado 
	while victoria == False:
	
		print("Ronda: " + str(ronda))

		# Se imprime el turno
		print("Es el turno de: " + turno)

		# Juega el primer jugador de la ronda
		while completada == False:
			jugada()	
		
		completada = False

		# Se comprueba si se ha ganado
		check_ganar()
		if victoria == True:
			return

		# Se cambia el turno
		cambiar_turno()

		# Se imprime el turno
		print("Es el turno de: " + turno)

		# Juega el segundo jugador de la ronda
		while completada == False:
			jugada()	
		
		completada = False

		# Se comprueba si se ha ganado
		check_ganar()
		if victoria == True:
			return

		# Se cambia el turno
		cambiar_turno()

		# Se pasa a la siguiente ronda
		ronda += 1
	
		# Se imprime el tablero actual
		print("TABLERO")
		for i in range(9):
			print(tablero[i])
		print("-----------------------------------")

	return

if __name__ == '__main__':
	main()

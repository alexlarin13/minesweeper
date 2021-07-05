import random as r
N, M = (5, 10) # размер игрового поля (N x N) и M мин на поле

def getTotalMines():
	n = 0
	for k in range(-1, 2):
		for l in range(-1, 2):
			x = i + k
			y = j + l
			if x < 0 or x >= N or y < 0 or y >= N:
				continue
			if PM[x * N + y] < 0:
				n += 1
	return n


def createGame(PM):
	'''Создание игрового поля:
	расположение мин и подсчет числа мин воткруг
	клеток без мин '''

	rng = r.Random()

	n = M
	while  n > 0:
		i = rng.randrange(N) #создание случайных мин на поле по координатам
		j = rng.randrange(N)
		if PM[i * N + j] != 0:
			continue
		P[i * N + j] = -1
		n -= 1
	
	# вычисляем количество мин вокруг клетки
	for i in range(N):
		for j in range(N):
			if PM[i * N + j] == 0:
				PM[i * N + j] = getTotalMines(PM, i, j)


def show():
	'''функция отображения игрового поля'''
	pass

def goPlayer():
	'''Функция для ввода пользователем координат
	закрытой клетки игрового поля'''

def isFinish():
	'''определение текущего состояния игры:
	выиграли, проиграли или игра продолжается'''


def startGame():
	'''функция запуска игры. отображается игрвоое поле
	игрок открывает закрытую клетку, выдается результат'''

	P = [-2] * N * N # игровое поле
	PM = [0] * N * N # поле мин

	createGame(PM)

	while isFinish():
		show()
		goPlayer()



startGame()
print('Игра завершена')
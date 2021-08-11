from tkinter import *
from typing import List, Dict

__author__ = 'SlavaGolovatskyu'
__version__ = '1.1'


"""
При создания класса тоисть
PlaceHold = PlaceHolder(arg1, arg2, arg3) нужно передать все строки тоисть 3 строки и больше.
"""

class PlaceHolder:
	def __init__(
		self, 
		arg1: str, 
		arg2: str, 
		arg3: str = None, 
		arg4: str = None
	) -> None:
	
		self.MainDict: Dict[int, str] = {
			1: arg1,  # Строка которую вы хотите впихнуть в первый Entry
			2: arg2,  # Строка которую вы хотите впихнуть во второй Entry и т.д
			3: arg3,
			4: arg4
		}

	""" number это цифра Entry сперва биндите Entry на клик. После чего этой функцие передаете номер Entry
	    Допустим enter.bind('<Button-1>', giveNumber)
	    def giveNumber(event):
	        DeletePlaceHolder(1, 2) 1 аргумент это номер Entry 2 аргумент количество всех Entry's
	        3, 4 аргументы обьязательны это переменые самих Entry's Тоисть создали вы например такую переменую:
	        enter = Entry() в 3 аргумент данной функции передаете эту переменую и следующие
	НА ДАННЫЙ МОМЕНТ ФУНКЦИЯ РАБОТАЕТ НОРМАЛЬНО ВСЕГОЛИШ С 2 и 3 АРГУМЕНТАМИ 4 и больше неработают. 
	"""

	def DeletePlaceHolder(
		self, 
		number: int, 
		CountEnter: int, 
		entry: Entry, 
		entry_2: Entry, 
		entry_3: Entry = None
	) -> None:
		# Делаем генератор списка. С проверкой. Если i не равно numb добавляем елемент. В ином случае пропускаем.
		generator_entrys: List[int] = [i for i in range(1, CountEnter + 1) if i != number]

		# Ищем главную Entry
		MainEnter: Entry = entry if number == 1 else entry_2 if number == 2 else entry_3

		# Ищем 2 Entry
		SecondEnter: Entry = entry if generator_entrys[0] == 1 else entry_2

		if CountEnter == 2:
			# Добавляем главное число в список которое передали в нашу функцию.
			generator_entrys.append(number)
			messages: Dict[int, str] = {
				generator_entrys[0]: SecondEnter.get(),
				# После того как добавили число в список появился елемент с идексом 1
				generator_entrys[1]: MainEnter.get()
			}

		elif CountEnter == 3:
			# Как и было сказано раньше если код заходит в проверку. Некоторые переменые меняют свои значение.
			ThreeEnter: Entry = entry_2 if generator_entrys[1] == 2 else entry_3
			messages: Dict[int, str] = {
				# SecondEnter это найденый второй Entry
				generator_entrys[0]: SecondEnter.get(),
				# ThreeEnter это найденый третий Entry
				generator_entrys[1]: ThreeEnter.get()
			}

		# Метод delete удаляет данные. Метод insert записывает данные.
		# Если хотите разобраться в проверках советую просмотреть на словать в def __init__():
		# Так будет проще понять что и как я делал.
		if (self.MainDict[generator_entrys[0]] == messages[generator_entrys[0]] and 
		   self.MainDict[generator_entrys[1]] == messages[generator_entrys[1]]
		):
			MainEnter.delete(0, END)
		else:
			if CountEnter == 2:
				if self.MainDict[generator_entrys[1]] != messages[generator_entrys[1]] and not messages[generator_entrys[1]]:
					# В главном Entry записываем данные.
					MainEnter.insert(0, self.MainDict[generator_entrys[1]])
					# Во-втором Entry удаляем все данные
					SecondEnter.delete(0, END)
				if self.MainDict[generator_entrys[0]] != messages[generator_entrys[0]] and not messages[generator_entrys[0]]:
					SecondEnter.insert(0, self.MainDict[generator_entrys[0]])
					MainEnter.delete(0, END)
				MainEnter.delete(0, END)
			else:
				if self.MainDict[generator_entrys[0]] != messages[generator_entrys[0]] and not messages[generator_entrys[0]]:
					SecondEnter.insert(0, self.MainDict[generator_entrys[0]])
					MainEnter.delete(0, END)

				if self.MainDict[generator_entrys[1]] != messages[generator_entrys[1]] and not messages[generator_entrys[1]]:
					ThreeEnter.insert(0, self.MainDict[generator_entrys[1]])
					MainEnter.delete(0, END)
				MainEnter.delete(0, END)

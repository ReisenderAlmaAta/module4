num = int(input('Из скольки чисел состоит массив: '))

def binary_search(ls, target):
	low = 0
	high = len(ls) - 1 
	guess = 0
	while guess != target:
		mid = (low + high) // 2
		guess = ls[mid]
		if guess == target:
			return  ls[mid]
		elif guess > target:
			high = mid - 1
		else: 
			low = mid + 1 

ls = [i for i in range(1, num + 1)]

import random
target = random.randint(1, num)


print('target =', target) # целевое число вывожу для проверки работы алгоритма
print(binary_search(ls, target))

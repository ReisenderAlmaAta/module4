def rand_list(n):
	from random import randint as r
	tmp = set()
	while len(tmp) < n:
		tmp.add(r(1, 10000))
	res = list(tmp)
	print('unsorted list is:', res, sep='\n')
	return(res)

def insert_sort(ls):
	n = len(ls)
	for top in range(1, n):
		k = top
		while k > 0 and ls[k - 1] > ls[k]:
			ls[k], ls[k-1] = ls[k-1], ls[k]
			k -= 1
	return (ls)

ls_srt = insert_sort(rand_list(int(input('Введите размер списка: '))))
print('sorted list is:', ls_srt, sep='\n')



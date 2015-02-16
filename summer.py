
__author__ = 'jgs3cd'

from helper import sumstuff

lst = []
with open('input.txt', 'r') as fin:
	while fin:
		x = int(fin.readline())
		lst.append(x)
print(sumstuff(lst))
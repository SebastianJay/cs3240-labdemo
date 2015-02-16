
__author__ = 'jgs3cd'

from helper import sumstuff

lst = []
print('Enter ints, or 0 to quit')
while True:
	x = int(input())
	if x == 0:
		break
	lst.append(x)
print('Sum is',sumstuff(lst))

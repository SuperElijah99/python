# save this file as random_int.py
from random import randint
def ranint():
	r = randint(65,91)
	return r
	
def main():
	for r in range (1000):
		ri = ranint()
		print (ri,end="")

main()
# grep 65 100000ints.txt | more



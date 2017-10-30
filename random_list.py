# save this file as random_int.py
from random import randint
def randlist(r):
	alpha = ["A","b","B,","c","C","d"]
	used[r] = 1
	sum = sum + usedlist[r]
	c = alpha[r]
	return c
	


# initial variables
def main():
	used = [0,0,0,0,0,0]
	done = False #boolean 
	######################
	while done == False:
		r = randint(0,5) # make a random number
		c = randlist(r)
		#print (used)
		#print(c,end="")
main()


 

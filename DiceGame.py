	# Gideon C's take on ADG
	# with assist from Nathan H & RLR
	
import random
	
def diceroll():
		random.seed()
		global d1, d2, sum, point
		d1=random.randint(1,6)
		d2=random.randint(1,6)
		sum=(d1+d2)
		
if name =='__main__':
		global cash,bet
		playing=True
		cash=1000
		print('You have ',cash,'dollars!')
		while playing==True:
			while True:
				try:
					bet=int(input('How much to bet: $'))
					if bet>cash:
						raise ValueError
					break
				except:
					print("That's not a valid betting amount...")
				bet=int(bet)
				diceroll()
				print('dice d1 = ',d1,'dice d2 = ',d2,'sum is ',sum)
				if(sum==7 or sum==11):
					cash=cash+bet
					print('You WIN and now have',cash,'dollars.')
				elif(sum==2 or sum==3 or sum==12):
					cash=cash-bet
					print ('You LOSE and now have',cash,'dollars.')
				else:
					print ('Your POINT is ',sum,'.You must now roll ',sum,' before you roll a 7 in order to add to your $',cash,' cash.')
					point=sum
					while(sum!=7):
						diceroll()
						print('You rolled a ',sum)
						if (sum==point):
							cash==cash+bet
							print('You WIN and now have ',cash,' dollars.')
							break
					else:
						cash=cash-bet
						print('You LOSE and now have ',cash,' dollars.')
				if cash<=0:
					print('You ran out of money.')
					playing=False
				else:
					test playin=input('Would you like to play again? ')
					if test playing=='y' or test playing=='yes' or test playing=='si' or test playing=='ja':
						pass
					else:
						playing=False
		

'''
war
optimal strategy:
-> put anything (no strategy)
<- put lightest stone, heavier than given stone. if no such stone, put the lightest stone.

deceitful strategy:
start from lightest stone
if opponent has a lighter stone, say my stone is heavier than opponents heaviest.
if opponent doesn't have a lighter stone (we lose), then say it's lighter than opponents heaviest.
'''

import sys

def war(mine, their):
	mine = sorted(mine)
	their = sorted(their)
	# make the losing-comparisons
	i = 0
	j = 0
	while i < len(mine):
		a = mine[i]
		# find stone bigger than my stone
		while j < len(their) and a > their[j]:
			j += 1
		if j == len(their):
			break
		else:
			# dispense stone found..
			j += 1
		i+=1
	# now all the wins will happen
	return len(mine)-i

def dwar(mine, their):
	mine = sorted(mine)
	their = sorted(their)
	wins = 0
	low = 0
	high = len(their)-1
	for a in mine:
		if a > their[low]:
			# win! (say my stone is very heavy)
			wins += 1
			low += 1
		else:
			high-=1
	return wins
	

def main():
	# how many test cases we have
	T = int(sys.stdin.readline().strip())
	for test_case in range(T):
		N = int(raw_input())
		
		mine = map(float, raw_input().split())
		their = map(float, raw_input().split())
		mine = sorted(mine)
		their = sorted(their)
		
		#print mine, their
		# war
		wwar = war(mine, their)
		
		# dwar
		wdwar = dwar(mine, their)
		
		print 'Case #%d: %d %d' % (test_case+1, wdwar, wwar)

if __name__ == '__main__':
	main()
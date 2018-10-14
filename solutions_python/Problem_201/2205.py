import numpy
import bisect
import math
from random import randrange

def gcd(a,b):
	if b > a:
		return gcd(b, a)
	if a % b == 0:
		return b
	return gcd(b, a % b) 

def simplify_fraction(numer, denom):
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    return [reduced_num,reduced_den]
    

def pancakes():
	cases = int(input())
	for case in range(0,cases):
		pancake = str(input()).split()
		K = int(pancake[1])
		pancake = pancake[0]
		flips = 0
		boolCake = []
		for i in pancake:
			if(i=='+'):
				boolCake.append(True)
			else:
				boolCake.append(False)
		for i in range(0,len(boolCake)):
			if(not boolCake[i]):
				if(i+K > len(boolCake)):
					print("Case #" + str(case+1) + ": IMPOSSIBLE")
					i = 9999
					break
				else:
					flips += 1
					for m in range(i,i+K):
						boolCake[m] = not boolCake[m]
		if(i!=9999):
			print("Case #" + str(case+1) + ": " + str(flips))

def tidynumbers():
	cases = int(input())
	for case in range(0,cases):
		num = int(input())
		isTidy = False
		while (not isTidy):
			isTidy = True
			#Check if Tidy
			numtemp = str(num)
			isTidy = all(numtemp[i]<=numtemp[i+1] for i in range(0,len(numtemp)-1))
			if(not isTidy):
				num -=1
				while(num % 10 != 9):
					num -= 1
				numtemp = str(num)
				isTidy = all(numtemp[i]<=numtemp[i+1] for i in range(0,len(numtemp)-1))
				if(not isTidy):
					if (numtemp[0] != '1'):
						tempn = int(numtemp[0])
						tempn -= 1
						length = len(numtemp)
						numtemp = str(tempn)
						numtemp += "9"*(length-1)
					else:
						numtemp = "9" * (len(numtemp)-1)
					num = int(numtemp)
		print("Case #" + str(case+1) + ": " + str(num))

def recursiveStalls(left, right, K):
	length = right - left + 1
	if(K==0):
		return(9999999,99999999)
	if(K == 1):
		if(length%2 == 0):
			newPosition = (right + left - 1)/2
		else:
			newPosition = (right + left)/2
		return (right - newPosition - 1, newPosition - left - 1)
	else:
		if(length %2 != 0):
			newPosition = (right + left)/2
			K = K-1
			return recursiveStalls(newPosition,right, math.ceil(K/2))
		else:
			newPosition = (right + left - 1)/2
			K = K-1
			(min1,max1) = recursiveStalls(left, newPosition,math.floor(K/2))#ADD K
			(min2,max2) = recursiveStalls(newPosition, right,math.ceil(K/2))#ADD K
			if(min1>min2):
				return (min2,max2)
			else:
				return (min1,max1)
			#return recursiveStalls(newPosition, right,math.floor(K/2))

def bathroomstalls():
	cases = int(input())
	for case in range(0,cases):
		N,K = map(int, input().split())
		stalls = [True] + N*[False] + [True]
		filled = [0,N+1]
		##METHOD 1
		#for person in range(0, K):
		#	left = 0
		#	right = 0
		#	maxlength = 0
		#	for i in range(0, len(stalls)):
		#		if(not stalls[i]):
		#			right = i
		#		else:
		#			length = right - left + 1
		#			if(length > maxlength):
		#				maxlength = length
		#				maxright = right
		#				maxleft = left
		#			left = i+1
		#	if(maxlength%2 == 0):
		#		newPosition = (maxright + maxleft - 1)/2
		#	else:
		#		newPosition = (maxright + maxleft)/2
		#	stalls[int(newPosition)] = True
		#
		#	print("Case #" + str(case+1) + ": " + str(int(maxright - newPosition - 1)) + ' ' + str(int(newPosition - maxleft - 1)))
		##METHOD 2
		#for person in range(0,K):
		#	left = filled[0]
		#	maxlength = 0
		#	for i in range(1, len(filled)):
		#		right = filled[i]
		#		length = right - left + 1
		#		if(length>maxlength):
		#			maxlength = length
		#			maxright = right
		#			maxleft = left
		#		left = right
		#	if(maxlength%2 == 0):
		#		newPosition = (maxright + maxleft - 1)/2
		#	else:
		#		newPosition = (maxright + maxleft)/2
		#	bisect.insort_left(filled,newPosition)
		#	print("Case #" + str(case+1) + ": " + str(int(maxright - newPosition - 1)) + ' ' + str(int(newPosition - maxleft - 1)))
		#
		##METHOD 3
		left = filled[0]
		right = filled[1]
		(a,b) = recursiveStalls(left,right,K)

		print("Case #" + str(case+1) + ": " + str(int(a)) + ' ' + str(int(b)))
		#		






bathroomstalls()
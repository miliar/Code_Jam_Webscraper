import sys
import math

def find_letter(letter, lst):
    return any(letter in word for word in lst)

n = int(input())
for i in range(n):
	R, C = [int(i) for i in input().split()]
	cake = []
	cakebis = []
	for j in range(R):
		st = input()
		cake.append(st)
		cakebis.append(list(st))

	for j in range(R):
		for k in range(C):
			if (cake[j][k] == '?'): continue
			# horizontal droite
			jbis = j
			kbis = k+1
			cakebis[j][k] = cake[j][k]
			while (kbis < C and cakebis[jbis][kbis] == '?') :
				cakebis[jbis][kbis] = cake[j][k]
				kbis += 1

			# horizontal gauche
			jbis = j
			kbis = k-1
			while (kbis >= 0 and cakebis[jbis][kbis] == '?') :
				cakebis[jbis][kbis] = cake[j][k]
				kbis -= 1
	for j in range(R):
		for k in range(C):
			if (cakebis[j][k] == '?'): continue

			jbis = j+1
			kbis = k
			while (jbis < R and cakebis[jbis][kbis] == '?') :
				cakebis[jbis][kbis] = cakebis[j][k]
				jbis += 1

			# bas
			jbis = j-1
			kbis = k
			while (jbis >= 0 and cakebis[jbis][kbis] == '?') :
				cakebis[jbis][kbis] = cakebis[j][k]
				jbis -= 1
 			


	print("Case #" + str(i+1) + ": ")
	if (not find_letter('?', cake)):
		print("\n".join(cake))
	else:
		for j in range(R):
			print("".join(cakebis[j]))
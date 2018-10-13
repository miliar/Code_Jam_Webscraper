#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *

def findNextPalindrome(nombre):
	chiffres = str(nombre)
	premiers_chiffres = chiffres[:len(chiffres)/2]
	palindrome = premiers_chiffres
	if len(chiffres) % 2 == 1:
		palindrome += chiffres[len(chiffres)/2]
	for i in range(len(premiers_chiffres)):
		palindrome += premiers_chiffres[len(premiers_chiffres) - i -1]
	if long(palindrome) < nombre:
		entier = str(long(premiers_chiffres) + 1)
		if len(chiffres) % 2 == 1:
			entier += chiffres[len(chiffres)/2]
		for i in range(len(premiers_chiffres)):
			entier += premiers_chiffres[len(premiers_chiffres) - i -1]
		return findNextPalindrome(long(entier))
	return long(palindrome)

def isAPalindrome(nombre):
	chiffres = str(nombre)
	for i in range(len(chiffres) / 2):
		if chiffres[i] != chiffres[len(chiffres) - i -1]:
			return False
	return True


inputFile = open("C-small-attempt0.in","r")
solution = open("C-small-attempt0.out","w")

T = int(inputFile.readline().split("\n")[0])

for i in range(T):
	ligne = inputFile.readline().split("\n")[0]
	A,B = long(ligne.split(" ")[0]), long(ligne.split(" ")[1])
	currentPalindrome = findNextPalindrome(long(floor(sqrt(A))))
	nbPalindromesAuCarre = 0
	
	while currentPalindrome <= long(floor(sqrt(B))):
		carre = currentPalindrome * currentPalindrome
		if isAPalindrome(carre) and carre >= A and carre <= B:
			nbPalindromesAuCarre += 1
			print i,currentPalindrome, currentPalindrome * currentPalindrome
		currentPalindrome = findNextPalindrome(currentPalindrome + 1)
	
	print nbPalindromesAuCarre
	solution.write("Case #"+str(i+1)+": "+str(nbPalindromesAuCarre)+"\n")

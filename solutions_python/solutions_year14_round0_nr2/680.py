# CookieClickerAlpha.py
"""
date: 2014-04-12
description: A program solving the 2014 Google Code Jam Problem B.
"""
import string

def readfile(filename):
	fInput = open(filename, 'r')
	lstCases = []

	caseNum = int(fInput.readline())
	for index in range(0, caseNum):
		lstCases.append(string.replace(fInput.readline(), '\n', '').split(' '))

	# print lstCases
	return lstCases

def process(lstCases):
	fOutput = open('B-large.out', 'w')
	cnCase = 0

	for case in lstCases:
		cnCase += 1

		farm = float(case[0])
		extra = float(case[1])
		target = float(case[2])

		rate = 2.0
		totalTime = 0.0

		while farm/rate + target/(rate+extra) < target/rate:
			totalTime += farm/rate
			rate += extra
		totalTime += target/rate

		fOutput.write('Case #'+str(cnCase)+': '+str(round(totalTime, 7))+'\n')

	fOutput.close()

def main():
	filename = 'B-large.in'
	process(readfile(filename))

if __name__ == '__main__':
	main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  QB.py
#  
"""
Problem

In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.

Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy.

Example

Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible strategy plays out:

    You start with 0 cookies, but producing 2 cookies per second.
    After 250 seconds, you will have C=500 cookies and can buy a farm that produces F=4 cookies per second.
    After buying the farm, you have 0 cookies, and your total cookie production is 6 cookies per second.
    The next farm will cost 500 cookies, which you can buy after about 83.3333333 seconds.
    After buying your second farm, you have 0 cookies, and your total cookie production is 10 cookies per second.
    Another farm will cost 500 cookies, while you can buy after 50 seconds.
    After buying your third farm, you have 0 cookies, and your total cookie production is 14 cookies per second.
    Another farm would cost 500 cookies, but it actually makes sense not to buy it: instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.

Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds.

Notice that you get cookies continuously: so 0.1 seconds after the game starts you'll have 0.2 cookies, and π seconds after the game starts you'll have 2π cookies.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of seconds it takes before you can have X delicious cookies.

We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10-6. See the FAQ for an explanation of what that means, and what formats of real numbers we accept. 
"""

def main():
	fin=open('B-large.in')
	fout=open('B-large.out','w')
	T=int(fin.readline())
	for i in range(T):
		#cfx is the line from input with c, f and x
		cfx=fin.readline()
		#splits cfx into a list by default string which is " "
		cfx_list=cfx.split()
		#C is first element, F is second, X is third
		#C is cost of farm, F is cps boost from farm, X is goal cookie count
		C=float(cfx_list[0])
		F=float(cfx_list[1])
		X=float(cfx_list[2])
		print (C,F,X)
		#N is number of farms
		N=0
		time_passed=0
		solved=0
		while solved==0:
			#cps is cookies per second
			cps=F*N+2
			#next_farm is time until next farm
			next_farm=C/cps
			#rem is remaining time until win if left
			rem=X/cps
			#either the remaining time until X is less than the time 
			#required to build a farm or it isn't
			if (rem<=next_farm):
				mintime=time_passed+rem
				solved=1
			else:
				#if it isn't then is the time remaining to build the 
				#next farm and then wait for X (farmplan) less 
				#than the time remaining until X (waitplan)
				farmplan=next_farm+X/(F*(N+1)+2)
				waitplan=rem
				if(waitplan<=farmplan):
					mintime=time_passed+waitplan
					solved=1
				else:
					N=N+1
					time_passed=time_passed+next_farm
		mintime=round(mintime,7)			
		fout.write("Case #"+str(i+1)+": "+str(mintime)+"\n")
	return 0

if __name__ == '__main__':
	main()


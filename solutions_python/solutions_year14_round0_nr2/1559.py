'''
# cookie clicker solver..
# base production: 2 cookies/s
# farm cost:       C cookies
# farm production: F cookies/s
# target:          X cookies

speed * time = total cookies
speed1 * time - farm cost + speed2 * time2 - farm cost + ... = total cookies

X / base

buy farms as soon as possible

say I make speed(farms*F+2) cookies and have C cookies, should I buy another farm or wait?
another farm:
	time = X/(speed+F)
no additional farm:
	time = (X-C)/(speed)
	
total time(X, 4) = C/(base) + C/(base+F) + C/(base+2*F) + C/(base+3*F) + X/(base+4*F)
total time(X, 3) = C/(base) + C/(base+F) + C/(base+2*F) + X/(base+3*F)

total time(X, i) = C/(base) + C/(base+F) + C/(base+2*F).. + C/(base+(i-1)*F) + X/(base+i*F)
total time(X, i+1) = C/(base) + C/(base+F) + C/(base+2*F).. + C/(base+i*F) + X/(base+(i+1)*F)

diff:
i:   X/(base+i*F)
i+1: C/(base+i*F) + X/(base+(i+1)*F)

C/(base+i*F) + X/(base+(i+1)*F) - X/(base+i*F) == 0
-> 
C*(base+i*F+F) + X*(base+i*F) - X*(base+i*F+F) == 0
->
C*(base+i*F+F) - X*F == 0
->
i = (X*F-C*(base+F))/(C*F) = X/C - (base+F)/F = X/C - base/F - 1

'''
import sys
from math import floor, ceil

time_to_farm = [0]
def calc(C, F, X, farms):
	global time_to_farm
	time_to_farm = [0]
	while len(time_to_farm) <= farms:
		speed = 2 + (len(time_to_farm)-1)*F
		time_to_farm.append(time_to_farm[-1] + C/speed)
	#print farms, len(time_to_farm), time_to_farm
	return time_to_farm[farms] + X/(2+F*farms)
def best_farm_num(C, F, X):
	return X/C - 2/F - 1
def get_best_time(C, F, X):
	farms = best_farm_num(C, F, X)
	farms = max(0, farms)
	less = calc(C, F, X, int(floor(farms)))
	more = calc(C, F, X, int(ceil(farms)))
	if less < more:
		return less
	return more

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		C, F, X = map(float, raw_input().split())
		msg = get_best_time(C, F, X)
		print 'Case #%d: %s' % (i+1, msg)

if __name__ == '__main__':
	main()
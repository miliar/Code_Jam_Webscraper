import sys
import os
import math


#------------------------------
# debug
en_debug = 1
en_debug = 0

def debug(*s):
    if( en_debug):
        print(*s)
#------------------------------




#------------------------------
# main
#------------------------------

#get input from file if file exists
file_name='d.txt'
file_name='A-small-attempt0.in'
file_name='A-large.in'
if os.path.exists(file_name) :
    fp = open(file_name,"r")
    if fp:
        sys.stdin = fp

#start working
N = int(sys.stdin.readline().strip())
debug ( 'case num = ',N )

for qw in range(1, N+1):

	wire_num = int(sys.stdin.readline().strip())

	wire_list=[]
	for i in range(wire_num):
		temp = sys.stdin.readline().strip().split(' ')
		#debug( 'temp  =',temp )
		for k in range(len(temp)):
			temp[k] = int(temp[k])
		wire_list.append(temp)
	debug( wire_list,'   wire_list')

	cross=0
	while(len(wire_list)>0):
		pp = wire_list.pop()
		debug('pp=',pp)
		for i in range( len(wire_list) ):
			if (pp[0]-wire_list[i][0])*(pp[1]-wire_list[i][1]) < 0 :
				debug('find a cross')
				cross+=1

	print( 'Case #%d:' % qw,cross )

#ending
sys.stdin=sys.__stdin__
#a=input("pausing...")

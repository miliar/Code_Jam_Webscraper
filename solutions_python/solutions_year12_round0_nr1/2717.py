#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kirodh
#
# Created:     14/04/2012
# Copyright:   (c) kirodh 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


infile = open('A-small-attempt2.in', 'r')
outfile = open('A small output.in','w')
n = 0
m=0


for line in infile:

##    if line.isdigit()==True:
##        #n= n*0
##        m= int(line)
    if n!=0 :
        #if n!=(m+1):
        print('Case #', n,': ', sep='',end='',file= outfile)
        #else:

##    if line=='':
##        print('',file= outfile)


    for char in line:
        if char.isdigit()==True:
            n= n*0
            m= int(char)
        elif char=='':
            print('',file= outfile)
            n=n*0

        if char == 'a':
            print('y',end='',file = outfile )
        elif char=='b':
            print('h',end='',file = outfile)
        elif char=='c':
            print('e',end='',file = outfile)
        elif char=='d':
            print('s',end='',file = outfile)
        elif char=='e':
            print('o',end='',file = outfile)
        elif char=='f':
            print('c',end='',file = outfile)
        elif char=='g':
            print('v',end='',file = outfile)
        elif char=='h':
            print('x',end='',file = outfile)
        elif char=='i':
            print('d',end='',file = outfile)
        elif char=='j':
            print('u',end='',file = outfile)
        elif char=='k':
            print('i',end='',file = outfile)
        elif char=='l':
            print('g',end='',file = outfile)
        elif char=='m':
            print('l',end='',file = outfile)
        elif char=='n':
            print('b',end='',file = outfile)
        elif char=='o':
            print('k',end='',file = outfile)
        elif char=='p':
            print('r',end='',file = outfile)
        elif char=='q':
            print('z',end='',file = outfile)
        elif char=='r':
            print('t',end='',file = outfile)
        elif char=='s':
            print('n',end='',file = outfile)
        elif char=='t':
            print('w',end='',file = outfile)
        elif char=='u':
            print('j',end='',file = outfile)
        elif char=='v':
            print('p',end='',file = outfile)
        elif char=='w':
            print('f',end='',file = outfile)
        elif char=='x':
            print('m',end='',file = outfile)
        elif char=='y':
            print('a',end='',file = outfile)
        elif char=='z':
            print('q',end='',file = outfile)
        elif char==' ':
            print(' ',end='',file = outfile)
    if n!=0 :
        print(end='\n',file= outfile)
    #if m!=n:
    n=n +1


infile.close()
outfile.close()

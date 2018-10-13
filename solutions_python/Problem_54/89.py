#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
from fractions import gcd
import operator

__author__="Shahar"
__date__ ="$08-May-2010 08:25:20$"

def Warnning(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    C = int(fin.readline())
    for iC in range(C):
        numbers = fin.readline().rstrip('\n').split(' ')
        N = int(numbers[0])
        T = map(int, numbers[1:N+1])
        #print str(N) + ' ' + str(T)
        dT = map(operator.sub, T[:-1], T[1:])
        dT = map(abs, dT)
        #print str(dT)
        N = reduce(gcd, dT)
        #print str(gcdT)
        #K = [N - (Ti % N) for Ti in T]
        #print str(K)
        k = (N - (T[0] % N)) % N
        text = 'Case #' + str(iC+1) + ': ' + str(k)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #Warnning(sys.argv[1]);
    #Warnning('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\B-test.in');
    #Warnning('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\B-small-attempt1.in');
    Warnning('C:\\Users\\Shahar\\Projects\\Misc\\LearnPython2\\GCJ2010Qual\\test\\B-large.in');

import math

CM = {0:'R',1:'O',2:'Y',3:'G',4:'B',5:'V'}
CMr = dict([(v,k) for k,v in CM.items()])
NM = dict([ (i,[ _ for _ in range(6) if not (abs(i-_)<2 or abs(_+6-i)<2 or abs(_-6-i)<2)]) for i in range(6)])

import sys

Colors = ["R", "O", "Y", "G", "B", "V"]

def Solver(N, Cur):
    l = []
    for i in range(N):
        mm = 0
        for j in range(6):
            if(l == [] or j != l[-1]) and (Cur[j] > mm or (l !=[] and Cur[j] == mm and mm >0 and j == l[0])):
                mm = Cur[j]
                c = j
        if mm == 0:
            return "IMPOSSIBLE"
        l += [c]
        Cur[c] -= 1
    if l[-1] == l[-2] or l[-1] == l[0]:
        return "IMPOSSIBLE"
    else:
        return "".join([Colors[c] for c in l])

def main():

    #print CMr

    with open(sys.argv[1]) as f:
        n = int(f.readline())

        for i in xrange(n):

            N, R, O, Y, G, B, V = map(int,f.readline().strip().split())
            r = Solver(N,[R,O,Y,G,B,V])

            print "Case #{:d}: ".format(i+1),r
main()

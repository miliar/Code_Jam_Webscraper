__author__ = 'miguel'
from numpy import *
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    tmp_row=zeros(4)
    for i in range(N):
        choose1= int(sys.stdin.readline())
        k=0
        while k<4:
            rowt=sys.stdin.readline()
            if k<choose1:
                row=rowt
            k+=1


        int_row=map(int,row.split())


        choose2= int(sys.stdin.readline())
        k=0
        while k<4:
            rowt=sys.stdin.readline()
            if k<choose2:
                row=rowt
            k+=1
        int_row2= map(int,row.split())

        resp=None
        exit=False
        for j in range(4):
            if int_row[j] in int_row2:
                if resp is None:
                    resp = int_row[j]
                else:
                    print "Case #"+str(i+1)+": "+"Bad magician!"
                    exit=True
                    break
        if exit:
            continue
        if resp is None:
            print "Case #"+str(i+1)+": "+"Volunteer cheated!"
        else:
            print "Case #"+str(i+1)+": "+str(resp)
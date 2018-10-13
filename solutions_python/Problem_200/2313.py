#Tidy Numbers

import sys
import math

sys.stdin = open('tidy.in', 'r')
sys.stdout = open('tidy.out','w')

def find_tidy_num(upper):
    upper = str(upper)
    reference = int(upper)
    upper = [int(k) for k in upper]
    tidy = False
    while not tidy:
        tidy = True
        for k in range(len(upper)-1):
            if upper[k] > upper[k+1]:
                tidy = False
                upper[k] -= 1
                upper[k+1] = 9
                break
    
    out = ''.join([str(k) for k in upper])
    out.strip('0')
    upper = [int(k) for k in out]
    for k in range(len(upper)-1,-1,-1):
        largest = False
        while not largest:
            if upper[k] != 9:
                upper[k] += 1
                if not check(upper,reference):
                    upper[k] -= 1
                    largest = True
            else:
                largest = True
    out = ''.join([str(k) for k in upper])
    return int(out)
    
def check(al,number):
    al_int = ''.join([str(k) for k in al])
    al_int = int(al_int)
    return al_int <= number

T = int(input())

for i in range(T):
    num = int(input())
    print "Case #%d: %d" % (i+1,find_tidy_num(num))

'''
Created on 2017. 4. 8.

@author: Hyeonsu
'''
import math 

def isValid(num_str):
    #print(num_str)
    if len(num_str)==1: 
        return True
    
    for i in range(1, len(num_str)):
        if int(num_str[i-1])>int(num_str[i]):
            return False
    return True    
            
def tinyNumbers(n):
    amt = 1
    while True:
        num_str = str(n)
        t = int(math.log10(amt))
        if num_str[len(num_str)-t-1] == '9':
            amt *= 10
        if isValid( num_str ):
            return str(n)
        n -= amt
    
if __name__ == '__main__':
    f = open("D:/B-large.in", 'r')
    n = int(f.readline())
    for i in range(int(n)):
        print_str="Case #"+str(i+1)+": "
        line = f.readline()
        print_str += tinyNumbers(int(line))
        print(print_str)
    f.close()
    pass
from sys import stdin
from unittest import result
from math import fmod, sqrt

def pall(i):
    result = True
    a = str(i)
    for i in range(len(a)):
        if not a[i] == a[len(a)-1-i]:
            result = False
            break
    
    return result

def cuad(i):
    return fmod(sqrt(i),1) == 0 

def main():
    n_cases = int(stdin.readline()) 

    for i_case in range(1, n_cases+1):
        a, b = stdin.readline().split(' ')
        
        result = 0
        for i in range(int(a),int(b)+1):
            if pall(i):
                s = sqrt(i)
                if fmod(s,1) == 0 and pall(int(s)):
                    result+=1
        
        
        print 'Case #'+str(i_case)+': '+ str(result)
        

if __name__ == '__main__':
    main()
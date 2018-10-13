'''
Created on Feb 22, 2017

@author: cturkarslan
'''
###REDIRECT IO
import sys
sys.stdin = open('B-large.in' ,'r')

#sys.stdin = open('Input.in' ,'r')
sys.stdout = open('output.txt' , 'w')


T = int(input())
for t in range(T):
    N = str(input())
    answer = N
    for i,c in enumerate(N[:-1]):
            if(N[i]>N[i+1]):
                j = i
                while(j>-1 and N[j] == c): j -= 1
#                print(j,i,N)
                if(j == -1):
                    if(c == "1"): answer =(i)*"9" #Number is  aaaaaa...ccc
                    else:
                        if(i == 0): answer = str(int(c)-1)
                        else: answer = str(int(c)-1) + i*"9"
                else:
                    answer =N[0:j+1]
                    answer += str(int(c)-1) + (i- j-1) * "9" 
#                    answer +=(i-j)*str(int(c)-1)
                answer +=(len(N)-i-1)*"9"
                break
                             
    print ("Case #%d:" %(t+1),answer)

if __name__ == '__main__':
    pass



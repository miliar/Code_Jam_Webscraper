'''
Created on Feb 22, 2017

@author: cturkarslan
'''
###REDIRECT IO
import sys
import operator
sys.stdin = open('B-small-attempt1.in' ,'r')

#sys.stdin = open('Input.in' ,'r')
sys.stdout = open('output.txt' , 'w')


T = int(input())
for t in range(T):
    N,R,O,Y,G,B,V = map(int,input().split())
    colors = {}
    colors["R"] = R
    colors["O"] = O
    colors["Y"] = Y
    colors["G"] = G
    colors["B"] = B
    colors["V"] = V
    answer = ["0"] *N
#    print(N)
#    print (colors)
    if(R > N/2 or Y > N/2 or B > N/2): 
        answer_string = "IMPOSSIBLE"
    else: 
        last_char = 0
        char1 = max(colors.items(), key=operator.itemgetter(1))
        del colors[char1[0]]
        char2 = max(colors.items(), key=operator.itemgetter(1))
        del colors[char2[0]]
        char3 = max(colors.items(), key=operator.itemgetter(1))
        del colors[char3[0]]
        answer_string = "".join([char1[0],char2[0],char3[0]]) * (char2[1]+char3[1]-char1[1]) + "".join([char1[0],char2[0]]) * (char1[1]-char3[1]) + "".join([char1[0],char3[0]]) * (char1[1]-char2[1])  
#             if( "0" in answer[last_char:]):operator
#                 i = answer[last_char:].index("0")
#                 for n in range(i,N,2):
#                     if(colors[char] == 0):
#                         last_char = n
#                         break
#                     answer[n] = char
#                     colors[char] -= 1
#                 else:
#                     last_char = 0
#   print (colors)
#    print ("Case #%d:" %(t+1),len(answer_string),answer_string)
    print ("Case #%d:" %(t+1),answer_string)

if __name__ == '__main__':
    pass



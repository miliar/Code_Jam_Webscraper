'''
Created on Apr 12, 2013

@author: Colin Lee
'''
import sys

def win(r,c,d):
    m=0
    for x in r:
        if x.count('X') + x.count('T')==4:return 'X won'
        if x.count('O') + x.count('T')==4:return 'O won' 
        m+=x.count('.')
    for x in c:
        if x.count('X') + x.count('T')==4:return 'X won'
        if x.count('O') + x.count('T')==4:return 'O won'
        m+=x.count('.')
    for x in d:
        if x.count('X') + x.count('T')==4:return 'X won'
        if x.count('O') + x.count('T')==4:return 'O won'
        m+=x.count('.')
    if m==0:return 'Draw'
    else: return 'Game has not completed'
    
sys.stdin=open('A-large.in')
sys.stdout=open('A-large.out','w')
for _ in range(int(input())):
    r=[]
    c=[]
    d=[]
    for i in range(4):
        r.append(input())
    c=list(map(list,zip(*r)))
    d=[[r[0][0],r[1][1],r[2][2],r[3][3]],[r[3][0],r[2][1],r[1][2],r[0][3]]]
    print('Case #'+str(_+1)+': '+win(r,c,d))
    input()
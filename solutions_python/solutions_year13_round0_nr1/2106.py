import math
import string
f=open('D:/codejam/A-large.in')
bl=f.readlines()
f.close()
n=bl[0]
k=int(n)*5
i=1
pyes=0
f=open('D:/codejam/out_A_large.txt','w')
while i <= k :
    won='D'
    if((bl[i][0] == 'X' or bl[i][0] == 'T') and (bl[i+1][1] == 'X' or bl[i+1][1] == 'T') and (bl[i+2][2] == 'X' or bl[i+2][2] == 'T') and (bl[i+3][3] == 'X' or bl[i+3][3] == 'T')) :
        won='X'
        f.write('Case #'+ str(int(i/5)+1) + ': '+ won + ' won\n')
        i=i+5
        continue
    if((bl[i][0] == 'O' or bl[i][0] == 'T') and (bl[i+1][1] == 'O' or bl[i+1][1] == 'T') and (bl[i+2][2] == 'O' or bl[i+2][2] == 'T') and (bl[i+3][3] == 'O' or bl[i+3][3] == 'T')) :
        won='O'
        f.write('Case #'+ str(int(i/5)+1) + ': '+ won + ' won\n')
        i=i+5
        continue
    if((bl[i][3] == 'X' or bl[i][3] == 'T') and (bl[i+1][2] == 'X' or bl[i+1][2] == 'T') and (bl[i+2][1] == 'X' or bl[i+2][1] == 'T') and (bl[i+3][0] == 'X' or bl[i+3][0] == 'T')) :
        won='X'
        f.write('Case #'+ str(int(i/5)+1) + ': '+ won + ' won\n')
        i=i+5
        continue
    if((bl[i][3] == 'O' or bl[i][3] == 'T') and (bl[i+1][2] == 'O' or bl[i+1][2] == 'T') and (bl[i+2][1] == 'O' or bl[i+2][1] == 'T') and (bl[i+3][0] == 'O' or bl[i+3][0] == 'T')) :
        won='O'
        f.write('Case #'+ str(int(i/5)+1) + ': '+ won + ' won\n')
        i=i+5
        continue
    for j in range(0,4) :
        if((bl[i+j][0] == 'X' or bl[i+j][0] == 'T') and (bl[i+j][1] == 'X' or bl[i+j][1] == 'T') and (bl[i+j][2] == 'X' or bl[i+j][2] == 'T') and (bl[i+j][3] == 'X' or bl[i+j][3] == 'T')) :
            won='X'
            break
        if((bl[i+0][j] == 'X' or bl[i+0][j] == 'T') and (bl[i+1][j] == 'X' or bl[i+1][j] == 'T') and (bl[i+2][j] == 'X' or bl[i+2][j] == 'T') and (bl[i+3][j] == 'X' or bl[i+3][j] == 'T')) :
            won='X'
            break
        if((bl[i+j][0] == 'O' or bl[i+j][0] == 'T') and (bl[i+j][1] == 'O' or bl[i+j][1] == 'T') and (bl[i+j][2] == 'O' or bl[i+j][2] == 'T') and (bl[i+j][3] == 'O' or bl[i+j][3] == 'T')) :
            won='O'
            break
        if((bl[i+0][j] == 'O' or bl[i+0][j] == 'T') and (bl[i+1][j] == 'O' or bl[i+1][j] == 'T') and (bl[i+2][j] == 'O' or bl[i+2][j] == 'T') and (bl[i+3][j] == 'O' or bl[i+3][j] == 'T')) :
            won='O'
            break
    if(won=='X' or won=='O'):
        f.write('Case #'+ str(int(i/5)+1) + ': '+ won + ' won\n')
        i=i+5
        continue
    for p in range(0,4):
        if(bl[i+p].count('.')>0):
            f.write('Case #'+ str(int(i/5)+1) + ': '+'Game has not completed\n')
            i=i+5
            won='I'
            break
    if(won=='D'):
        f.write('Case #'+ str(int(i/5)+1) + ': '+'Draw\n')
        i=i+5
 
f.close()

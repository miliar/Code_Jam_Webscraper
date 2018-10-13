n=int(raw_input())
win=[['T', 'X', 'X', 'X'],
     ['X', 'X', 'X', 'X'],
     ['O', 'O', 'O', 'T'],
     ['O', 'O', 'O', 'O']]
def solve(lis,i):
    dots=0
    for row in lis:
        temp=sorted(row)
        dots+=temp.count('.')
        if temp in win and temp[1]=="X":
            return "Case #{0}: X won".format(i+1)
        elif temp in win and temp[1]=="O":
            return "Case #{0}: O won".format(i+1)
    for col in zip(*lis):
        temp=sorted(col)
        if temp in win and temp[1]=="X":
            return "Case #{0}: X won".format(i+1)
        elif temp in win and temp[1]=="O":
            return "Case #{0}: O won".format(i+1)
    diag1=[lis[j][j] for j in xrange(4)]
    diag1.sort()
    if diag1 in win and diag1[1]=="X":
        return "Case #{0}: X won".format(i+1)
    elif diag1 in win and diag1[1]=="O":
        return "Case #{0}: O won".format(i+1)
    diag2=[lis[3][0],lis[2][1],lis[1][2],lis[0][3]]
    diag2.sort()
    if diag2 in win and diag2[1]=="X":
        return "Case #{0}: X won".format(i+1)
    elif diag2 in win and diag2[1]=="O":
        return "Case #{0}: O won".format(i+1)
    #print dots
    if dots==0:
        return "Case #{0}: Draw".format(i+1)
    else:
        return "Case #{0}: Game has not completed".format(i+1)
    
for i in xrange(n):
    lis=[list(raw_input()) for _ in xrange(4)]
    print solve(lis,i)
    if i!=  n-1:raw_input()        
        
            
            
        

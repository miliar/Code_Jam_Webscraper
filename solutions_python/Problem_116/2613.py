'''
Created on Apr 14, 2012

@author: lucamaf
'''


def print_out(res):
    if res==1:
        return "X won"
    elif res==-1:
        return "O won"
    elif res==0:
        return "Draw"
    else:
        return "Game has not completed"

def comp_out(total):
    res=0
    if total==4*10 or total==3*10+1:
        res=1
        #X
    elif total==4*0 or total==3*0+1:
        res=-1
        #O
    elif total<0:
        res=2
        #incomplete
    else:
        res=0
        #draw
    return res

def comp_list(board):
    result=0
    t=True
    while t:
        #compute horizontal
        for i in range(4):
            tmp=comp_out(sum(board[i]))
            if tmp==1 or tmp==-1: 
                result=tmp
                t=False
                return result
            else:
                result+=tmp   
        #compute vertical
        for i in range(4):
            z=0
            for j in range(4):
                z+=board[j][i]
            tmp=comp_out(z)
            if tmp==1 or tmp==-1: 
                result=tmp
                t=False
                return result
            else:
                result+=tmp
        #compute diagonal1
        tmp=comp_out(sum(board[i][i] for i in range(4)))
        if tmp==1 or tmp==-1: 
            result=tmp
            t=False
            return result
        else:
            result+=tmp
        #compute diagonal2
        tmp=comp_out(sum(board[i][3-i] for i in range(4)))
        if tmp==1 or tmp==-1: 
            result=tmp
            t=False
            return result
        else:
            result+=tmp
        t=False
    #print result
    return result

def results(afile):
    f=open(afile)
    T=int(f.next())
    for i in range(T):
        m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for j in range(4):
            line=f.next()
            l=0
            for k in line:
                if k=='X':
                    m[j][l]=10
                elif k=='O':
                    m[j][l]=0
                elif k=='T':
                    m[j][l]=1
                elif k=='.':
                    m[j][l]=-100
                l+=1
        f.next()
        #print m    
        res=comp_list(m)
        print 'Case #{case}: {s}'.format(case=i+1,s=print_out(res))

results('a-large-p1.txt')
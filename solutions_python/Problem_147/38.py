# Encoding: utf-8
'''
Created on 26.04.2014

@author: Los

@version: 0.0.1
'''
import sys
from math import hypot, sqrt, ceil

def input_int():
    return int(input())

def input_float():
    return float(input())

def input_str():
    return input().strip()

def input_list_int():
    return list(map(int, tuple(input().split())))

def input_list_float():
    return list(map(float, tuple(input().split())))

def main(argv=None):
    if argv is None:
        argv=sys.argv

    import locale
    locale.setlocale(locale.LC_ALL, '')
    
    CASE_NUM=input_int()
    
    for case_num in range(CASE_NUM):
        N,M,K = map(int, tuple(input().split()))
        
        field=list()
        for x in range(N):
            field.append(list())
            for y in range(M):
                field[x].append(0)
        #print (field)
        
        ksq=ceil(sqrt(K))
        
        if ksq%2==0:
            centX=(N-1)/2
            centY=(M-1)/2
        else:
            centX=int(N/2)
            centY=int(M/2)


        
        lDist=list()
        for x in range(N):
            for y in range(M):
                lDist.append((x,y,abs(x-centX)+abs(y-centY)))
        lDist.sort(key=lambda x: x[2])
        #print(lDist)
        
        for i in range(K):
            #print (i)
            d=lDist[0][2]
            for j in range(len(lDist)):
                if lDist[j][2]>d :
                    break
            if j==0:
                subl=list(lDist)
            else:
                subl=lDist[:j]
            flag=False
            for item in subl:
                x, y= item[0], item[1]
                dx, dy=(centX-x), (centY-y)
                if dx<0 and y!=0 and y!=M-1:
                    if field[x-1][y-1]+field[x-1][y+1]+field[x-1][y] == 3:
                        break
                elif dx>0 and y!=0 and y!=M-1:
                    if field[x+1][y-1]+field[x+1][y+1]+field[x+1][y] == 3:
                        break
                if dy<0 and  x!=0 and x!=N-1:
                    if field[x-1][y-1]+field[x+1][y-1]+field[x][y-1] == 3:
                        break
                elif dy>0 and  x!=0 and x!=N-1:
                    if field[x-1][y+1]+field[x+1][y+1]+field[x][y+1] == 3:
                        break
            
            x,y=item[0],item[1]
            #print(lDist)
            #print(subl, j)
            #print (item)
            lDist.remove(item)
            field[x][y]=1
        #print(field)      
        
        count=0
        for x in range(N):
            for y in range(M):
                if field[x][y]==1:
                    if (x!=0) and (y!=0) and (x!=N-1) and (y!=M-1) :
                        if field[x-1][y]>0 and field[x+1][y]>0 and field[x][y-1]>0 and field[x][y+1]>0:
                            count+=1
                            field[x][y]=2
        #print(field)
        
        #print (N,M,K)
        #for x in range(N):
        #    for y in range(M):
        #        print(field[x][y], end='')
        #    print()
        #print('----------------------')
        
        print('Case #{0}: {1}'.format(case_num+1, K-count))
        


if __name__ == '__main__':
    main()

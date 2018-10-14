from string import lowercase as lc
import sys
import pdb

infile=open(sys.argv[1])
# infile=open('B-sample.in')

def child(i,j):
    """Returns the coordinates of the child of i,j
    """
    global Map, W, H
    l=Map[i][j];d='';t=0; ans=None
    if i!=0 and Map[i-1][j]<l:  # NORTH
        l=Map[i-1][j]
        ans=i-1,j
        d='N'
    if j!=0 and Map[i][j-1]<l:  # WEST
        l=Map[i][j-1]
        ans=i,j-1
        d='W'
    if j!=W-1 and Map[i][j+1]<l:  # EAST
        l=Map[i][j+1]
        ans=i,j+1
        d='E'
    if i!=H-1 and Map[i+1][j]<l:  # SOUTH
        l=Map[i+1][j]
        ans=i+1,j
        d='S'
        
    return ans

def dfs(i,j):
    """Performs a dfs over the map from position i,j
    """
    global Basin, label
    
    if Basin[i][j]:
        # pdb.set_trace()
        return Basin[i][j]
    
    n=child(i,j)
    if n:
        Basin[i][j]=dfs(n[0],n[1])
        return Basin[i][j]
    else:
        Basin[i][j]=lc[label]
        label+=1
        return Basin[i][j]

def labeler():
    """Calls dfs on empty cells of the Basin until it's all labeled
    """
    global W, H
    for h in range(H):
        for w in range(W):
            dfs(h,w)


if __name__ == '__main__':
    T=int(infile.readline())
    for t in range(T):          # each map
        H,W=[int(x) for x in infile.readline().split()]
        Basin=[['' for w in range(W)] for h in range(H)]
        Map=[]
        label=0
        for i in range(H):     # read the map
            row=[int(x) for x in infile.readline().split()]
            Map.append(row)
        
        labeler()
        print 'Case #%s:' % (t+1)

        for h in range(H):
            print ' '.join(Basin[h])

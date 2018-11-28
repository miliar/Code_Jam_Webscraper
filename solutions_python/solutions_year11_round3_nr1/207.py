import copy

def is2by2(p,x,y):
    return p[x][y]=='#' and p[x+1][y]=='#' and p[x][y+1]=='#' and p[x+1][y+1]=='#'
def replaceN(p,x,y):
    p[x][y]='/'
    p[x+1][y]='\\'
    p[x][y+1]='\\'
    p[x+1][y+1]='/'
def containshash(p):
    for x in p:
        for y in x:
            if y=='#':
                return True
    return False

def get_red_picture(p):
    pnew=copy.deepcopy(p)
    for x in range(len(pnew)-1):
        for y in range(len(pnew[x])-1):
            if(is2by2(pnew,x,y)):
                replaceN(pnew,x,y)
    if (pnew==p and containshash(p)) or containshash(pnew):
        return []
    else:
        return pnew
        

T = int(raw_input())
for tc in range(T):
    R,C = [int(x) for x in raw_input().split()]
    picture=[]
    for x in range(R):
        row=raw_input()
        picture+=[list(row)]

    replacedpicture = get_red_picture(picture)
    print "Case #%d: "%(tc+1)
    if(replacedpicture!=[]):
        for x in replacedpicture:
            st=''
            for y in x:
                st+=y
            print st
    else:
        print "Impossible"
    

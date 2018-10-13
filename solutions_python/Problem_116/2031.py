

def count(l,m):
    counter=0
    for i in l:
        if i==m :
            counter=counter+1
    return counter






def solve(l):
    check="X"
    # horizontal solve
    for i in l :
        if ( count(i,check)==4 or (count(i,check)==3 and count(i,"T")==1) ) :
            return check+" won"
    t=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(4):
        for i in range(4):
            t[j][i]=l[i][j]
    print t
    # transposed and checking for vertical
    for i in t :
        if ( count(i,check)==4 or (count(i,check)==3 and count(i,"T")==1) ) :
            return check+" won"
   # diagonal 1
    tmp1=[l[0][0],l[1][1],l[2][2],l[3][3]]
    if ( count(tmp1,check)==4 or (count(tmp1,check)==3 and count(tmp1,"T")==1) ) :
        return check+" won"
    # diagonal 2
    tmp2=[l[0][3],l[1][2],l[2][1],l[3][0]]
    if ( count(tmp2,check)==4 or (count(tmp2,check)==3 and count(tmp2,"T")==1) ) :
        return check+" won"


    check="O"
    # horizontal solve
    for i in l :
        if ( count(i,check)==4 or (count(i,check)==3 and count(i,"T")==1) ) :
            return check+" won"
    t=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(4):
        for i in range(4):
            t[j][i]=l[i][j]
    print t
    # transposed and checking for vertical
    for i in t :
        if ( count(i,check)==4 or (count(i,check)==3 and count(i,"T")==1) ) :
            return check+" won"
    # diagonal 1
    tmp1=[l[0][0],l[1][1],l[2][2],l[3][3]]
    if ( count(tmp1,check)==4 or (count(tmp1,check)==3 and count(tmp1,"T")==1) ) :
        return check+" won"
    # diagonal 2
    tmp2=[l[0][3],l[1][2],l[2][1],l[3][0]]
    if ( count(tmp2,check)==4 or (count(tmp2,check)==3 and count(tmp2,"T")==1) ) :
        return check+" won"


    
    

    for i in l:
         for j in i:
             if j=="." :
                return "Game has not completed"
            
    return "Draw"
    

    

f=open("answers_tic.txt","w")

t=int(raw_input())
for i in range(t) :
    
    tmp=[]
    x=raw_input();    tmp.append([x[0],x[1],x[2],x[3]])
    x=raw_input();    tmp.append([x[0],x[1],x[2],x[3]])
    x=raw_input();    tmp.append([x[0],x[1],x[2],x[3]])
    x=raw_input();    tmp.append([x[0],x[1],x[2],x[3]])
    
    #print "Case #"+str(i+1)+": "+solve(tmp)
    f.write("Case #"+str(i+1)+": "+solve(tmp)+"\n")

    if  i != t-1 :
        raw_input() #line between test cases

    


f.close()
    

            
        
    

import re

def solveB(R,Y,B):
    N=R+Y+B
    if R>N/2 or Y>N/2 or B>N/2:
        return 'IMPOSSIBLE'
    col=sorted([R,Y,B],reverse=True)
    res=""
    for i in xrange(col[2]):
        res+="123"
    col[0]-=col[2]
    col[1]-=col[2]
    col[2]=0
    for i in xrange(col[1]):
        res+="12"
    col[0]-=col[1]
    col[1]=0
    while col[0]:
        for i in xrange(len(res)-1):
            if int(res[i])>1 and int(res[i+1])>1:
                res=res[:i+1]+"1"+res[i+1:]
                col[0]-=1
                break
            
    res=list(res)
    if max([R,Y,B])==R:
        for i in xrange(len(res)):
            if res[i]=="1":
                res[i]="R"
        if min([R,Y,B])==B:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="B"
                if res[i]=="2":
                    res[i]="Y"
        else:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="Y"
                if res[i]=="2":
                    res[i]="B"
    elif max([R,Y,B])==Y:
        for i in xrange(len(res)):
            if res[i]=="1":
                res[i]="Y"      
        if min([R,Y,B])==B:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="B"
                if res[i]=="2":
                    res[i]="R"
        else:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="R"
                if res[i]=="2":
                    res[i]="B"      
    else:
        for i in xrange(len(res)):
            if res[i]=="1":
                res[i]="B"        
        if min([R,Y,B])==R:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="R"
                if res[i]=="2":
                    res[i]="Y"
        else:
            for i in xrange(len(res)):
                if res[i]=="3":
                    res[i]="Y"
                if res[i]=="2":
                    res[i]="R"        
    return "".join(res)
    
out=open("out.txt","w")
with open("B-small-attempt0.in") as file: #A-large.in
    T=int(file.readline())
    #print T
    for case in range(T):
        s=file.readline().rstrip()
        N, R, O, Y, G, B, V=map(int,s.split())
        
        ans=solveB(R,Y,B)
        print ans    
        #print "--------------"    
        out.write("Case #"+str(case+1)+": "+str(ans)+"\n")

out.close()
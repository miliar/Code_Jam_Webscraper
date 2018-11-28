def genWord(T,Letter):
    if sum(T)==0:
        return ""
    i = T.index(max(T))
    if T[i] >sum(T)-T[i]:
        l =min(T[i],2*T[i]-sum(T)+1)
        w=Letter[i]*(l)
        T[i]-=l
        print("notDead")
    else:
        w=Letter[i]
        T[i]-=1
    while (sum(T)>0):
        #print(w)
        #print(T)
        #print(i)
        ma=max([T[j] for j in range(3) if j!= i])
        Mini = [j for j in range(3) if (j!=i) and T[j]==ma]
        i= min(Mini)        
        w=w+Letter[i]
        T[i]-=1
    if (len(w)>1) and w[0]==w[len(w)-1]:
        w=w[:len(w)-2]+w[len(w)-1]+w[len(w)-2]
    return w

filename  = "B-small-attempt0.in" #"B-large.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [N,R,O,Y,G,B,V]=[int(j) for j in f.readline().split()]
    m= [max(R-Y-B,0),max(Y-R-B,0),max(B-Y-R,0)]
    w = genWord([R,Y,B],"RYB")
    if w[0]==w[1]:
        ret="IMPOSSIBLE"
    else:
        ret =w
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")

f.close()
out.close()
print(genWord([1,8,10],"ABC"))

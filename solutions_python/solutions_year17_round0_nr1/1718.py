def flip(ss):
    if ss=="+":
        return "-"
    else:
        return "+"

def main():
    t = int(raw_input())
    for it in range(1, t + 1):
        ans=0
        
        inp = raw_input().split()
        st = inp[0]
        k = int(inp[1])
        st=list(st)
        
        for i in range(0,len(st)-k+1):
            if st[i]=='-':
               # print "Found at "+str(i)
                ans+=1
               # print("Inverting " + str(i) +" to "+ str(i+k-1)+ "includsicve")
                for j in range(i,i+k):
                    
                    st[j]=flip(st[j])
               # print "Now array is: "
                #print st
                
       # print("Final arr")
       # print st
        for i in range(0,len(st)):
            if st[i] == "-":
                ans="IMPOSSIBLE"
                break
                   
        
        print("Case #{}: {}".format(it, ans))
        



main()
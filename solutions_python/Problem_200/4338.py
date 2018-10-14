
def dodude(mn,i):
    if i==0 :
        if mn[i]!=0:
            return 2
        return 5
    if ans[i]<ans[i-1]:
        ans[i]=9
        mn[i-1]=mn[i-1]-1
        if i-1==0 and mn[i-1]!=0:
            return 9;
    return dodude(mn,i-1)
tests=int(raw_input())
for duder in range(tests):
    t=(raw_input())
    m=list(t);
    ans=[];
    last=-1;
    for i in m:
        num=int(i)
        if len(ans)==0 or num>=ans[last]:
            ans.append(num)
            last+=1
        else:
            ans.append(num);
            last+=1;
            klu=dodude(ans,last)
            if klu==5:
                jl=len(m);
                ans=[]
                for md in range(jl-1):
                    ans.append('9')
                break;
            elif klu==9:
                ner=ans[0];
                ans=[];
                jl=len(m);
                ans.append(ner);
                for md in range(jl-1):
                    ans.append('9')
                break;
    prince=[]
    for i in ans:
        prince.append(str(i))
    nand=''.join(prince)
    print "Case #"+str(duder+1)+": "+nand
        

# encoding: utf-8

txtin="B-small-attempt3.in"
# txtin="in.txt"
fout="out.txt"

with open(txtin,'r') as f:
    # lst = list(map(int,f.readline()))
    t=int(f.readline())
    
    with open(fout, 'w') as fout:
        for k in range(t):
            num=int(f.readline())
            decompo=[]
            while num!=0:
                small=num%10
                decompo.append(small)
                num=(num-small)//10
            decompo=[i for i in reversed(decompo)]
#             print(decompo)
            make=[]
            for ind,_ in enumerate(decompo):
                if ind+1<len(decompo) and decompo[ind]>decompo[ind+1]:
                    #violation!
                    break
            ind+=1
#             print(ind)
            j=ind-1
            i=j
            while i>=0 and decompo[i]==decompo[j]:
                i-=1
            i=min(i+1,j)
#             print(i,j)
            for counter in reversed(range(ind,len(decompo))):
#                     print(counter)
                decompo[counter-1]-=1
                decompo[counter]=9
            if i!=j and ind!=len(decompo):
                for counter in reversed(range(max(i,1),len(decompo))):
    #                     print(counter)
                    decompo[counter-1]-=1
                    decompo[counter]=9
            fout.write('Case #'+str(k+1)+': ')
            while decompo[0]==0:
                decompo.remove(0)
#             print(decompo)
            for dig in decompo:
                fout.write(str(dig))
            fout.write('\n')
            
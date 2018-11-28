run=int(input())
count=[]
for i in range(run):
    first=input().strip().split()
    nshy=int(first[0])
    shy=list(first[1])
    shy=list(map(int,shy))
    ppl=0
    frnds=0
    c=[]
    d=""

    for j in range (nshy+1):
        if ppl < j:
            frnds+=(j-ppl)
            ppl+=j-ppl
        
        ppl=ppl+shy[j]
    d="Case #"+str(i+1)+": " + str(frnds)
    count.append(d)
for i in range (len(count)):
    print(count[i])
    
    





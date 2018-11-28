num_cases = int(raw_input())
result=[]
for casenum in range(1, num_cases+1):
    word,n= [z for z in raw_input().split()]
    n=int(n)
    l=len(word)
    total=0
    print n,l,word
    flag=0
    limit=-1
    for i in range(l):
        count=0
        print("*******at i :"+str(i))
        if not(word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u'):
            for j in range(i,l):
                if not(word[j]=='a' or word[j]=='e' or word[j]=='i' or word[j]=='o' or word[j]=='u'):
                    count+=1
                else:
                    break
                if count==n:
                    total+=l-n-i
                    x=i-1
                    while x>limit:
                        total+=l-i-n+1
                        x-=1
                    print("at "+word[j])
                    total+=1
                    print i,count,limit,total
                    limit=i
                    
                    break
    result.append(total)
                    

for x in range(1,len(result)+1):
    print "Case #%d: %d" % (x, result[x-1])

def pancakeFlipper(S,K):
    plus = 0
    minus = 0
    count = 0
    for i in range(len(S)):
        if S[i]=='+':
            plus+=1
        else:
            minus+=1
    

    S = list(S)
    for i in range(len(S)-K+1):
        if S[i]=='-':
            for j in range(i,i+K):
                if S[j]=='-':
                    S[j]='+'
                else:
                    S[j]='-'
            count+=1
    "".join(S)
    for i in range(len(S)):
        if S[i]=='-':
            return 'IMPOSSIBLE'
    return count
fname = "A-large.in"
with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content] 
f = open('Output.txt','w')
T = int(content[0])
for i in range(1,T+1):
	(S,K) = content[i].split(" ")
	K = int(K)
	res = pancakeFlipper(S,K)
	print("Case #{}:".format(i),res,file=f)
f.close()
    

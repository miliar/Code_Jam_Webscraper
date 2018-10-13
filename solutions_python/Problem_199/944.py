
def solve(S, K,numOps):
    # print "solving ",S,K,numOps
    if len(S) < K:
        print len(S),K
        for j in xrange(len(S)):
            if S[j]=='-':
                return "IMPOSSIBLE"
        return numOps

    if S[0]=='+':
        return solve(S[1:], K, numOps)

    S2=list(S)
    for j in xrange(K):
        # print "working on",S2[j],j,S2[j]=='-',S2[j]=='+'
        if S2[j]=='-':
            S2[j]='+'
        elif S2[j]=='+':
            S2[j]='-'

    return solve("".join(S2),K, numOps+1)


filename ='A-small-attempt0.in'
with open(filename) as f:
    content = f.readlines()

content =[x.strip() for x in content]
T=content[0]
out = []
for i in xrange(len(content)-1):
    print i,content[i+1]
    S,K = content[i+1].split(" ")
    out.append("Case #%d: %s" % (i+1, solve(S,int(K),0)))

solution = "\n".join(out)
print solution

with open("Output.txt", "w") as text_file:
    text_file.write(solution)


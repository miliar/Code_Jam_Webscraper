
def tidy(n):
    s=str(n)
    for i in reversed(xrange(len(s)-1)):
        # print "checking index",i,":",s[i],">",s[i+1]
        if s[i]>s[i+1]:
            return False

    return True



def solveIter(N):

    while True:
        # print "solving for",N
        if tidy(N):
            return N

        s = str(N)
        # remove digit from rtl
        for i in xrange(len(s)-1):
            remove = N%pow(10,i)+1
            N=N-remove
            if tidy(N):
                return N



filename ='B-large.in'
with open(filename) as f:
    content = f.readlines()

content =[x.strip() for x in content]
T=content[0]
out = []
for i in xrange(len(content)-1):
    # print i,content[i+1]
    N = int(content[i+1])
    res = solveIter(N)
    out.append("Case #%d: %s" % (i+1, res))
    print "Sol for",N,"is",res

solution = "\n".join(out)
# print solution

with open("Output2b.txt", "w") as text_file:
    text_file.write(solution)


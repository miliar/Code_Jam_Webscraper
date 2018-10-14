import math
def ispalindrome(n):
    if n/10 is 0:
        return True
    l=[]
    x=n
    while x>0:
        l.append(x%10)
        x=x/10
    leng=len(l)
    i=0
    while i<leng:
        if l[i]!=l[leng-i-1]:
            return False
        i+=1
    return True

#print ispalindrome(123)

file = open("C-small-attempt1.in")
l=[]
while 1:
	line=file.readline() 
	if not line:
		break
	l.append(line)

num=int(l[0])
#print num
i=1
outs=[]
while i<=num:
    inp=str(l[i]).split()
    #print inp
    j=int(inp[0])
    end=int(inp[1])
    #print j
    #print end
    count=0
    while j<=end:
        if ispalindrome(j):
            sqr=math.sqrt(j)
            if sqr==int(sqr):
                if ispalindrome(int(sqr)):
                    count+=1
        j+=1
    outs.append(count)
    i+=1
i=0
while i<len(outs):
    print "Case #"+str(i+1)+": "+str(outs[i])
    i+=1

N=int(raw_input())
def isPalindrome(num):
    num=str(num)
    rev=num[::-1]
    if num==rev:return True
    return False
f=open('out.txt','r+')
for i in xrange(N):
    print "Time "+str(i+1)
    A,B=map(int, raw_input().split())
    s_A=int(A**0.5)
    s_B=int(B**0.5)
    count=0
    for j in xrange(s_A,s_B+1):
        if isPalindrome(j):
            temp=j**2
            if temp <=B and temp>=A and isPalindrome(temp):
                count+=1
                print j**2
    f.write("Case #"+str(i+1)+": "+str(count)+'\n')



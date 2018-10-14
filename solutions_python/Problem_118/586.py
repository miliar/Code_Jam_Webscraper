import math

def gen():
    i = 1
    while i<=(10**7):
        if isPalindrome(i):
            if isPalindrome(i**2):
                valid.add(i**2)
                print i**2
        i+=1
    #print valid
    #out.write("Case #"+str(testnum)+": "+str(ans)+'\n')

def find(testnum,a,b):
    ans = 0
    for num in valid:
        if num>=a and num<=b:
            ans+=1
            #print num
    #print "Case #"+str(testnum)+": "+str(ans)
    out.write("Case #"+str(testnum)+": "+str(ans)+'\n')

def isPalindrome(num):
    string = str(num)
    return string==string[::-1]

tests = int(raw_input())
i = 0
valid = set([])
out = open('output.txt','w')
gen()
while i<tests:
    i+=1
    a,b=raw_input().strip().split()
    find(i,int(a),int(b))
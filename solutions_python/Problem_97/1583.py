import sys
t = input()
def digits(num):
    temp = num
    n=0
    while num!=0:
        rem = num%10
        n+=1
        num/=10
    return n
def gen(num):
    dig = digits(num)
    temp = num
    for i in xrange(dig-1):
        rem = temp%10
        
        temp=temp/10
        
        temp=rem*(10**(dig-1))+temp
        yield temp
def find(nums,a,b):
    for i in nums:
        if (i[0] == a and i[1] == b) or (i[0] == b and i[1] == a):
            return True
    return False
def savecompare(nums,a,b):
    for i in xrange(a,b+1):
        gens = gen(i)
        for j in gens:
            if not find(nums,i,j) and i>=a and i<=b and j>=a and j<=b and i != j:
                #print i,j
                nums.append([i,j])
    

for i in xrange(t):
    nums = []
    line = raw_input().split()
    a,b = int(line[0]),int(line[1])
    savecompare(nums,a,b)
    #print nums
    sys.stdout.write("Case #"+str(i+1)+": "+str(len(nums)))
    print

import math;
f = open("C-small-attempt1.in", "r+")
def palindrome(num):
    string=str(num)
    k=len(string)-1
    length_string_mid=int(k/2)
    for i in range(0,length_string_mid+1):
        if string[i]==string[k-i]:
            continue
        else:
            return False
    return True
def fands(range_values):
    count=0
    for i in range(range_values[0],range_values[1]):
        b=palindrome(i)
        if b:
            c = palindrome(i*i)
            if c:
                count=count+1
    return count;

i=f.readline()
t=int(i)
testcases=t+1
while t>0:
    i=f.readline()
    range_values=i.split(" ")
    temp=math.sqrt(int(range_values[1]))-int(math.ceil(math.sqrt(int(range_values[1]))))
    for i in range(0,2):
        range_values[i]=int(math.ceil(math.sqrt(int(range_values[i]))))
    if temp==0:
        range_values[1]=range_values[1]+1
    count=fands(range_values)
    print "Case #"+str(testcases-t)+": "+str(count)
    t=t-1

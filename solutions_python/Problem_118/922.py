import math
import itertools

def game():
    f = open("C-large-1.in", "r")
    output = open("C-large-1.out", "w")
    first = f.readline()
    T = int(first)
    case = 1

    while case < T+1:
        line = f.readline().split(" ")
        beg, end = int(line[0]), int(line[1])
        res = "Case #" + str(case) + ": " + str(listed(beg, end))
        #print res
        output.write(res+"\n")
        case = case+1

def getDecimal(num):
    count = 0
    while num>0:
        num = num/10
        count+=1
    return count

def count(beg, end):
    #print beg, end
    count = 0
    temp_end = getDecimal(end) 
    if (beg<=9 and end >=9):
        #print 3, 9
        count=1
    d = dict()
    
    list_possibility = itertools.product('012', repeat=temp_end)
    for possibility in list_possibility:
        i = int("".join(possibility))
        #print "i", i
        a = i*i
        if(a >= beg and a <=end and a not in d):
            if (isPalindrome1(i)):
                if(isPalindrome1(a)):
                    #print i, a
                    d[a]=i
                    count += 1
    print d
    return count

def listed(beg, end):
    d = {1: 1, 1212225222121L: 1101011, 400080004: 20002, 1024348434201L: 1012101, 4004009004004L: 2001002,
         121242121: 11011, 1004006004001L: 1002001, 40000800004L: 200002, 44944: 212, 1234321: 1111, 10201: 101,
         4: 2, 12102420121L: 110011, 12321: 111, 404090404: 20102, 123454321: 11111, 14641: 121, 12345654321L: 111111,
         121: 11, 10000200001L: 100001, 4008004: 2002, 4000008000004L: 2000002, 100020001: 10001, 1022325232201L: 1011101,
         1214428244121L: 1102011, 1234567654321L: 1111111, 1210024200121L: 1100011, 102030201: 10101, 484: 22, 1232346432321L: 1110111,
         40804: 202, 1020304030201L: 1010101, 1002001: 1001, 1000002000001L: 1000001, 10221412201L: 101101, 104060401: 10201,
         125686521: 11211, 1002003002001L: 1001001}
    d[9]=3
    count = 0
    for i in d:
        if i>=beg and i<=end:
            count += 1
    return count
        


def isPalindrome1(num):  
    n=str(num)
    i=0
    while i < int(len(n)/2):
        if n[i]!=n[-i-1]:
            return 0  
        i += 1 
    return 1

game()

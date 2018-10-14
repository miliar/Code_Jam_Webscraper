from bisect import *

li = []
MAX = 10**100

def IsPalindrome(x):
    return x == x[::-1]
    
def Check(x):
    return IsPalindrome(x) and IsPalindrome(str(int(x)**2))
    
def CheckAdd(x):
    global li
    #if not Check(x):
        #print x
    #assert Check(x)
    if Check(x) and int(x)**2 <= MAX:
        assert(int(x)**2 not in li)
        #if int(x) not in li:
        li += [int(x)**2]

def MakeSingles():
    CheckAdd("1")
    CheckAdd("2")
    CheckAdd("3")

def MakeTwos():
    for l in range(2, 105):
        if l % 2 == 0:
            # Even length
            CheckAdd("2" + "0"*(l-2) + "2")
        else:
            # Odd length
            CheckAdd("2" + "0"*((l/2)-1) + "0" + "0"*((l/2)-1) + "2")
            CheckAdd("2" + "0"*((l/2)-1) + "1" + "0"*((l/2)-1) + "2")
        
def GetBinaryStrings(length, maxOnes):
    bits = ['0' for i in range(length + 1)]
    bits[0] = '1'
    popCount = 1
    
    results = []
    while bits[length] == '0':
        results += [str(int("".join(bits[:-1])))]
        addPosition = 0
        if popCount == maxOnes:
            while bits[addPosition] == '0':
                addPosition += 1
        for i in range(addPosition, length + 1):
            if bits[i] == '0':
                bits[i] = '1'
                popCount += 1
                break
            else:
                bits[i] = '0'
                popCount -= 1
        
    return results
    
def MakeTwoCenters():
    Twos50 = GetBinaryStrings(51, 2)
    
    for t in Twos50:
        x = "%s2%s" % (t, t[::-1])
        CheckAdd(str(int(x)))
        
def MakeBinarys():
    Fours50 = GetBinaryStrings(51, 4)
    
    for t in Fours50:
        x = "%s%s" % (t, t[::-1])
        CheckAdd(str(int(x)))
    
    for t in Fours50:
        x = "%s0%s" % (t, t[::-1])
        CheckAdd(str(int(x)))

    for t in Fours50:
        x = "%s1%s" % (t, t[::-1])
        CheckAdd(str(int(x)))

MakeSingles()
MakeTwos()
MakeTwoCenters()
MakeBinarys()
li.sort()
#print "\n".join(map(lambda x: str(int(x**0.5)), li))

T = 10000
T = int(raw_input())

for t in range(1, T + 1):
    A, B = 10**100, 10**100 
    A, B = map(int, raw_input().split())
    ans = 0
    for p in li:
        if A <= p and p <= B:
            ans += 1
        if p > B:
            break
    
    print "Case #%d: %d" % (t, ans)
    #print "Case #%d: %d %d %d" % (t, A, B, bisect_right(li, B) - bisect(li, A))
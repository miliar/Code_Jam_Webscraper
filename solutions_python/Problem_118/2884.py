'''
Created on Apr 13, 2013

@author: Kenneth
'''
import math
def isPalindrome(i):
    if i != math.floor(i):
        return False
    st = str(int(i))
    print type(st)
    print st
    l = len(st)
    for j in xrange(0, (l/2)):
        if st[j] != st[int(math.floor(l-1-j))]:
            return False
    return True
def solve(min,max):
    count = 0
    for i in xrange(min,max+1):
        if(isPalindrome(i) and isPalindrome(math.sqrt(i))):
            count = count+1
    return count

if __name__ == '__main__':
    output = open ("C:\\jam\\fair\\out.txt",'w')
    inp = open ("C:\\jam\\fair\\C-small-attempt0.in",'r')
    num = int(inp.readline())
    for i in xrange(1,num+1):
        print i
        size = inp.readline().split(' ')
        l = int(size[0])
        w = int(size[1])
        res = solve(l,w)
        output.write("Case #%d: %d" %(i,res ))
        output.write("\n")
    output.close()
    inp.close()
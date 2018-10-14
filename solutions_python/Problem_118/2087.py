from math import sqrt

def isPalindrome(x):
    return str(x)==str(x)[::-1]

def main():
    t = int(raw_input())
    for j in range(t):
        a,b = [int(i) for i in raw_input().split()]
        #i = a
        count = 0
        for i in range(a,b+1):
            #if i*i > b: break
            sq=sqrt(i)
            if int(sq) == sq and isPalindrome(int(sq)) and isPalindrome(i):
                #print i
                count += 1
            #i += 1
        print "Case #%d: %d" %(j+1,count)

if __name__=="__main__": main()

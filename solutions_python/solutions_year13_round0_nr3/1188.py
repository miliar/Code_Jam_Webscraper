from math import *
def probC():
    f=open('input.txt','r')
    new=open('answer.txt','w')
    for tc in xrange(1, int(f.readline())+1):
        # Get input
        line=f.readline()
        array=line.split(" ")
        start=int(array[0])
        end=int(array[1])
        count=0
        for i in xrange(int(ceil(sqrt(start))),int(floor(sqrt(end)))+1):
            if palindrome(i) and palindrome(i*i):
                count+=1
        new.write('Case #%d: %d' % (tc,count)+"\n")


def palindrome(number):
    text=str(number)
    for i in xrange(0,len(text)/2):
        if text[i]!=text[len(text)-i-1]:
            return False
    return True
        

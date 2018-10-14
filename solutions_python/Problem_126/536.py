import sys
import os

if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        word, n = sys.stdin.readline().strip().split()
        n = int(n)

        #print word, n

        le = len(word)

        endoflast = 0
        beginnext = 0
        total = 0
        xlast = 0
        for x in xrange(le-n+1):
            found = True
            for xx in xrange(n):
                if word[x+xx] in ['a', 'e', 'i', 'o', 'u']:
                    found = False
                    break
            # all consonants
            if found:                
                #print 'found'
                #print word[x]
                #print x
                endofthis = x+n-1
                #print 'endofthis', endofthis
                after_this = le - endofthis - 1
                #print 'after', after_this
                                
                before_this = x - beginnext + 1
                #print 'before', before_this
                beginnext = x+1                

                mixmode = (before_this-1) * after_this

                tot = after_this + before_this + mixmode
                #print 'mixmode', mixmode
                #print 'tot', tot
                total += tot
                #print tot
            
        
        sys.stdout.write('Case #{0}: {1}\n'.format(i+1, total))
        
            
                



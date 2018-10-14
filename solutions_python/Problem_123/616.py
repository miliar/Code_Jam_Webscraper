
def calcans(startsize, motes, ans):
#    print "####init ", startsize, motes, ans
    if len(motes)==0:
#        print 'return'
        return ans
    elif startsize == 1:
        return len(motes)
    elif motes[0] < startsize:
#        print 'ate mtoa. startsize and mote', startsize, motes
        return calcans(startsize+motes[0], motes[1:], ans)
    else:
        numifremove = len(motes)
#        print '## going in lastcase'
        newans = calcans(startsize*2-1, motes, ans)
#        print 'to remove and newans:', numifremove, newans
        return ans + min(newans+1, numifremove)




times = input()
for time in range(times):
    a = [int(i) for i in raw_input().split()]
    startsize = a[0]
    motes = [int(i) for i in raw_input().split()]
    motes.sort()
    ans = 0
    print 'Case #%d: %d'%( time+1, calcans(startsize, motes, ans))
    


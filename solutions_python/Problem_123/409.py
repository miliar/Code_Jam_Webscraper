import math

MAX_MOTE_SIZE = 100

def checkifsolveable(ms,motes):
    if ms > motes[len(motes)-1]:
        return True

    if ms <= motes[0]:
        return False
    
    for i in motes:
        if ms > i:
            ms += i
        else:
            return False
        
    return True

def amount_of_motes_to_eat(ms,i):
    num = 0
    while ms <= i:
        ms += (ms-1)
        num += 1
    return (num, ms)

# Return minimum number of steps needed
def solvetestcase(ms, motes):
#    print "ITERATING"
    if (checkifsolveable(ms,motes) == True):
        return 0
    
    for i in motes:
#        print "Motes: " + str(motes)
#        print "Iterating over " + str(i)
        if ms > i:
            ms += i
#            print "New motes: " + str(motes)
        else:
            break

    # Remove all motes smaller than the big one we bumped into
    stop = False
    while (stop != True):
        for j in motes:
            if j < i:
                motes.remove(j)
                break
            else:
                stop = True
                
        
    # Now we reached a point where we can't eat a mote
    # Do we want to increase ours by n-1 or remove the rest of the motes?
    # First of all, if we need to increase so much that our actions will
    # end up adding more motes than what is left, we should just remove
    # the rest
#    print "I ran into a big mote, im " + str(ms) + " and it is " + str(i)
    aomte = amount_of_motes_to_eat(ms,i)
#    print "ill need " + str(aomte[0]) + "steps to eat it"
    if (aomte[0] >= len(motes)):
#        print "Returning len of motes as it is hard for " + str(ms) + "to eat " + str(i)
#        print "BTW motes is: " +str(motes)
        return len(motes)

    ms = aomte[1]
#    print "Proceeding with new motesize: " + str(ms)
    # Now we don't know whether we will have to add 4 new motes in order
    # to be able to eat the next 5, and then the next mote will trip us up
    # and have us add 4 more motes, for example, then we get 8 actions instead
    # of 5. So we have to just test it or something and backtrack    
    therest = solvetestcase(ms,motes[:])

#    print "This is how much ill need to solve the rset of the q: " + str(therest)
#    print "This is how much ill need to eat next mote: " + str(aomte[0])
     #aomte[0] is how many moves we needed to eat the next mote
     #therest is how many moves we needed to solve the rest of the question
    if (aomte[0] + therest > len(motes)):
#        print "len of motes is easier to remove: " + str(len(motes))
        return len(motes)

#    print "sum is easier to remove"
    return aomte[0] + therest
    
def parseinput(fd):
    motesize = fd.readline()
    motesize = int(motesize.split()[0])
#    print "motesize: " + str(motesize)
    motes = fd.readline().split()
#    print "motes read: " + str(motes)
    for i in range(len(motes)):
        motes[i] = int(motes[i])
    motes.sort()

#    print "READ MOTES: " + str(motes)
    # special case
    if motesize == 1:
        return len(motes)
    else:
        return solvetestcase(motesize,motes)
    
def solve(filename):
    fd = open(filename, "r+t")
    output= open("output.txt", "w+t")
    testcases = int(fd.readline())
#    print "testcases: " + str(testcases)
    for x in range(testcases):
        num_of_actions = parseinput(fd)
#        print "ANSWER: " + str(num_of_actions)
        output.write("Case #"+str(x+1)+": " + str(num_of_actions) + "\n")        
        
    fd.close()
    output.close()
    
##### main ####

solve("apoop.in")

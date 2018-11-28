def is_tidy(n):
    #print n
    if len(n) == 1:
        return True

    for i in xrange(1,len(n)):
        if (int(n[i]) < int(n[i-1])):
            return False

    return True

#Import the data
tests = []
T = int(raw_input())
for i in xrange(1,T+1):
    tests.append((raw_input()))

# Loop over each data row
case = 1
for n in tests:
    for i in xrange(int(n),-1,-1):
        if is_tidy(list(str(i))):
            print "Case #"+str(case)+": "+str(i)
            #print "n: "+str(case)+" tidy found: "+str(i)
            break
    case += 1

__author__ = 'Giannis'

f = open("A-small-attempt0.in", 'r')

for t in range(int(f.readline())):
    [m , audience] = f.readline().split()
    clappers = 0
    friends = 0
    for i in range(int(m)+1):
        #print clappers, i, friends
        if clappers >= i:
            clappers += int(audience[i])
        elif int(audience[i]) != 0:
            #print "S", i - clappers, i
            friends += i - clappers
            clappers += friends + int(audience[i])
            #print "E", clappers, i, friends
        #print "CL %s: %s" % (str(clappers), str(friends))
    print "Case #%s: %s" % (str(t+1), str(friends))
    #break
        

f.close()

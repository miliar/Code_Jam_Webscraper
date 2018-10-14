def flipCounter(string, k):
    string = list(string)
    counter = 0
    i=0
    while i < len(string):
        if string[i] == "-":
            for j in range(k):
                try:
                    if string[i+j] == "+":
                        string[i+j] = "-"
                    else:
                        string[i+j] = "+"
                except:
                    counter = "IMPOSSIBLE"
                    return counter
            counter += 1

        i += 1
    
    return counter



T = int(raw_input())

for i in xrange(1, T+1):
    string, k = raw_input().split()
    k =  int(k)
    print "Case #{}: {}".format(i, str(flipCounter(string, k)))

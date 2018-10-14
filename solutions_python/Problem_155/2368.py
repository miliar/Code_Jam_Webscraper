
def min_friends(s_max, s_counts):
    #print s_max, s_counts
    total = 0
    result = 0
    for i in range(0,s_max+1):
        #print "\ti: " + str(i)
        if s_counts[i] != 0:
            #print "\t\tscounts: " + str(s_counts[i])
            if total < i:
                #print "\t\t\ttotal < i, i - total: " + str(i - total)
                # Need more people
                toadd = i - total
                total += toadd
                result += toadd
                #print "\t\t\tresult: " + str(result)
            total += s_counts[i]
    return result

t = int(raw_input())
for i in range(t):
    line = raw_input().split()
    s_max = int(line[0])
    s_counts = [int(c) for c in line[1]]

    result = min_friends(s_max, s_counts)

    print "Case #" + str(i+1) + ": " + str(result)

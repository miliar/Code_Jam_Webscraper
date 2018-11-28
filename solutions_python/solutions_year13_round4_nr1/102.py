infile = open("A-small-attempt1.in", "rU")
outfile = open("A-small-attempt1.out", "w")

case = 1
linenum = 0
get_details = True
stops = 0
pairs = 0
pairs_done = 0

pairs_list = []

def T(n):
    return (n*(n+1))/2

for line in infile:
    if linenum != 0:
        if get_details:
            line = line.strip().split(" ")
            stops = int(line[0])
            npairs = int(line[1])
            pairs = 0
            pairs_done = 0
            pairs_list = []
            get_details = False

        else:
            line = line.strip().split(" ")

            for i in xrange(3):
                line[i] = int(line[i])

            for l in xrange(line[2]):    
                pairs_list.append((line[0], line[1]))

            pairs_done += 1
            pairs += line[2]

            if pairs_done == npairs:
                # k stations trip: k(n+1) - k(k+1)/2
                # T(a+b) - T(a) - T(b) is difference in cost for swapping
                total = 0

                if pairs == 1:
                    outfile.write("Case #%d: 0\n" % case)
                    case += 1

                else:
                    pairs_list.sort()
                    shuffled = True

                    while shuffled:
                        shuffled = False
                        
                        for i in xrange(len(pairs_list)):
                            for j in xrange(i+1, len(pairs_list)):
                                pi = []
                                pj = []

                                if pairs_list[i][0] < pairs_list[j][0]:
                                    pi = pairs_list[i]
                                    pj = pairs_list[j]

                                else:
                                    pi = pairs_list[j]
                                    pj = pairs_list[i]

                                if pi[0] < pj[0] and pj[0] <= pi[1] and pi[1] < pj[1]:
                                    
                                    pi = pairs_list[i]
                                    pj = pairs_list[j]
                                    
                                    total += T(pj[1] - pi[0]) + T(pi[1] - pj[0]) - T(pi[1] - pi[0]) - T(pj[1] - pj[0])
                                    pairs_list[i] = (pi[0], pj[1])
                                    pairs_list[j] = (pj[0], pi[1])

                                    shuffled = True

                        for item in pairs_list:
                            if item[0] == item[1]:
                                pairs_list.remove(item)

                        if len(pairs_list) == 1:
                            shuffled = True
                            break
                    
                get_details = True
                print total
                outfile.write("Case #%d: %d\n" % (case, total))
                case += 1
    
    linenum += 1

outfile.close()

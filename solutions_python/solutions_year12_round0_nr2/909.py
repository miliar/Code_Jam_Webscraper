__author__ = 'diana_fisher'

# Dancing With the Googlers
# scores range from 0 to 10, inclusive
# surprising if a triplet contains two scores that are 2 apart
# 8,8,8 -> not surprising
# 6,7,8 -> surprising
# 7,6,9 -> will never happen
# total points = sum of three scores
# best result = maximum of three scores in the triplet

# given: total points and number of surprising triplets
# output: maximum number of Googlers that could have had a best result of at least p

# 6 Googlers:
# total points: 29, 20, 8, 18, 18, 21
# 2 surprising triplets
# how many Googlers could have gotten a best result of 8 or better?

def max_googlers(N, S, p, total_points):
#    print 'N', N  # number of Googlers
#    print 'S', S  # number of surprising triplets
#    print 'p', p  # best result of p or better
#    print 'total_points', total_points
    googler_count = 0
    surprise_count = 0
    for i in range(N):
#        print total_points[i]
        t = int(total_points[i])
        triplets = find_triplets(t)
        surprises = find_surprise_triplet(t)
#        print 'triplets:', triplets
#        print 'surprises:', surprises
        counted_googler_N = False
        for tr in triplets:
            if not counted_googler_N:
#                print 'tr', tr
                for score in tr:
                    if score >= p:
                        googler_count += 1
                        counted_googler_N = True
#                        print 'incrementing googler_count to',googler_count
                        break

#        print 'surprise_count=', surprise_count
        if surprise_count < S and not counted_googler_N:
            for s in surprises:
#                print 's', s
                for score in s:
                    if score >= p:
                        googler_count += 1
                        surprise_count += 1
#                        print 'incrementing googler_count to',googler_count
#                        print 'surprise_count googler_count to',surprise_count
                        break

    return googler_count

def find_triplets(total):
    result = []
    triplet = []
    a = total / 3
    triplet.append(a)
    
    remaining = total - a
    b = remaining / 2
    triplet.append(b)

    c = remaining - b
    triplet.append(c)
    result.append(triplet)

    return result

def find_surprise_triplet(total):
    surprises = []
    a = total / 3 - 1
    remaining = total - a
    b = remaining / 2
    c = remaining - b
#    print 'a=',a
#    print 'b=', b
#    print 'c=', c
    if a < 11 and b < 11 and c < 11:
        if a > -1 and b > -1 and c > -1:
            if abs(a-b) <= 2 and abs(a-c) <= 2 and abs(b-c) <=2:
                t = [a,b,c]
                surprises.append(t)

    a = total / 3
    remaining = total - a
    b = remaining / 2 - 1
    c = remaining - b
#    print 'a=',a
#    print 'b=', b
#    print 'c=', c
    if a < 11 and b < 11 and c < 11:
        if a > -1 and b > -1 and c > -1:
            if abs(a-b) <= 2 and abs(a-c) <= 2 and abs(b-c) <=2:
                t = [a,b,c]
                isDuplicate = False
                for item in surprises:
#                    print 'item:', item
                    if a in item and b in item and c in item:
                        isDuplicate = True
#                        print 'already have this triplet'

                if not isDuplicate:
                    surprises.append(t)
    return surprises

filename = "B-large.in"
file = open(filename, "r")
lines = []
for line in file:
    lines.append( line.strip() )

file.close()

numCases = int(lines[0])
for i in range(1, numCases+1):
#    print '----------------------------------------------------'
    case = "Case #" + str(i) + ":"
    line = lines[i]
    items = line.split()
#    print items
    N = int(items[0])
    S = int(items[1])
    p = int(items[2])
    points = items[3:]

    max = max_googlers(N, S, p, points)
    print case, max
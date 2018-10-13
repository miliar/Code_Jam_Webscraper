T = int(raw_input())

for i in xrange(0, T):
    #read line by line only
    #skip lines based on displacement
    guess = int(raw_input())
    for g in xrange(0, guess):
        row1 = raw_input().split()
        
    row1 = set(row1)
    
    #get second guess
    for g in xrange(0, 4-guess):
        raw_input()
    guess = int(raw_input())

    for g in xrange(0, guess):
        row2 = raw_input().split()
    row2 = set(row2)

    answer = row1.intersection(row2)
    l = len(answer)
    if l <= 0:
        print "Case #{}: Volunteer cheated!".format(i+1)
    elif l == 1:
        print "Case #{}: {}".format(i+1, list(answer)[0])
    elif l > 1:
        print "Case #{}: Bad magician!".format(i+1)

    #displace line again if not EOF yet
    for x in xrange(0, 4-guess):
        raw_input()

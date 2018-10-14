with open("A-small-attempt0.in") as f:
    for case in xrange(int(f.readline())):
        matches = 0
        row1 = int(f.readline()) # 1-4
        arrange1 = []
        for i in xrange(4):
            arrange1.append([int(c) for c in f.readline().replace("\n", "").split(" ")])
        possible_nums = arrange1[row1-1]
        row2 = int(f.readline()) # 1-4
        arrange2 = []
        for i in xrange(4):
            arrange2.append([int(c) for c in f.readline().replace("\n", "").split(" ")])
        for pos_num in possible_nums:
            if pos_num in arrange2[row2-1]:
                matches += 1
                match = pos_num


        if matches == 1:
            print "Case #%d: %s" % (case + 1, match)
        elif matches > 1:
            print "Case #%d: %s" % (case + 1, "Bad magician!")
        elif matches == 0:
            print "Case #%d: %s" % (case + 1, "Volunteer cheated!")


"""
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

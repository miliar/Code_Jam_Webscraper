inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %d"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    s_max, shies = rl().split()
    #print "s_max, shies", s_max, shies
    s_max = int(s_max)
    added_people = 0
    standing = 0
    for i in xrange(s_max+1):
        cur_shy = int(shies[i])
        #print "standing", standing, "added", added_people, "i", i, "cur_shy", cur_shy
        if i > standing:
            added_people += i - standing
            standing += i - standing
        standing += cur_shy
    print >>outputfile, out_s % (ncase,added_people)
        
    
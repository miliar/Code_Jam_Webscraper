T = int(raw_input().strip())        # grabs an integer from stdin

for case in range(1,T+1):
    rawline = raw_input().strip()
    line = rawline.split(' ')
    C = int(line[0])
    cc = line[1:1+C]
    D = int(line[1+C])
    dd = line[2+C:2+C+D]
    N = int(line[-2])
    inp = line[-1]

#    print ""
#    print "    " , rawline
#    print "    " , cc, dd, inp

    combines = {}
    for c in cc:
        combines[c[0:2]] = c[2]
        combines[c[1::-1]] = c[2]
    dd = set(dd)

    ans = ""

    for letter in inp:
        ans += letter
#        print "  + %s = %s" % (letter, ans), 
        if ans[-2:] in combines.keys():
#            bit = ans[-2:]
            ans = ans[:-2] + combines[ans[-2:]]
#            print ", %s -> %s" % (bit, combines[bit]),
        else:
#            print "    ",
            for l2 in ans[:-1]:
                if l2+letter in dd or letter+l2 in dd:
#                    print ", wipe!",
                    ans = ''
#            if ans != '': print "       ",
#        print "     got %s" % repr(ans)

    ans = "[" + ", ".join(ans) + "]"
    print "Case #%d: %s" % (case, ans)


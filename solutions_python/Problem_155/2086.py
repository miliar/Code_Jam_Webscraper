from sys import argv

# T = 4

# shy = ["4 11111",
#        "1 09",
#        "5 110011",
#        "0 1"]

ifile = open(argv[1], "rU")
ofile = open(argv[2], "w")

T = int(ifile.readline())

for case in xrange(1, T+1):

    # max_shy, aud = shy[case-1].split()

    max_shy, aud = ifile.readline().split()
    max_shy = int(max_shy)
    aud = [int(c) for c in aud]

    count = 0
    invite = 0
    for a in xrange(len(aud)):
        if count + invite < a and aud[a] > 0:
            invite += a - (count + invite)
        count += aud[a]

    if case < 5:
        print("Case #{}: {} for {}".format(case, invite, aud))
    ofile.write("Case #{}: {}\n".format(case, invite))

ofile.close()
ifile.close()

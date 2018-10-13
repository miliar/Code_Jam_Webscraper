import sys

f = open(sys.argv[1])

f.readline()

case = 0
while True:
    case += 1
    l = f.readline().strip().split()
    if not l:
        break
    audience = [int(x) for x in l[1]]
    friends = 0
    standing = 0
    for i, people in enumerate(audience):
        if standing < i:
            needed = i - standing
            friends += needed
            standing += needed
        standing += people
    print "Case #{}:".format(case), friends


inputfile = file("a-small.in", "rb")
outputfile = file("a-small.out", "wb")
out_yes = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]

def parse(s):
    l = []
    last_char = '~'
    current_count = 0
    for c in s:
        if c == last_char:
            current_count += 1
        else:
            l.append((last_char, current_count))
            current_count = 1
            last_char = c
    l.append((last_char, current_count))
    l.remove(('~', 0))
    return l

intdiff = lambda x,y: x - y if x > y else y - x
    
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    N = parse_line()[0]
    strings = [inputfile.readline().strip() for i in xrange(N)]
    fegla_won = False
    parsed = []
    for s in strings:
        parsed.append(parse(s))
    for p in parsed:
        if [a for a,b in p] != [a for a,b in parsed[0]]:
            fegla_won = True
            break
    if fegla_won:
        print >>outputfile, out_yes % (ncase, "Fegla Won")
        continue
    moves = 0
    for numchar in xrange(len(parsed[0])):
        s = 0
        for p in parsed:
            s += p[numchar][1] # Count
        avg = float(s) / N
        rounded_avg = int(round(avg))
        for p in parsed:
            moves += intdiff(p[numchar][1], rounded_avg)
    print >>outputfile, out_yes % (ncase, str(moves))
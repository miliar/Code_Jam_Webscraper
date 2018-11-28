#!/usr/bin/python

def charcount(s):
    pchar = ''
    count = 1
    retval = []
    for x in range(len(s)):
        if s[x] == pchar:
            count += 1
        else:
            if pchar != '':
                retval.append( (pchar, count) )
                count = 1
            pchar = s[x]
    retval.append( (pchar, count) )
    return retval


def solve_case(case):
    print(case)
    basestr = ''.join([x[0] for x in case[0]])

    # check for nonmatching
    for c in case:
        cstr = ''.join([x[0] for x in c])
        if basestr != cstr:
            return 'Fegla Won'

    # once matches confirmed, then check distances
    distances = []
    for a in range(len(case)):
        acount = [x[1] for x in case[a]]
        adist = []
        for b in range(len(case)):
            if a != b:
                bcount = [x[1] for x in case[b]]
                dist = 0
                for (n, m) in zip(acount, bcount):
                    dist += abs(n-m)
                adist.append(dist)
        distances.append(adist)
    # return lowest dist i think
    print(distances)

    currmin = -1
    for x in distances:
        csum = sum(x)
        if currmin == -1 or currmin > csum:
            currmin = csum
    return currmin

def main():
    inp = open('small.in')
    out = open('out.txt', 'w')
    lines = inp.readlines()
    cases = int(lines[0])
    lines = lines[1:]
    # read cases
    for casecount in range(cases):
        numstrings = int(lines[0])
        case = [charcount(x.strip()) for x in lines[1:numstrings+1]]
        output = 'Case #{0}: {1}'.format(casecount+1, solve_case(case))
        print(output)
        out.write(output + '\n')

        lines = lines[numstrings+1:]

if __name__=='__main__':
    main()

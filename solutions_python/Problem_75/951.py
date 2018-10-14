def invoke(line):
    split = line.split(' ')
    # build table of combinations
    combo_ct = int(split.pop(0))
    combinations = {}
    while combo_ct > 0:
        combo_ct = combo_ct - 1
        combo = split.pop(0)
        combinations[combo[0:2]] = combo[2]
        combinations[combo[1]+combo[0]] = combo[2]

    # build table of oppositions
    opp_ct = int(split.pop(0))
    oppositions = {}
    while opp_ct > 0:
        opp_ct = opp_ct - 1
        opp = split.pop(0)
        opp0 = opp[0]
        opp1 = opp[1]
        if opp[0] in oppositions:
            oppositions[opp0].append(opp1)
        else:
            oppositions[opp0] = [opp1]
        
        if opp1 in oppositions:
            oppositions[opp1].append(opp0)
        else:
            oppositions[opp1] = [opp0]

    split.pop(0)

    # loop through elements adding one at a time
    invokes = split.pop(0)
    invocations = ''
    for x in invokes:
#        print "invocations: %s" % invocations
        combined = False
        opposed = False
        # check combinations
        if invocations:
            last2 = invocations[-1] + x
            if last2 in combinations:
                invocations = invocations[:-1] + combinations[last2]
                combined = True
                continue
        # check opposes
        if x in oppositions and invocations:
            for opp in oppositions[x]:
                if opp in invocations:
                    opposed = True
                    invocations = ''
                    continue
        # or just add
        if not opposed and not combined:
            invocations = invocations + x

    return invocations

test1 = '1 QRI 0 4 RRQR'

def format_str(str):
    new_str = "["
    str_len = len(str)
    # not efficient.
    for x in range(0, str_len):
        new_str = new_str + str[x]
        if x < str_len-1:
            new_str = new_str + ", "
    new_str = new_str + "]"
    return new_str

def runcase(num, f):
    line = f.readline().strip()
    print "Case #%d: %s" % (num, format_str(invoke(line)))

f = open('B-large.in')

cases = int(f.readline())

for case in range(1, cases+1):
    runcase(case, f)

test_cases = input()

def print_result(t, result):
    print "Case #" + str(t+1) + ": " + result

def handle_case(t):
    N= raw_input()
    words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    #words = [, "THREE", "EIGHT",
    counts = {}
    m = {}
    for c in N:
        if c not in m:
            m[c] = 0
        m[c] += 1

    # Now see what possibilities we have
    # get the sixes and zeros out of the way
    # SIX
    if 'X' in m:
        counts[6] = m.get('X', 0)
        m['X'] = 0
        m['I'] -= counts[6]
        m['S'] -= counts[6]

    # ZERO
    if 'Z' in m:
        counts[0] = m['Z']
        m['Z'] = 0
        m['E'] -= counts[0]
        m['R'] -= counts[0]
        m['O'] -= counts[0]

    # TWO
    if 'W' in m:
        counts[2] = m['W']
        m['T'] -= counts[2]
        m['W'] -= counts[2]
        m['O'] -= counts[2]

    # FOUR
    if 'U' in m:
        counts[4] = m['U']
        m['F'] -= counts[4]
        m['O'] -= counts[4]
        m['U'] -= counts[4]
        m['R'] -= counts[4]

    # ONE
    if 'O' in m and m['O'] is not 0:
        counts[1] = m['O']
        m['O'] = 0
        m['N'] -= counts[1]
        m['E'] -= counts[1]

    # FIVE
    if 'F' in m and m['F'] is not 0:
        counts[5] = m['F']
        m['F'] = 0
        m['I'] -= counts[5]
        m['V'] -= counts[5]
        m['E'] -= counts[5]

    # SEVEN
    if 'V' in m and m['V'] is not 0:
        counts[7] = m['V']
        m['S'] -= counts[7]
        m['E'] -= counts[7]
        m['V'] -= counts[7]
        m['E'] -= counts[7]
        m['N'] -= counts[7]


    # NINE
    if 'N' in m and m['N'] is not 0:
        counts[9] = (int(m['N'] / 2))
        m['N'] -= counts[9]
        m['I'] -= counts[9]
        m['N'] -= counts[9]
        m['E'] -= counts[9]

    #EIGHT
    if 'I' in m and m['I'] is not 0:
        counts[8] = m['I']
        m['E'] -= counts[8]
        m['I'] -= counts[8]
        m['G'] -= counts[8]
        m['H'] -= counts[8]
        m['T'] -= counts[8]

    # THREE
    if 'T' in m and m['T'] is not 0:
        counts[3] = m['T']

    s = ''
    for key in sorted(counts):
        for i in xrange(0, counts[key]):
            s += str(key)
    print_result(t, s)

for t in range(0, test_cases):
    handle_case(t)



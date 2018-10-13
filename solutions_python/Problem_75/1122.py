def getInput():
    combinations = {}
    opposed = {}

    line = raw_input()
    sp = line.split()

    C = int(sp[0])
    D = int(sp[C + 1])
    # N = int(sp[C + D + 2]) not useful

    for x in range(1, C + 1):
        combinations[((sp[x][0], sp[x][1]))] = sp[x][2]
        combinations[((sp[x][1], sp[x][0]))] = sp[x][2]

    for x in range(C + 2, C + D + 2):
        opposed[sp[x][0]] = sp[x][1]
        opposed[sp[x][1]] = sp[x][0]

    strings = sp[len(sp) - 1]

    return combinations, opposed, strings

def compute(combinations, opposed, strings):
    l = []

    for c in strings:
        if len(l) == 0:
            l.append(c)
        elif (l[len(l) - 1], c) in combinations:
            l.append(combinations[(l[len(l) - 1], c)])
            l.pop(len(l) - 2)
        elif c in opposed and opposed[c] in l:
            l = []
        else:
            l.append(c)

    return l

def stringFormat(l):
    st = []

    if len(l) == 0:
        return "[]"

    st.append("[")
    st.append(l[0])

    for c in l[1:]:
        st.append(", ")
        st.append(c)

    st.append("]")

    return ''.join(st)

num = int(raw_input())

for x in range(num):
    combinations, opposed, strings = getInput()
    l = compute(combinations, opposed, strings)

    print "Case #" + str(x + 1) + ": " + stringFormat(l)

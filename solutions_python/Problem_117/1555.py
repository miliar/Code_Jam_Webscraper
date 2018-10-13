def possible_position(p_i, p_j, n, m, lawn):

    h = lawn[p_i][p_j]

    # i axis
    r = range(0, n)
    i_ok = True
    for i in r:
        if lawn[i][p_j] > h:
            i_ok = False
            break

    # j axis
    r = range(0, m)
    j_ok = True
    for j in r:
        if lawn[p_i][j] > h:
            j_ok = False
            break

    return (i_ok or j_ok)

def process_case(case, n, m, lawn):
    case_ok = True
    for i in range(0, n):
        for j in range (0, m):
            case_ok = possible_position(i, j, n, m, lawn)
            if (not case_ok):
                break
        if (not case_ok):
            break
    if (case_ok):
        print "Case #" + str(case) + ": YES"
    else:
        print "Case #" + str(case) + ": NO"

with open("B-small-attempt0.in") as f:
    content = f.readlines()

next = 1
for i in range(0, int(content[0].rstrip())):
    l = content[next].rstrip().split()
    n = int(l[0])
    m = int(l[1])
    lawn = []
    for j in range(0, n):
        lawn.append([])
        tokens = content[next+1+j].split()
        for k in range(0, m):
            lawn[j].append(tokens[k])
    process_case(i+1, n, m, lawn)
    next = next + n + 1
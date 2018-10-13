test_cases = int(raw_input())

def get_common(line1, line2):
    a = []
    b = []
    for i in line1.strip().split(' '):
        a.append(int(i.strip()))
    for i in line2.strip().split(' '):
        b.append(int(i.strip()))
    return list(set.intersection(set(a), set(b)))


for j in range(test_cases):
    first = int(raw_input())
    first_lines = []
    for i in range(4):
        first_lines.append(raw_input())
    second = int(raw_input())
    second_lines = []
    for i in range(4):
        second_lines.append(raw_input())
    a = get_common(first_lines[first-1], second_lines[second-1])
    if len(a) == 0:
        b = "Volunteer cheated!"
    elif len(a) > 1:
        b = "Bad magician!"
    else:
        b = str(a[0])

    print "Case #%d: %s" % (j+1, b)
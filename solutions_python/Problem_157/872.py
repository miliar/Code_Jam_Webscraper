def multiply(quat1, quat2):
    sign = 1
    if '-' in quat1:
        sign *= -1
        quat1 = quat1[1]
    if '-' in quat2:
        sign *= -1
        quat2 = quat2[1]
    stng = 'ijkij'
    out = ''
    if quat1 == '1':
        out = quat2
    elif quat2 == '1':
        out = quat1
    elif quat1 == quat2:
        sign *= -1
        out = '1'
    else:
        toMult = quat1 + quat2
        if toMult not in stng:
            out = stng[stng.index(quat2 + quat1) + 2]
            sign *= -1
        else:
            out = stng[stng.index(toMult) + 2]
    return '-'*(sign == -1) + out

def findIJK(stng, reps):
    if reps == 1:
        if stng == 'ijk':
            return True
        if len(stng) < 3:
            return False
        if len(stng) == 3 and reps == 1 and stng != 'ijk':
            return False
    
    first = stng[0]
    x = 0
    for r in range(1, len(stng) * reps):
        first = multiply(first, stng[r % len(stng)])
        if first == 'i':
            x = r + 1
            break
    else:
        return False
    
    first = stng[x % len(stng)]
    for r in range(x + 1, len(stng) * reps):
        first = multiply(first, stng[r % len(stng)])
        # print(stng[r % len(stng)])
        if first == 'j':
            x = r + 1
            break
    else:
        return False

    first = stng[x % len(stng)]
    for r in range(x + 1, len(stng) * reps):
        first = multiply(first, stng[r % len(stng)])
    if first == 'k':
        return True
    else:
        return False

def main():
    file1 = open('C-small-attempt0.in')
    lines = file1.read().split('\n')
    testCases = int(lines[0])
    lines = lines[1:-1]
    file1.close()

    file1 = open('C-small-attempt0.out', 'w')
    for case in range(testCases):
        i = 2 * case
        (leng, reps) = [int(x) for x in lines[i].split(' ')]
        stng = lines[i + 1]
        if findIJK(stng, reps):
            out = 'Case #%d: YES\n'%(case + 1)
        else:
            out ='Case #%d: NO\n'%(case + 1)
        file1.write(out)

    file1.close()

main()
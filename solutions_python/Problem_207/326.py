in_file = 'B-small-attempt1.in'
out_file = 'B-small.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')


def insert(string, index, sub):
    return string[:index] + sub + string[index:]


t = int(inp.readline())
for case in range(1, t+1):
    n, r, o, y, g, b, v = list(map(int, inp.readline().split()))
    list1 = [r, y, b]
    list1.sort()

    list2 = []
    if r == list1[0]:
        list2.append('R')
    elif y == list1[0]:
        list2.append('Y')
    else:
        list2.append('B')

    if r == list1[1] and 'R' not in list2:
        list2.append('R')
    elif y == list1[1] and 'Y' not in list2:
        list2.append('Y')
    else:
        list2.append('B')

    if 'R' not in list2:
        list2.append('R')
    elif 'Y' not in list2:
        list2.append('Y')
    else:
        list2.append('B')

    if list1[2] > list1[1] + list1[0]:
        ans = 'IMPOSSIBLE'
    else:
        ans = ''
        for i in range(list1[0]):
            ans += list2[0] + list2[1]
        for i in range(list1[1]-list1[0]):
            ans += list2[2] + list2[1]
        for i in range(list1[2]-list1[1]+list1[0]):
            ans = insert(ans, 2*i, list2[2])

    out.write('Case #{}: {}\n'.format(case, ans))

inp.close()
out.close()

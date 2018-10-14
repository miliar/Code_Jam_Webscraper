def get_number_of_test_case():
    return int(raw_input().strip())

def solve_case(t):
    word, n = raw_input().strip().split()
    n = int(n)
    l = len(word)

    position_list = list()
    begin = 0
    length = 0
    i = 0

    while i < l:
        if word[i] not in ['a', 'e', 'i', 'o', 'u',]:
            length += 1
        else:
            if length >= n:
                position_list.append([begin, length,])
            length = 0
            begin = i + 1
        i += 1
    if length >= n:
        position_list.append([begin, length,])
        
    output = 0
    p = 0
    for item in position_list:
        output += (item[0] - p + 1) * (l - (item[0] + n) + 1)
        x = item[1] - n
        y = l - (item[0] + n)
        z = y - x
        output += ((y * (y + 1)) - (z * (z + 1))) / 2
        p = item[0] + item[1] - n + 1

    print 'Case #%d: %d' % (t, output,)

T = get_number_of_test_case()
t = 1
while t <= T:
    solve_case(t)
    t += 1


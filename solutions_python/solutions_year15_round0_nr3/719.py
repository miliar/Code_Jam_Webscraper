from sys import stdin

table = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
        'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}

def solve(line, size, reps):
    result = '1'
    block_result = result

    found_i = False
    found_j = False
    for i in line:
        negative = False
        if result[0] == '-':
            negative = True
            result = result[1]
        result = table[result][i]

        if negative: result = '-'+result
        if len(result) == 3: result = result[2]

        if result == 'i': found_i = True
        elif result == 'k' and found_i: found_j = True

        size -= 1
        if size == 0: block_result = result
        if found_j and size <= 0: break

    if found_i and found_j:
        if block_result == '1': return 'NO'
        elif block_result == '-1':
            if reps % 2 == 0: return 'NO'
            else: return 'YES'
        elif reps % 4 != 2: return 'NO'
        else: return 'YES'
    else: return 'NO'

cases = int(stdin.readline())
for i in range(1,cases+1):
    L,X = [int(x) for x in stdin.readline().strip().split()]
    prefix = stdin.readline().strip()
    line = prefix*X
    found = solve(line,L,X)
    print("Case #{0}: {1}".format(i,found))


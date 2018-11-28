cases = int(raw_input().split()[0])

def to_bool_array(line):
    return [c == '+' for c in line]

def apply(arr, pos, k):
    for i in range(pos, pos + k):
        arr[i] = not arr[i]

def is_ok(bool_array):
    return reduce(lambda a, b: a and b, bool_array, True)

for i in range(cases):
    data = raw_input().split()
    line = data[0]
    k = int(data[1])
    bool_array = to_bool_array(line)

    counter = 0
    for j in range(0, len(bool_array) - k + 1):
        if not bool_array[j]:
            apply(bool_array, j, k)
            counter += 1
    
    if is_ok(bool_array):
        print 'Case #%d: %d' % (i + 1, counter)
    else:
        print 'Case #%d: IMPOSSIBLE' % (i + 1,)
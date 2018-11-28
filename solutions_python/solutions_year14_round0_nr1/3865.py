def get_row(n):
    return_arr = []
    for i in range(1, 5):
        arr = raw_input()
        if n == i:
            return_arr = map(int, arr.split(' '))

    return return_arr

n = input()
for i in xrange(1, n+1):
    a = input()
    arr_a = set(get_row(a))
    b = input()
    arr_b = set(get_row(b))
    return_arr = arr_a.intersection(arr_b)
    l = len(return_arr)
    if l == 1:
        print("Case #%d: %d" % (i, list(return_arr)[0]))
    elif l > 1:
        print("Case #%d: Bad magician!" % i)
    else:
        print("Case #%d: Volunteer cheated!" % i)

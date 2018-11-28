def test_sort_small(data):
    while ''.join(sorted(str(data))) != str(data):
        data -= 1
    return data


def test_sort_large(data):
    res = [0]
    err = False
    for val in list(str(data)):
        val = int(val)
        if err is False and val >= res[-1]:
            res.append(val)
        elif err:
            res.append(9)
        elif int(val) < res[-1]:
            res[-1] -= 1
            res.append(9)
            err = True
    res = int(''.join([str(i) for i in res]))
    if err is False:
        return res
    else:
        return test_sort_large(res)

if __name__ == '__main__':
    count = int(input())
    for x in range(count):
        inp = int(input())
        print("Case #%s: %s" % (x + 1, test_sort_large(inp)))

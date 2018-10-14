P = float(2)


def f(C, F, X, count):
    global P
    # if count == 0:
    #     return X / P
    res = 0
    for i in range(count):
        res += C / (P + i * F)
    res += X / (P + F * count)
    return res


def foo(C, F, X):
    prev = f(C, F, X, 0)
    curr = f(C, F, X, 1)
    # print prev, curr
    i = 2
    while curr < prev:
        prev = curr
        curr = f(C, F, X, i)
        # print curr, prev, i
        i += 1
    return prev

# def foo(C, F, X):
#     global P
#     p = P
#     max_count = int(round(X / C + 0.5))
#     f = [None] * max_count
#     f[0] = X / P
#     i = 1
#     while i < max_count:
#         f[i] = C / p
#         p += F
#         i += 1
#         for i in range(1, max_count):
#             f[i] += (X - C) / (P + i * F)
#     return min(f)

def get_msg(a):
    return "%.7f" % a

def write_to_file(output_path, content):
    with open(output_path, 'w+') as output_file:
        output_file.write(content)

if __name__ == '__main__':
    input_path = 'B-small-attempt0.in'
    output_path = 'B-small-attempt0.out'
    # input_path = 'test.in'
    # output_path = 'test.out'
    outputlines = []
    with open(input_path) as input_file:
        T = int(input_file.readline())
        # print T
        for case in range(T):
            C, F, X = (float(x) for x in input_file.readline().split())
            res = foo(C, F, X)
            msg = get_msg(res)
            outputlines.append('Case #%d: %s' % (case + 1, msg))
        write_to_file(output_path, '\n'.join(outputlines))
        print outputlines


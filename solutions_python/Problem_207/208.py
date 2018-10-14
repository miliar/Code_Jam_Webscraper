n_tests = int(input())

def solve(cols):
    (a, A), (b, B), (c, C) = cols
    if a > b + c:
        return "IMPOSSIBLE"
    lst = [[A] for _ in range(a)]
    for i in range(b):
        lst[i].append(B)
    for i in range(c):
        lst[(b+i) % a].append(C)
    lst = [''.join(x) for x in lst]
    return ''.join(lst)
  
for test_case_no in range(1, n_tests+1):
    row = [int(x) for x in input().split()]

    N, r, o, y, g, b, v = row

    cols = sorted([(r, "R"), (y, "Y"), (b, "B")], reverse=True)

    print("Case #{}: {}".format(test_case_no, solve(cols)))

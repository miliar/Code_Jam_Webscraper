from collections import deque

def next_circular(n):
    s = str(n)
    d = deque(s)
    for i in range(len(s) - 1):
        d.rotate(1)
        a = list(d)
        a = ''.join(a)
        a = int(a)
        if a > n:
            yield a

testcases = int(input())


def count_them(A, B):
    all_numbers = list(range(A, B + 1))

    counter = 0
    for n in all_numbers:
        if n == 0:
            continue
        local_counter = 0
        for i in next_circular(n):
            try:
                if all_numbers[i - A] != 0:
                    local_counter += 1
                    all_numbers[i - A] = 0
            except IndexError:
                pass
        counter += local_counter * (local_counter + 1) // 2
    
    return counter


for i in range(1, testcases + 1):
    A, B = [int(x) for x in input().split()]
    print('Case #' + str(i) + ': ' + str(count_them(A, B)))

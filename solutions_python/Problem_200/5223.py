def is_tidy(x):
    return str(x) == ''.join(sorted(str(x)))

assert is_tidy(123)
assert is_tidy(224488)
assert not is_tidy(121)
assert not is_tidy(10)

def biggest_tidy(n):
    for x in range(n, 0, -1):
        if is_tidy(x):
            return x
        
assert biggest_tidy(132) == 129
assert biggest_tidy(7) == 7
assert biggest_tidy(1000) == 999
#assert biggest_tidy(111111111111111110) == 99999999999999999

i = 1
for _ in range(int(input())):
    print('Case #{}: {}'.format(i, biggest_tidy(int(input()))))
    i += 1
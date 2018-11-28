def read_ints():
    return map(int, input().strip().split())

t, = read_ints()
for test_case in range(t):
    _, audience = input().strip().split()
    standing = 0
    friends = 0
    for shyness, mem in enumerate(map(int, audience)):
        if mem:
            friends += max(0, shyness - standing)
            standing += mem + friends
    print('Case #{}: {}'.format(test_case + 1, friends))


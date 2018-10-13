def get_output(i):
    s_max, s = line.split(' ')
    s_max = int(s_max)
    s = [int(_) for _ in s]
    num_standing = 0
    num_to_invite = 0
    for i, s_i in enumerate(s):
        print(num_standing, num_to_invite)
        if (num_standing + num_to_invite < i) and s_i > 0:
            num_to_invite += i - (num_standing + num_to_invite)
        num_standing += s_i

    return num_to_invite

with open('A-large.in', 'r') as f:
    _input = [line.strip() for line in f.readlines()]
    num_test_cases = _input[0]
    _input = _input[1:]
    with open('output.txt', 'w') as fo:
        for i, line in enumerate(_input):
            print(str(i))
            fo.write('Case #' + str(i + 1) + ': ' + str(get_output(i)) + '\n')

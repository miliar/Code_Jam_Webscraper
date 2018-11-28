import string

def get_rows(lines):
    if lines == 1:
        return map(str, raw_input().split())
    return [raw_input() for _ in range(lines)] #[map(str, raw_input().split()) for _ in range(lines)]

def get_diff(strings):
    length = len(get_count(strings[0]))
    total = [0] * length
    for s in strings:
        s_count = get_count(s)
        for i in range(length):
            total[i] += s_count[i]
    for i in range(length):
        total[i] = round(total[i] / float(len(strings)))
    total2 = 0
    for s in strings:
        s_count = get_count(s)
        for char in range(length):
            total2 += int(abs(s_count[char] - total[char]))
    return total2

def get_count(s):
    seq = [1]
    prev = s[0]
    for char in s[1:]:
        if char == prev:
            seq[-1] += 1
        else:
            seq.append(1)
            prev = char
    return seq

def unique(strings):
    x = set(strings[0])
    for i in strings[1:]:
        if set(i) != x:
            return False

    seq = get_seq(strings[0])
    for s in strings[1:]:
        if get_seq(s) != seq:
            return False
    return True

def get_seq(s):
    seq = []
    prev = s[0]
    seq.append(prev)
    for char in s[1:]:
        if char != prev:
            prev = char
            seq.append(prev)
    return seq

cases = input()
for i in range(1, cases + 1):
    num_strings = input()
    strings = get_rows(num_strings)
    if not unique(strings):
        diff = 'Fegla Won'
    else:
        diff = get_diff(strings)
    print "Case #{0}: {1}".format(i, diff)


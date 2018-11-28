# def to_num(s):
#     bit_string = ''.join(['0' if c == '+' else '1' for c in s])
#     return int(bit_string, 2)

def reverse(s):
    return ''.join(['+' if c == '-' else '-' for c in s])

def flip(s, i, k):
    return ''.join([s[:i], reverse(s[i:i+k]), s[i+k:]])

def dfs(s, happy, k, flip_positions, mem):
    if s == happy:
        return 0
    mem.add(s)
    for i in flip_positions:
        s_flipped = flip(s, i, k)
        if not s_flipped in mem:
            fp_copy = flip_positions.copy()
            fp_copy.remove(i)
            res = dfs(s_flipped, happy, k, fp_copy, mem)
            if res >= 0:
                return 1 + res
    return -1

def foo(line):
    args = line.split()
    s, k = args[0], int(args[1])
    happy = ''.join(['+' for _ in xrange(len(s))])
    flip_positions = set(i for i in xrange(len(args[0]) - k + 1))
    num_flip = dfs(s, happy, k, flip_positions, set())
    return num_flip if num_flip >= 0 else "IMPOSSIBLE"

if __name__ == "__main__":
    fo = open("output", "w")
    with open("A-small-attempt0.in") as f:
        text = f.readlines()
        text = [line.strip() for line in text]
        [fo.write("Case #{0}: {1}\n".format(i, foo(text[i]))) for i in xrange(1, len(text))]
    fo.close()
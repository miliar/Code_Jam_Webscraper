class Impossible(Exception): pass

def solve(s, k):
    flips = 0
    for i, v in enumerate(s):
        if v % 2 == 0:
            continue
        else:
            # flip
            flips += 1
            try:
                for j in range(i, i+k):
                    s[j] += 1
            except IndexError:
                raise Impossible()
    return flips

if __name__ == '__main__':
    import io
    for i, line in enumerate(io.open('A-large.in', 'r').readlines()):
        if i == 0: continue
        s_, k = line.split()
        k = int(k)
        s = [char == '-' for char in s_]
        try:
            print('Case #{}: {}'.format(i, solve(s, k)))
        except Impossible:
            print('Case #{}: IMPOSSIBLE'.format(i))
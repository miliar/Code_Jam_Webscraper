def solve(a, b):
    res = []
    for num in  xrange(a, b + 1):
        st = str(num)
        for tail_len in xrange(1, len(st)):
            rec = int(st[-tail_len:] + st[:-tail_len])
            if rec >= a and rec <= b and rec > num:
                res.append((num, rec))
    return len(set(res))



def main():
    tc = int(raw_input())
    for i in xrange(tc):
        print('Case #{}: {}'.format(
            i + 1, 
            solve(*map(int, raw_input().split()))))

if __name__ == '__main__':
    main()

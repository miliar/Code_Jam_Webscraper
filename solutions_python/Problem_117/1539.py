for case in range(1, input()+1):
    N, M = map(int, raw_input().split())
    field = [raw_input().split() for _ in range(N)]
    field = [line for line in field if any(x == '2' for x in line)]
    N = len(field)
    field = zip(*field)
    field = map(''.join, field)
    field = [line for line in field if line.count('1') < N]
    answer = 'NO' if '1' in ''.join(field) else 'YES'
    print 'Case #{}: {}'.format(case, answer)

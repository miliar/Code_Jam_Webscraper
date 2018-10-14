def get_moves(N, K):
    base = (1<<K)-1
    moves = [base]
    for i in range(N-K):
        moves.append(moves[-1]<<1)
    return moves

def try_moves(S, moves, count):
    #print(bin(S))
    if S == 0:
        return count
    if moves == []:
        return -1
    res = try_moves(S, moves[1:], count)
    if res >= 0:
        return res
    else:
        return try_moves(S^moves[0], moves[1:], count+1)

def run(s, K):
    S = int(s.replace('+', '0').replace('-', '1'), 2)
    return try_moves(S, get_moves(len(s), K), 0)

infile = open('A-small-attempt0.in')
outfile = open('A-small-attempt0.out', 'w')

T = int(infile.readline().strip())
for i in range(T):
    line = infile.readline().strip().split(' ')
    count = run(line[0], int(line[1]))
    res = "Case #{}: {}"
    if count < 0:
        res = res.format(i+1, 'IMPOSSIBLE')
    else:
        res = res.format(i+1, count)
    #print(res)
    outfile.write(res+'\n')

infile.close()
outfile.close()

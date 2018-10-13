def fill(s):
    seq = [c for c in s if c != '?']
    ans = list()
    flag = False
    for c in s:
        if c != '?':
            if flag:
                del seq[0]
            else:
                flag = True
        ans.append(seq[0])
    return ''.join(ans)

def solve(k):
    r, c = map(int, input().split())
    last = None
    cnt = 0
    board = list()
    for _ in range(r):
        s = input()
        if any(q != '?' for q in s):
            if last:
                last = fill(s)
            else:
                last = fill(s)
                board = [last] * cnt + board
            board.append(last)
        elif last:
            board.append(last)
        else:
            cnt += 1
    board = ["Case #%d:" % k] + board
    return '\n'.join(board) 

t = int(input())
for k in range(1, t + 1):
    print(solve(k))

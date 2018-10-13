
def solve(ll):
    lettersFound = set(['?'])
    for i in range(len(ll)):
        for j in range(len(ll[0])):
            if ll[i][j] not in lettersFound:
                right = j + 1
                while right < len(ll[0]) and ll[i][right] == '?':
                    ll[i][right] = ll[i][j]
                    right += 1
                left = j - 1
                while 0 <= left and ll[i][left] == '?':
                    ll[i][left] = ll[i][j]
                    left -= 1
                up = i - 1
                while 0 <= up and all(ch == '?' for ch in ll[up][left+1:right]):
                    ll[up][left+1:right] = [ll[i][j]] * len(ll[i][left+1:right])
                    up -= 1
                down = i + 1
                while down < len(ll) and all(ch == '?' for ch in ll[down][left+1:right]):
                    ll[down][left+1:right] = [ll[i][j]] * len(ll[i][left+1:right])
                    down += 1
                lettersFound.add(ll[i][j])
    return ll

t = int(input())
for i in range(1, t+1):
    line = input()
    r = int(line.split(" ")[0])
    c = int(line.split(" ")[1])
    ll = list()
    for j in range(r):
        ll.append(list(input()))
    print("Case #{}:".format(i))
    ll = solve(ll)
    for row in ll:
        print(''.join(row))
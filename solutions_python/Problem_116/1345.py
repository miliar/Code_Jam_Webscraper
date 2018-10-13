N = 4

def check_seq(s, c):
    cnt = s.count(c)
    return ((cnt == N - 1) and ('T' in s)) or (cnt == N)
    
def check_win(a, c):
    for i in range(N):
        if check_seq(a[i], c): return True
        col = ''.join(s[i] for s in a)
        if check_seq(col, c): return True
    diag1 = ''.join(a[i][i] for i in range(N)) 
    if check_seq(diag1, c): return True
    diag2 = ''.join(a[i][N - i - 1] for i in range(N)) 
    if check_seq(diag2, c): return True
    
    return False

if __name__ == '__main__':
    Tn = int(raw_input())
    for Tc in range(Tn):
        a = []
        for i in range(N):
            a.append(raw_input())
        raw_input()
#         print a
        output = 'Case #%d: ' % (Tc + 1)
        if check_win(a, 'X'):
            output += 'X won'
        elif check_win(a, 'O'):
            output += 'O won'
        elif '.' in ''.join(a):
            output += 'Game has not completed'
        else:
            output += 'Draw'
        print output
            

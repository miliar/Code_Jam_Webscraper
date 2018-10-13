def main():
    num_of_tests = int(raw_input())
    for test_i in range(num_of_tests):
        s = []
        for i in range(4):
            s.append(raw_input())
        try:
            line = raw_input()
        except:
            return

        def is_win(p):
            a = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    if s[i][j] == p or s[i][j] == 'T':
                        a[i][j] = 1
            for i in range(4):
                if sum(a[i]) == 4: return True
            for j in range(4):
                if sum([a[i][j] for i in range(4)]) == 4: return True
            if sum([a[i][i] for i in range(4)]) == 4: return True
            if sum([a[i][3 - i] for i in range(4)]) == 4: return True
            return False
        
        ans = ''
        if is_win('X'):
            ans = 'X won'
        elif is_win('O'):
            ans = 'O won'
        elif '.' in ''.join(s):
            ans = 'Game has not completed'
        else:
            ans = 'Draw'
        print "Case #%d: %s" % (test_i + 1, ans)

if __name__ == "__main__":
    main()
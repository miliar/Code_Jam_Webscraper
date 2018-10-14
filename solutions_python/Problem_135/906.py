def read_matrix():
    res = []
    for i in range(4):
        row = map(int, raw_input().strip().split())
        res.append(row)
    return res

if __name__ == '__main__':
    T = input()
    for tnum in range(1, T+1):
        possibilities = set(range(1,17))
        for i in range(2):
            row = input()
            mat = read_matrix()
            possibilities &= set(mat[row - 1])
            
        l = len(possibilities)
        if l > 1:
            ans = 'Bad magician!'
        elif l == 0:
            ans = 'Volunteer cheated!'
        else:
            ans = possibilities.pop()
             
        print 'Case #%d: %s' % (tnum, ans)
def lex(n):
    x = len(n)-1
    while n[x-1] >= n[x]:
        x = x-1
        if x == 0: break
    y = len(n)
    while n[y-1] <= n[x-1]:
        y = y-1
        if y == 0: break

    n[x-1],n[y-1] =  n[y-1], n[x-1]

    x += 1
    y = len(n)
    while x < y:
        n[x-1],n[y-1] =  n[y-1], n[x-1]
        x += 1
        y -= 1
    return n

if __name__ == '__main__':
    """
    import sys
    print lex([0,8,0,0])
    sys.exit()
    """
    f = open('B-large.in')
    w = open('B-large.out','w')

    n_case = int(f.readline().strip())

    for i in range(1,n_case+1):
        s_n = f.readline().strip()
        n = map(int,[j for j in s_n])
        n_tmp = [x for x in n]
        n_tmp.sort(reverse=True)
        #print n, n_tmp

        if len(n) == 1:
            s_ans = str(n[0]) + '0'
        elif n_tmp == n:
            n.insert(0,0)
            ans = lex(n)
            s_ans = reduce(lambda x,y: str(x) + str(y),ans)
        else:
            ans = lex(n)
            s_ans = reduce(lambda x,y: str(x) + str(y),ans)
            if s_ans == s_n:
                ans.insert(0,0)
                print ans
                ans = lex(ans)
                print ans
                if ans[0] == 0:
                    ans = ans[1:]
                s_ans = reduce(lambda x,y: str(x) + str(y),ans)

        if i == n_case:
            w.write('Case #' + str(i) + ': ' + s_ans)
        else:
            w.write('Case #' + str(i) + ': ' + s_ans + '\n')
    f.close()
    w.close()


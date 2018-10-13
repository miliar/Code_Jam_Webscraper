input_file = 'B-small-attempt1.in'
output_file = 'B.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            arr = map(int, f.readline().split())
            n = arr.pop(0)
            ans = 0
            if max(arr) * 2 > n:
                ans = 'IMPOSSIBLE'
            else:
                ans = ['Q']
                arr = [[c, col] for c, col in zip(arr, 'ROYGBV') if c]
                # print arr
                arr.sort(key=lambda x: x[0])
                arr[-1][0] += .5
                while arr:
                    arr.sort(key=lambda x: x[0])
                    if arr[-1][1] != ans[-1]:
                        ans.append(arr[-1][1])
                        arr[-1][0] -= 1
                        if arr[-1][0] < 1:
                            arr.pop(-1)
                    elif len(arr) > 1:
                        ans.append(arr[-2][1])
                        arr[-2][0] -= 1
                        if arr[-2][0] < 1:
                            arr.pop(-2)
                    else:
                        ans = 'IMPOSSIBLE'
                        break
                ans = ''.join(ans[1:])
                if ans[0] == ans[-1]:
                    ans = 'IMPOSSIBLE'
            print 'Case #{i}: {res}'.format(res=ans, i=i)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=i))
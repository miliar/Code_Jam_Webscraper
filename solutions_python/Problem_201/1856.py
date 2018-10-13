def solve(N, K):
    if N % 2 == 0:
        task = [(N/2, N/2-1)]
    else:
        task = [(N/2, N/2)]
    while len(task) > 0:
        # print task
        mx, mn = task.pop(0)
        if mx == 0 and mx == 0:
            return mx, mn 
        mx_item = None
        if mx % 2 == 0:
            mx_item = (mx/2, max(mx/2-1, 0))
        else:
            mx_item = (mx/2, mx/2)
        
        if len(task) == 0:
            task.append(mx_item)
        else:
            while i >= 0:
                if task[i][0] == mx_item[0] and task[i][1] == mx_item[1]:
                    task.insert(i, mx_item)
                    break
                if task[i][0] >= mx_item[0] and task[i][1] >= mx_item[1]:
                    task.insert(i+1, mx_item)
                    break
                i -= 1

        mn_item = None
        if mn % 2 == 0:
            mn_item = (mn/2, max(mn/2-1, 0))
        else:
            mn_item = (mn/2, mn/2)
        i = len(task)-1
        while i >= 0:
            if task[i][0] == mn_item[0] and task[i][1] == mn_item[1]:
                task.append(mn_item)
                break
            if task[i][0] >= mn_item[0] and task[i][1] >= mn_item[1]:
                task.insert(i+1, mn_item)
                break
            i -= 1

        if K == 1:
            return mx, mn
        K -= 1
        # raw_input()

for i in range(int(raw_input())):
    N, K = raw_input().split(' ')
    result = solve(int(N), int(K))
    print 'Case #%d: %s %s' % (i+1, result[0], result[1])

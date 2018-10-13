t = int(raw_input().strip())
for ti in range(1, t+1):
    r,c = [int(x) for x in raw_input().strip().split(' ')]
    cake_arr = []
    answer = []
    for row in range(r):
        cake_arr.append(raw_input().strip())
    for cc in cake_arr:
        if '?' not in cc:
            answer.append(cc)
        else:
            curr = None
            arr = []
            for col in cc:
                if col != '?':
                    curr = col
                    arr.append(col)
                elif curr != None:
                    arr.append(curr)
                else:
                    arr.append('?')
            if '?' not in arr:
                answer.append(''.join(arr))
            else:
                curr = None
                arr = arr[::-1]
                arr2 = []
                for acol in arr:
                    if acol != '?':
                        curr = acol
                        arr2.append(acol)
                    elif curr!= None:
                        arr2.append(curr)
                    else:
                        arr2.append('?')
                answer.append(''.join(arr2[::-1]))
    
    for i in xrange(r):
        answer2 = []
        for ai in range(len(answer)):
            if '?' not in answer[ai]:
                answer2.append(answer[ai])
            else:
                arr3 = []
                for ac in range(len(answer[ai])):
                    if answer[ai][ac] != '?':
                        arr3.append(answer[ai][ac])
                    elif ai != 0 and answer[ai - 1][ac] != '?':
                        arr3.append(answer[ai-1][ac])
                    elif ai < r-1 and answer[ai + 1][ac] != '?':
                        arr3.append(answer[ai+1][ac])
                    else:
                        arr3.append('?')
                answer2.append(''.join(arr3))
        answer = answer2
                                    
    print 'Case #' + str(ti) + ':'
    for a in answer2:
        print a
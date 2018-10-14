T = input()



for case in range(1,T+1):
    R,C = [int(_) for _ in raw_input().split()]

    store = [raw_input() for _ in range(R)]
    ans = [[] for _ in range(R)]

    todorow = 0
    curbottom = -1
    
    for i in range(R):
        letters = [_ for _ in range(C) if store[i][_] != '?']
        if letters != []:
            curbottom = i #

            
            for j in range(i-todorow,i+1):
                start = 0
                
                for l in letters[:-1]:
                    ans[j] += store[i][l] * (l - start + 1)
                    start = l+1

                ans[j] += store[i][letters[-1]] * (C-1 - start + 1)
                    
 
                



            todorow = 0

        else:
            todorow += 1
            
        


    if todorow > 0:
        #print "YES"
        i = curbottom
        letters = [_ for _ in range(C) if store[i][_] != '?']
        for j in range(i+1,R):
            start = 0
                
            for l in letters[:-1]:
                ans[j] += store[i][l] * (l - start + 1)
                start = l+1

            ans[j] += store[i][letters[-1]] * (C-1 - start + 1)
            



    print "Case #%d:" % case
    for i in ans:
        print ''.join(i)

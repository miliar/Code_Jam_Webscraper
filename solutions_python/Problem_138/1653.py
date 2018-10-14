t = int(raw_input())
for i in range(1, t + 1):
    n = int(raw_input())
    parser = lambda x: int(x.split(".")[1])

    naomi = sorted(map(parser, raw_input().split(" ")))
    ken = sorted(map(parser, raw_input().split(" ")))

    naive_score = 0
    deceit_score = 0
    largest = n-1
    index_lst = range(n)
    ken_burnt = [False for j in index_lst]
    naomi_burnt = [False for j in index_lst]

    j = 0
    while (j + naive_score) < n:
        while ken[j + naive_score] < naomi[j]:
            naive_score += 1
            #print j, naive_score
            if (j + naive_score) >= n:
                break
        j += 1

    ken_burnt = [False for j in index_lst]
    #naomi_burnt = [False for j in index_lst]
    largest = n-1
    smallest = 0

    for j in range(n):
        if ken[smallest] < naomi[j]:
            smallest += 1
            deceit_score +=1
        else:
            largest -= 1
        
    print "Case #" + str(i) + ":", deceit_score, naive_score
    #print "Naomi: ", naomi
    #print "Ken  : ", ken

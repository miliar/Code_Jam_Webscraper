import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    print "Case #" + str(tc) + ":",
    # print "--------------------------------------------"
    N = int(sys.stdin.readline())
    n = sys.stdin.readline().split()
    n = [float(i) for i in n]
    n.sort(reverse=True)
    n_used = [0]*N
    k = sys.stdin.readline().split()
    k = [float(i) for i in k]
    k.sort(reverse=True)
    k_used = [0]*N
    # print n
    # print k
    # print "done with input-"
    allList = []
    for i in n:
        allList.append([i, "n"])
    for i in k:
        allList.append([i, "k"])
    allList.sort()
    # print allList
    acc = 0
    min = 0
    for i in allList:
        if i[1] == "k":
            acc += 1
        if i[1] == "n":
            acc -= 1
        # print acc, "-"  ,
        if acc < min:
            min = acc
    # print "number of times N must loose", abs(min)
    print N-abs(min), 








    k_points = 0
    for i in range(N):
        k_choice = k[i]
        foundOneToBeat = False
        for j in range(N):
            if n_used[j] == 0:
                if n[j] < k_choice:
                    k_points +=1
                    foundOneToBeat = True
                    k_used[i] = 1
                    n_used[j] = 1
                    break
        if not foundOneToBeat:
            break



    print N-k_points
























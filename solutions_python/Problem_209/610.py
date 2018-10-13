import math
N_questions = input()

for q_num in range(int(N_questions)):
    n,k = list(map(int,input().split()))

    cakes = []
    for i in range(n):

        rad, height = list(map(int,input().split()))

        cakes.append([rad, 2*rad*height, i])

    cakes.sort(key = lambda x : -x[1]) # sorting by the added height
    best_by_base = []

    for i in range(n):
        best_by_base.append(cakes[i][0]**2 + cakes[i][1])

        count = 1
        for j in range(n):
            if count == k:
                break
            if i != j and cakes[j][0] <= cakes[i][0]:
                count += 1
                best_by_base[i] = best_by_base[i] + cakes[j][1] # adding the things one by one

    print("Case #{}: {:.9f}".format(q_num + 1, max(best_by_base)*math.pi) )

__author__ = 'sushrutrathi'



def find_min(arr):
    i = arr[0]
    for elem in arr:
        i = min(i,elem)
    return i
opt = open("output.txt", 'w')
with open("input.txt") as f:
    total_tests = int(f.readline())
    for tests in range(1,total_tests+1):
        n,q = [int(i) for i in f.readline().strip().split(' ')]
        hor_stam = []
        hor_sp = []
        for i in range(n):
            stam, sp = [int(i) for i in f.readline().strip().split(' ')]
            hor_stam.append(stam)
            hor_sp.append(sp)

        dist_mat = []

        for i in range(n):
            dist = [int(i) for i in f.readline().strip().split(' ')]
            dist_mat.append(dist)

        u,v = [int(i) for i in f.readline().strip().split(' ')]

        ans = 0

        sequence = [0]
        curr = 0
        for i in range(n-1):
            for j in range(n):
                if dist_mat[curr][j]!=-1:
                    curr = j
                    sequence.append(curr)
                    break

        time_mat = [[10000000000000 for i in range(n)] for j in range(n)]

        time_mat[0][0] = 0

        i = 0

        for horse_ind in range(n-1):
            base_horse = sequence[horse_ind]
            base = find_min(time_mat[base_horse])
            i = horse_ind
            curr = sequence[i]
            dist = 0

            while i<(n-1):
                dist += dist_mat[curr][sequence[i+1]]
                time = 1.0*dist/hor_sp[base_horse]
                if dist > hor_stam[base_horse]:
                    break
                time_mat[sequence[i+1]][base_horse] = time+base
                i+=1
                curr = sequence[i]

        i=0


        opt.write("Case #" + str(tests) + ": " + str(find_min(time_mat[n-1])) + '\n')
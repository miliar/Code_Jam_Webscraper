fname = "B-small-attempt1"
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')

T = int(fin.readline())
for i in range(T):
    line = fin.readline().split()
    L, t, N, C = [int(line[x]) for x in range(4)]
    dists = [int(x)*2 for x in line[4:]]
    while len(dists) < N:
        dists.extend(dists)
        
    stars = dists[:N]

    for j in range(L):
        time = 0
        max_save = [0, 0]
        for k in range(N):
            time_saved = 0
            if time > t:
                time_saved = stars[k] / 2
            elif time + stars[k] > t:
                time_saved = (stars[k] - (t - time)) / 2
                
            time += stars[k]
            if time_saved > max_save[0]:
                max_save = [time_saved, k]
        stars[max_save[1]] -= max_save[0]

    answer = sum(stars)
    fout.write('Case #{0}: {1}\n'.format(i+1, answer))

fin.close()
fout.close()
    

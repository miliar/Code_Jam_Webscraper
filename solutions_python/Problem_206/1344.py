def get_speed(horses, D):
    horses_cp = horses.copy()
    for (k1, s1) in horses_cp:
        for (k2, s2) in horses_cp:
            if k1 < k2 and (D - k1)/s1 < (D - k2)/s2:
                horses.discard((k1, s1))
        
    hi = max([(D - k)/s for (k, s) in horses])
    return D/hi

infile = open("A-large.in")
outfile = open("A-large.out", 'w')

T = int(infile.readline().strip())
for i in range(T):
    [D, N] = [int(x) for x in infile.readline().strip().split(' ')]
    horses = set()
    for j in range(N):
        [K, S] = [int(x) for x in infile.readline().strip().split(' ')]
        if K <= D:
            horses.add((K, S))
    outfile.write("Case #{}: {:.6f}\n".format(i+1, get_speed(horses, D)))

outfile.close()
print("done")
infile.close()

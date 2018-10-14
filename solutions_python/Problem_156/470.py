inf = open("input.txt", "r")
ouf = open("out.txt", "w")


for i in range(int(inf.readline())):
    inf.readline()
    l = sorted(list(map(int, inf.readline().split())), reverse = True)
    length = len(l)
    min_sum = l[0]
    for i1 in range(1, l[0]):
        moves = 0
        itr = 0
        while itr < length and l[itr] > i1:
            moves += l[itr] // i1
            if not l[itr] % i1:
                moves -= 1
            
            itr += 1
        
        min_sum = min(min_sum, i1 + moves)
    
    ouf.write("Case #" + str(i + 1) + ": " + str(min_sum) + "\n")

inf.close()
ouf.close()
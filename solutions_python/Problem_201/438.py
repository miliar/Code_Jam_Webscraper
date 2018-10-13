def find_last_size():
    line = input().split()
    k = int(line[1])
    d = {int(line[0]):1}

    while True:
        total_values = 0
        new_d = {}
        for key, value in d.items():
            total_values += value
            if key % 2 == 1:
                if (key - 1) >> 1 in new_d:
                    new_d[(key - 1) >> 1] += 2 * value
                else:
                    new_d[(key - 1) >> 1] = 2 * value
            else:
                if (key - 1) >> 1 in new_d:
                    new_d[(key - 1) >> 1] += value
                else:
                    new_d[(key - 1) >> 1] = value
                if ((key - 1) >> 1) + 1 in new_d:
                    new_d[((key - 1) >> 1) + 1] += value
                else:
                    new_d[((key - 1) >> 1) + 1] = value
        if total_values >= k:
            l = sorted(d.items(), key=lambda t: -t[0])
            for (size, amount) in l:
                if size != 0:
                    if amount >= k:
                        return size
                        #richtige größe
                    else:
                        k -= amount
            return -1
        else:
            k -= total_values
            d = new_d
            #print(d)
            #print(k)

n = int(input())
for i in range(n):
    print("Case #",i+1,": ",sep="",end="")
    f = find_last_size()
    if f%2 == 1:
        print(f >> 1, f >> 1)
    else:
        print(((f - 1) >> 1) + 1, (f - 1) >> 1)

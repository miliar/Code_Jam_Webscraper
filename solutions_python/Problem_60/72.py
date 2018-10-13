with open("b.in") as fin:
    with open("b.out", "w") as fout:
        c = int(fin.readline())
        for i in range(c):
            (n, k, b, t) = tuple(int(x) for x in fin.readline().split())
            distances = [b - int(x) for x in fin.readline().split()]
            speeds = [int(x) for x in fin.readline().split()]
            chicks = sorted(zip(distances, speeds))

            done = 0
            swaps = 0
            for j in range(len(chicks)):
                (d, s) = chicks[j]
                if d/s > t:
                    # Too slow, need to swap
                    swaps += k - done
                else:
                    done += 1
                if done == k:
                    break
                
            fout.write("Case #" + str(i + 1) + ": ")
            if done < k:
                fout.write("IMPOSSIBLE")
            else:
                fout.write(str(swaps))
            fout.write("\n")
                    

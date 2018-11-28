fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()

    #print line

    pancakes = line[0]
    k = int(line[1])

    currflips = []
    result = ""

    for j in xrange(0, len(pancakes)):
        curr = pancakes[j]
        state = 0 if curr == '-' else 1  # 0 is unflipped

        # Calculate current state of pancake
        prev_flips = currflips[j-1] if j > 0 else 0
        unaffected_flips = currflips[j-k] if j >= k else 0
        flipdiff = prev_flips - unaffected_flips

        needs_flip = 0
        if (state + flipdiff) % 2 == 0: # unflipped state
            needs_flip = 1
            currflips.append(prev_flips + 1)
        else:
            currflips.append(prev_flips)

        if needs_flip and j > len(pancakes)-k: #cannot flip anymore
            result = "IMPOSSIBLE"
            break

    if result != "IMPOSSIBLE":
        result = currflips[-1]


    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()

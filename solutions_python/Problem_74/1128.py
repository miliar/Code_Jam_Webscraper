import time, math, re
start = time.time()

infile = open("A.in")
outfile = open("A.out", "w")

for k in range(int(infile.readline())):
    line = infile.readline()

    seq_order = re.findall('([O|B])', line)
    orange_seq = [int(i) for i in re.findall('O (\d+)', line)]
    blue_seq = [int(i) for i in re.findall('B (\d+)', line)]
    #print(seq_order)

    total = 0
    free_blue_mov = 0
    free_orange_mov = 0
    
    orange_task = 0
    blue_task = 0

    orange_loc = 1
    blue_loc = 1

    for t in seq_order:
        if t == "O":
            delta = total
            dist = abs(orange_seq[orange_task] - orange_loc)
            if free_orange_mov < dist:
                total += dist - free_orange_mov + 1
            else:
                total += 1
            free_orange_mov = 0
            free_blue_mov += total - delta
            orange_loc = orange_seq[orange_task]
            orange_task += 1
        else:
            delta = total
            dist = abs(blue_seq[blue_task] - blue_loc)
            if free_blue_mov < dist:
                total += dist - free_blue_mov + 1
            else:
                total += 1
            free_orange_mov += total - delta
            free_blue_mov = 0
            blue_loc = blue_seq[blue_task]
            blue_task += 1
    
    outfile.write("Case #" + str(k+1) + ": " + str(total) + "\n")

infile.close()
outfile.close()

print(time.time() - start)

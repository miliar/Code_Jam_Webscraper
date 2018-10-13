

filer = open("coco.txt")

copious = 0

for line in filer:
    if copious == 0:
        copious += 1
        continue
    r = 0
    r_count = 0
    A = int(line.split(" ")[0])
    B = int(line.split(" ")[1])
    if A < 10:
        print "Case #" + str(copious) + ": 0"
        copious += 1
        continue
    for i in range(A, B+1):
        si = str(i)
        pairs = []
        for j in range(len(si)-1):
            new = si[len(si)-(j+1):]
            new += si[:len(si)-(j+1)]
            if (int(new) > i) and (int(new) <= B):
                pair = (i,new)
                if pairs != []:
                    if pairs.count(pair) > 0:
                        continue
                r_count += 1
                pairs.append(pair)
    print "Case #" + str(copious) + ": " + str(r_count)
    copious += 1

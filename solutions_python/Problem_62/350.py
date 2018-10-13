casenumber = 1
file = open("A-small-attempt0.in")
wfile = open("2.txt", "w")
numberofcases = int(file.readline()) + 1
while casenumber < numberofcases:
    N = int(file.readline())
    windows = []
    for x in range(0, N):
        line = file.readline()
        line = line.split()
        
        windows.append(line)
    inters = []
    for coord1 in windows:
        for coord2 in windows:
            if coord1 == coord2:
                pass
            p1 = (0, int(coord1[0]))
            p2 = (1, int(coord1[1]))
            p3 = (0, int(coord2[0]))
            p4 = (1, int(coord2[1]))
            
            if p1[1] > p3[1]:
                if p2[1] < p4[1]:
                    item = [coord1, coord2]
                    item.sort()
                    if item not in inters:
                        inters.append(item)
            if p1[1] < p3[1]:
                if p2[1] > p4[1]:
                    item = [coord1, coord2]
                    item.sort()
                    if item not in inters:
                        inters.append(item)
                    
    wfile.writelines("Case #" + str(casenumber) + ": " + str(len(inters)) + "\n")
    casenumber+=1
    
wfile.close()
        

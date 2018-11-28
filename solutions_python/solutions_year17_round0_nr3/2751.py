fname = "C-small-1-attempt2.in"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

id = 1
for line in content[1:]:
    split = line.split(' ')
    array = []
    for i in range(int(split[0])+2):
        array.append(0)
    array[0] = 1
    array[-1] = 1
    last_l = len(array)
    last_r = len(array)
    best_min_l_r = 0
    best_max_l_r = len(array)
    for j in range(0, int(split[1])):
        min_l_r = 0
        max_l_r = len(array)
        best_pos = -1
        for pos in range(0, len(array)):
            if array[pos] == 1:
                pass
            else:
                dist_l = 0
                dist_r = 0
                pos_l = 0
                pos_r = 0
                while True:
                    if array[pos - pos_l] == 1:
                        break
                    else:
                        dist_l += 1
                    pos_l += 1
                while True:
                    if array[pos + pos_r] == 1:
                        break
                    else:
                        dist_r += 1
                        pos_r += 1
                if min(dist_l, dist_r) > min_l_r:
                    min_l_r = min(dist_l, dist_r)
                    best_min_l_r = min_l_r
                    max_l_r = max(dist_l, dist_r)
                    best_max_l_r = max_l_r
                    best_pos = pos
                elif min(dist_l, dist_r) == min_l_r:
                    if max(dist_l, dist_r) > max_l_r:
                        max_l_r = max(dist_l, dist_r)
                        best_max_l_r = max_l_r
                        best_pos = pos
        array[best_pos] = 1
    if j+1 == int(split[1]):
        print("Case #" + str(id) + ": " + str(best_max_l_r-1) + ' ' + str(min_l_r-1))
        id += 1
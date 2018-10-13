infile = file("A-large.in")
outfile = file("A-large.out", "w+")
t = int(infile.readline())
dir_dic = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}
dir_list = ["^", ">", "v", "<"]
for i in range(t):
    result = 0
    failed = False
    inline = infile.readline().split()
    r = int(inline[0])
    c = int(inline[1])
    square = []
    for j in range(r):
        square.append(infile.readline())
    for j in range(r):
        if failed:
            break
        for k in range(c):
            if failed:
                break
            current = square[j][k]
            if current == '.':
                continue
            x, y = j, k
            x += dir_dic[current][0]
            y += dir_dic[current][1]
            not_finish = True
            while 0 <= x < r and 0 <= y < c and not_finish:
                if square[x][y] != '.':
                    not_finish = False
                else:
                    x += dir_dic[current][0]
                    y += dir_dic[current][1]
            if not_finish:
                result += 1
                for dirs in dir_list:
                    if not_finish is False or dirs == current:
                        continue
                    x, y = j, k
                    x += dir_dic[dirs][0]
                    y += dir_dic[dirs][1]
                    not_finish = True
                    while 0 <= x < r and 0 <= y < c and not_finish:
                        if square[x][y] != '.':
                            not_finish = False
                        else:
                            x += dir_dic[dirs][0]
                            y += dir_dic[dirs][1]
            if not_finish:
                failed = True
    if failed:
        result = "IMPOSSIBLE"
    outfile.write("Case #" + str(i + 1) + ": " + str(result) + '\n')
outfile.close()
infile.close()

DEBUG = True
# DEBUG = False


# if DEBUG is True:
#     debug = print
# else:
#     debug =


def flip(pancakes, start, k):
    for i in range(k):
        if pancakes[start+i] is False:
            pancakes[start+i] = True
        else:
            pancakes[start+i] = False


def check(pancakes):
    for i in pancakes:
        if(i is False):
            return False
    return True


def initial_cake(n,m):
    result = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp = tmp + ["."]
        result.append(tmp)
    return result
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems


def initial_visit(n,m):
    result = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp = tmp + ["."]
        result.append(tmp)
    return result


def check_down(cake, current_x, current_y, r):
    tmp_x = 0
    initial = "?"

    while(current_x+tmp_x < r and cake[current_x+tmp_x][current_y] == "?"):
        tmp_x += 1
    if current_x+tmp_x < r:
        initial = cake[current_x+tmp_x][current_y]
    if current_x+tmp_x < r:
        tmp_x += 1
    while(current_x+tmp_x < r and cake[current_x+tmp_x][current_y] == "?"):
        tmp_x += 1

    return (initial, tmp_x)


def check_right(cake, current_x, current_y, tmp_x, c):
    # print("check_right",cake, current_x, current_y, tmp_x, c)
    tmp_y = 0
    done = False
    while (not done) and current_y + tmp_y < c:
        # print(tmp_y)
        tmp_y += 1
        if current_y + tmp_y < c:
            for i in range(tmp_x):
                # print("now", cake[current_x+i][current_y+tmp_y])
                if cake[current_x+i][current_y+tmp_y] != "?":
                    done = True
        else:
            done = True
    return tmp_y


def put_initial(cake, visit, current_x, current_y, tmp_x, tmp_y, intial):
    # print("--!!", cake, visit, current_x, current_y, tmp_x, tmp_y, intial)
    try:
        for i in range(tmp_x):
            for j in range(tmp_y):
                cake[current_x+i][current_y+j] = initial
                visit[current_x+i][current_y+j] = "*"
    except:
        print("--", cake, visit, current_x, current_y, tmp_x, tmp_y, intial)
    return None


def where_to_start_next(visit, current_x, current_y, r, c):
    # print("start ", visit, current_x, current_y, r, c)
    done = False
    while not done:
        if current_x == r:
            current_x = 0
            current_y += 1
        elif current_x > r or current_y > c:
            print("-----------------really?")
        else:
            if(current_y == c):
                done = True
            elif(visit[current_x][current_y] == "."):
                done = True
            else:
                while(current_x < r and visit[current_x][current_y] == "*"):
                    current_x += 1

    new_x = current_x
    new_y = current_y
    # print("end ", new_x, new_y)
    return (new_x, new_y)


t = int(input())  # read a line with a single integer

# down then right
for i in range(1, t + 1):
    # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    line = input()
    r, c = line.split(" ")

    r = int(r)
    c = int(c)
    cake = initial_cake(r,c)
    visit = initial_visit(r,c)
    for j in range(r):
        row = input()
        # print(row)
        for jj in range(len(row)):
            cake[j][jj] = row[jj]
    # print(cake)
    finish = False
    current_x = 0
    current_y = 0
    # print(cake[0][1])
    while not finish:
        initial = "?"
        this_tmp_y = current_y
        while initial == "?":
            initial, tmp_x = check_down(cake, current_x, this_tmp_y, r)
            this_tmp_y += 1
        tmp_y = check_right(cake, current_x, current_y, tmp_x, c)
        # print("tmp_y ", tmp_y)
        put_initial(cake, visit, current_x, current_y, tmp_x, tmp_y, initial)
        # print(current_x, current_y, tmp_x, tmp_y)
        current_x += tmp_x
        current_x, current_y = where_to_start_next(visit, current_x, current_y, r, c)
        # print(initial, tmp_x, tmp_y, current_x, current_y)
        if current_y == c:
            finish = True
            print("Case #{}:".format(i))
            for ii in range(r):
                for jj in range(c):
                    print(cake[ii][jj], end="")
                print()
        # finish = True
        # go down



    # if(check(pancakes)):
    #     print("Case #{}:".format(i),count)
    # else:
    #     print("Case #{}:".format(i),"IMPOSSIBLE")
    # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

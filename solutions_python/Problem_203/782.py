import copy

def find_chars(cake):
    chars = []
    for i, row in enumerate(cake):
        for j, char in enumerate(row):
            if char != '?':
                chars.append([char, [i, j], [i, j]])
    return chars

def f(r, c, cake):
    chars = find_chars(cake)
    return bfs(cake, chars)

def test_cake(cake):
    for row in cake:
        if '?' in row:
            return False
    return True
    # test if the cake is full

def bfs(cake, chars):
    # print('starting bfs with cake')
    # for row in cake:
        # print(row)
    # print('')
    if test_cake(cake):
        return cake
    for i in range(len(chars)):
        # print('considering %s' % chars[i])
        # extend up
        new_chars = copy.deepcopy(chars)
        new_cake = copy.deepcopy(cake)
        if new_chars[i][1][0] != 0:
            new_chars[i][1][0] -= 1
            issue = False
            for a in range(new_chars[i][1][1], new_chars[i][2][1]+1):
                if new_cake[new_chars[i][1][0]][a] == '?':
                    new_cake[new_chars[i][1][0]][a] = new_chars[i][0]
                else:
                    issue = True
                    continue
            if not issue:
                # print("extend %s up" % new_chars[i][0])
                tmp = bfs(new_cake, new_chars)
                if tmp:
                    return tmp

        # extend down
        new_chars = copy.deepcopy(chars)
        new_cake = copy.deepcopy(cake)
        if new_chars[i][2][0] != len(cake)-1:
            new_chars[i][2][0] += 1
            issue = False
            for a in range(new_chars[i][1][1], new_chars[i][2][1]+1):
                if new_cake[new_chars[i][2][0]][a] == '?':
                    new_cake[new_chars[i][2][0]][a] = new_chars[i][0]
                else:
                    issue = True
                    break
            if not issue:
                # print("extend %s down" % new_chars[i][0])
                tmp = bfs(new_cake, new_chars)
                if tmp:
                    return tmp

        # extend left
        new_chars = copy.deepcopy(chars)
        new_cake = copy.deepcopy(cake)
        if new_chars[i][1][1] != 0:
            new_chars[i][1][1] -= 1
            issue = False
            for a in range(new_chars[i][1][0], new_chars[i][2][0]+1):
                if new_cake[a][new_chars[i][1][1]] == '?':
                    new_cake[a][new_chars[i][1][1]] = new_chars[i][0]
                else:
                    issue = True
                    break
            if not issue:
                # print("extend %s left" % new_chars[i][0])
                tmp = bfs(new_cake, new_chars)
                if tmp:
                    return tmp

        # extend right
        new_chars = copy.deepcopy(chars)
        new_cake = copy.deepcopy(cake)
        if new_chars[i][2][1] != len(cake[0])-1:
            new_chars[i][2][1] += 1
            issue = False
            for a in range(new_chars[i][1][0], new_chars[i][2][0]+1):
                if new_cake[a][new_chars[i][2][1]] == '?':
                    new_cake[a][new_chars[i][2][1]] = new_chars[i][0]
                else:
                    issue = True
                    break
            if not issue:
                # print("extend %s right" % new_chars[i][0])
                tmp = bfs(new_cake, new_chars)
                if tmp:
                    return tmp
        # print("finished considering %s" % chars[i])
    return None




if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        cake = []
        r, c = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        for j in range(r):
            cake.append([s for s in raw_input()])
        res = f(r, c, cake)
        print "Case #{}:".format(i)
        for line in res:
            print("".join(line))
        # check out .format's specification for more formatting options
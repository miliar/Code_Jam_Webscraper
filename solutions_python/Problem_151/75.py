T = int(input())
test = 1

number = 0

count = 0


def trie(string):
    ret = set()
    for i in range(1, len(string)+1):
        ret.add(string[:i])
    return ret


def total_trie(strings):
    the_set = set()
    for str in strings:
        the_set = the_set.union(trie(str))
    return len(the_set) + 1


def split_nodes(splited, nodes):
    if len(nodes) == 0:
        ss = 0
        for strings in splited:
            if len(strings) == 0:
                return
            ss += total_trie(strings)
        #print(ss)
        global number, count
        if ss > number:
            count = 1
            number = ss
        elif ss == number:
            count += 1
        return
    global N
    for i in range(N):
        splited[i].append(nodes[0])
        split_nodes(splited, nodes[1:])
        splited[i].remove(nodes[0])



while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1
    line = input().split()
    M = int(line[0])
    N = int(line[1])
    nodes = []
    for i in range(M):
        nodes.append(input())
    # print(nodes)
    number = 0
    count = 0
    split_nodes([[] for i in range(N)], nodes)
    print(number, count)
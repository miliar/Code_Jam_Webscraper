def flipCharFromIndexWithCount(s, index, count):
    s_list = list(s)
    for i in xrange(index, index + count):
        s_list[i] = "+" if s_list[i] == "-" else "-"
    return "".join(s_list)

def searchTree(s, start_index, count, target, level):
    if s == target:
        return level
    if start_index == len(s) - count + 1:
        return None
    for i in xrange(start_index, len(s) - count + 1):
        current_s = flipCharFromIndexWithCount(s, i, count)
        result = searchTree(current_s, i + 1, count, target, level + 1)
        if result != None:
            return result
    if level == 0:
        return "IMPOSSIBLE"
    else:
        return None

t = int(raw_input())
for i in xrange(1, t + 1):
    current_input = raw_input().split(" ")
    target = current_input[0]
    s = "+" * len(target)
    count = int(current_input[1])
    print "Case #{}: {}".format(i, searchTree(s, 0, count, target, 0))

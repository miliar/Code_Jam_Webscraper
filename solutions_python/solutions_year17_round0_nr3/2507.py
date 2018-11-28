"""
there's n stalls, the left most and rightmost are occupied
you get L and R for each stall, which is the number of empty stalls left and right of that stall
then they get the min(L,R) of those stalls and choose the one that has the highest number
if there's a tie they get max(L,R) and choose the biggest, if there's a tie just pick the leftmost

[0,2,0,1,0,3,4,0,]
6, 2
[0,0][0,0,0]
10, 3
[(0,0),(0,0),(0,0),(0,0),(4,4),(0,0),(0,0),(0,0),(0,0),(0,0)]
[(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(2,2),(0,0),(0,0)]
[(0,0),(1,2),(0,0),(0,0)],[(0,0),(0,0)],[(0,0),(0,0)]


"""

def pick_stall(stalls, people):
    stall_list = []
    stall = []
    for i in range(stalls):
        stall.append((0,0))
    stall_list.append(stall)
    for i in range(people):
        #divide the list and update it n times
        list_index = get_longest_list(stall_list)
        l,r = bisect_list(stall_list,list_index)
        divided_list = split_list(stall_list,list_index)
        del stall_list[list_index]
        stall_list.insert(list_index, divided_list[0])
        stall_list.insert(list_index + 1, divided_list[1])
    return (max(l,r), min(l,r))

def split_list(stall_list,list_index):
    x = stall_list[list_index]
    ln = len(x)
    if len == 1:
        return x
    point = (ln - 1) / 2
    return (x[0:point],x[point + 1:])


def get_longest_list(stall_list):
    ln = len(stall_list)
    max_index = 0
    max_ln = 0
    for i in range(ln):
        curr_ln = len(stall_list[i])
        if curr_ln > max_ln:
            max_ln = curr_ln
            max_index = i
    return max_index

def bisect_list(stall_list, list_index):
    lst = stall_list[list_index]
    l,r = 0,0
    ln = len(lst)
    point = (ln - 1) / 2
    for i in range(ln):
        if i == point:
            continue
        elif i > point:
            r += 1
        else:
            l += 1
    return (l,r)

#main
t = int(raw_input())
for i in range(t):
    str_val = raw_input().split(' ')
    stalls,people = int(str_val[0]), int(str_val[1])
    x,y = pick_stall(stalls,people)
    answer = "Case #" + str(i + 1) + ": " + str(x) + " " + str(y)
    print answer

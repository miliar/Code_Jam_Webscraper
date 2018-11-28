def read_mapped(func=lambda x:x):
    return map(func, raw_input().split(" "))
def read_array(N, func):
    l = []
    for i in range(N):
        l.append(func(raw_input()))
    return l
def read_int():
    return int(raw_input())
def read_str():
    return raw_input()
def read_float():
    return float(raw_input())

T = read_int()

for case in range(T):
    a1 = read_int()
    for i in range(4):
        _ = raw_input()
        if i==a1-1:
            row1 = map(int, _.split(" "))
    a2 = read_int()
    for i in range(4):
        _ = raw_input()
        if i==a2-1:
            row2 = map(int, _.split(" "))
    inter = list(set(row1).intersection(set(row2)))
    if len(inter)==1:
        res = inter[0]
    elif len(inter)>1:
        res = "Bad magician!"
    else:
        res = "Volunteer cheated!"
    print "Case #{}: {}".format(case+1, res)

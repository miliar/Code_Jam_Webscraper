def load_mat():
    return [raw_input().strip().split() for _ in range(4)]

for idx in range(1, input()+1):
    n1 = input()
    r1 = set(load_mat()[n1-1])
    n2 = input()
    r2 = set(load_mat()[n2-1])
    inter = r1.intersection(r2)
    if len(inter)==1:
        print('Case #%d: %s' % (idx, inter.pop()))
    elif len(inter)>1:
        print('Case #%d: Bad magician!' % idx)
    else:
        print('Case #%d: Volunteer cheated!' % idx)

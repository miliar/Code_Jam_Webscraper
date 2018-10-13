

with open("A-small-attempt0.in", 'r') as f:
    a = f.readlines()

with open("a-small.out", 'w') as f:
    T = int(a[0])
    for i in range(T):
        ans1 = int(a[10*i+1])
        ans2 = int(a[10*i+6])
        cards1 = [map(int, e.strip().split(' ')) for e in a[10*i+2:10*i+6]]
        cards2 = [map(int, e.strip().split(' ')) for e in a[10*i+7:10*i+11]]
        inter = set(cards1[ans1-1]).intersection(set(cards2[ans2-1]))
        print inter
        if len(inter) == 0:
            result = "Volunteer cheated!"
        elif len(inter) > 1:
            result = "Bad magician!"
        else:
            result = str(list(inter)[0])        
        f.write("Case #{0}: {1}\n".format(i+1, result))

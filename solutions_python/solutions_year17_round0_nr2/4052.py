def is_tidy(d):
    return sorted(d) == d

with open("B-small-attempt1.in") as f:
    data = [each.strip() for each in f.readlines()]
    #print data

    T = data[0]
    out_data = []
    for index, i in enumerate(data[1:]):
        N = int(i)
        #for i in range(0,T):
        #N = map(int, raw_input().split())[0]
        while not is_tidy(map(int, str(N))):
            N -= 1
        out_data.append('Case #{0}: {1}'.format(index+1, N))
    with open('out.in', 'w') as w:
        w.write("\n".join(out_data))


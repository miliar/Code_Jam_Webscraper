def load(queue, capacity, amount=0):
    for position, group_size in enumerate(queue):
        amount, old_amount = amount + group_size, amount
        if amount > capacity:
            amount = old_amount
            break
    return (queue[position:]+queue[:position], amount)

def main():
    with open('test.in','r') as f:
        line, outputs = f.readline(), []
        for x, line in enumerate(f):
            x += 1
            if x % 2 is 1:
                l = line.split()
                r, k = int(l[0]), int(l[1])
            if x % 2 is 0:
                q, total = map(int, line.split()), 0
                for round in xrange(r):
                    q, amount = load(q, k)
                    total += amount
                s = "Case #{0}: {1}".format(x/2, total)
                outputs.append(s)
    with open('test.out','w') as g:
        g.write('\n'.join(outputs))

if __name__ =='__main__':
    main()

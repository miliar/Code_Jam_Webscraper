# -*- coding: utf-8 -*-
def A(size, motes):
    motes.sort()
    stack = [(size, motes, 0)]
    steps_l = []
    while stack != []:
        size, motes, steps = stack.pop()
        if motes == []:
            steps_l.append(steps)
            continue
        mote = motes[0]
        if mote < size:
            stack.append((size+mote, motes[1:], steps))
        else:
            if size != 1:
                stack.append((size + size - 1, motes, steps+1))
            stack.append((size, motes[1:], steps+1))
    return reduce(min, steps_l)

if __name__ == '__main__':
    N = int(raw_input())
    for i in xrange(N):
        [size, n] = map(int, raw_input().split())
        motes = map(int, raw_input().split())
        print('Case #{}: {}'.format(i+1, A(size, motes)))

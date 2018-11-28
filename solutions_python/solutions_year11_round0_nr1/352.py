#!/usr/bin/python3


def populate(o, b, case):
    i = 1
    size = len(case)
    queue_o = True
    while i < size:
        robot = case[i]
        button = int(case[i+1])
        i += 2
        if queue_o:
            if robot == 'O':
                o.append(button)
            else:
                o.append(None)
                i -= 2
        else:
            if robot == 'B':
                b.append(button)
            else:
                b.append(None)
                i -= 2
        queue_o = not queue_o

def get_first(queue):
    for each in queue:
        if each:
            return each 
    return None

def calc(case):
    o_q = []
    b_q = []
    populate(o_q,b_q,case)
    po = pb = 1
    t = 0
    o = get_first(o_q)
    b = get_first(b_q)
    next_is_o = True
    while o_q or b_q:
        if next_is_o and o == None:
            next_is_o = False
            o_q = []
            continue
        if not next_is_o and b == None:
            next_is_o = True
            b_q = []
            continue
        if next_is_o and not o_q[0]:
            next_is_o = False
            o_q.pop(0)
        if not next_is_o and not b_q[0]:
            next_is_o = True
            b_q.pop(0)
        # WALK OR PRESS
        if next_is_o and po == o: # PRESS O
            o_q.pop(0)
            next_is_o = False
            if b and b != pb:
                pb += 1 if pb < b else -1
            t += 1
        elif not next_is_o and pb == b: # PRESS B
            b_q.pop(0)
            next_is_o = True
            if o and o != po:
                po += 1 if po < o else -1
            t += 1
        else: # WALK
            if o and next_is_o:
                max_walk = abs(o-po)
                po +=  max_walk if po < o else -max_walk
                if b:
                    need_walk = abs(b-pb)
                    if need_walk < max_walk:
                        walk = need_walk
                    else:
                        walk = max_walk
                    pb += walk if pb < b else -walk
            else:
                max_walk = abs(b-pb)
                pb +=  max_walk if pb < b else -max_walk
                if o:
                    need_walk = abs(o-po)
                    if need_walk < max_walk:
                        walk = need_walk
                    else:
                        walk = max_walk
                    po += walk if po < o else -walk
            t += max_walk
        o = get_first(o_q)
        b = get_first(b_q)
    return t

def main():
    cases = int(input())
    case = True
    for i in range(cases):
        case = input()
        print('Case #{0}:'.format(i+1), end=' ')
        print(calc(case.split()))
    

if __name__ == '__main__':
    main()

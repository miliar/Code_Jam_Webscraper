#!/usr/bin/python
import re
import inspect
from sys import argv, exit

def rstr():
    return input()

def rstrs(splitchar=' '):
    return [i for i in input().split(splitchar)]

def rint():
    return int(input())

def rints(splitchar=' '):
    return [int(i) for i in rstrs(splitchar)]

def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]

def pvar(var, override=False):
    prnt(varnames(var), var)

def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)

# Faster IO
pq = []
def penq(s):
    if not isinstance(s, str):
        s = str(s)
    pq.append(s)

def pdump():
    s = ('\n'.join(pq)).encode()
    os.write(1, s)

class Horse:
    def __init__(self, *args):
        self.pos = args[0]
        self.vel = args[1]

    def __str__(self):
        return 'p{}|v{}'.format(self.pos, self.vel)

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    T = rint()
    for seq in range(1,T+1):
        D, H = rints()
        prnt(D, H)
        horses = [Horse(*rints()) for h in range(H)]
        mp = 0
        horses = sorted(horses, key=lambda h: h.pos)
        prnt('horses', horses)

        to_remove = []
        for i,horse in enumerate(horses):
            next_horse = horses[i+1] if i+1 < len(horses) else None
            if next_horse:
                if next_horse.vel >= horse.vel:
                    to_remove.append(next_horse)

        horses = [h for h in horses if h not in to_remove]
        prnt('valid', horses)

            
        ti = 0
        if len(horses) == 1:
            horse = horses[0]
            delta_p = D - horse.pos
            delta_t = delta_p / horse.vel
            ti = delta_t
        else:
            pos = horses[0].pos
            for i,horse in enumerate(horses):
                next_horse = None
                next_horse = horses[i+1] if i+1 < len(horses) else None
                if next_horse:
                    prnt('nh', next_horse)
                    delta = next_horse.pos - pos
                    delta_v = horse.vel - next_horse.vel
                    delta_t = delta / delta_v
                    delta_p = horse.vel * delta_t
                    prnt(delta, delta_v, delta_t, delta_p)
                    if pos + delta_p > D:
                        delta_p = D - pos
                        delta_t = delta_p / horse.vel
                        ti += delta_t
                        prnt('Traveling at {} for {} hours, {} dist'.format(horse.vel, delta_t, delta_p))
                        break
                    else:
                        prnt('Traveling at {} for {} hours, {} dist'.format(horse.vel, delta_t, delta_p))
                        pos += delta_p
                        ti += delta_t
                        prnt('Pos: {}'.format(pos))
                        for adjh in horses[i:]:
                            prnt('adjusting')
                            adjh.pos = adjh.pos + adjh.vel * delta_t
                else:
                    prnt('else')
                    delta_p = D - horse.pos
                    delta_t = delta_p / horse.vel
                    ti += delta_t
                    prnt('Traveling at {} for {} hours, {} dist'.format(horse.vel, delta_t, delta_p))
                

        prnt(D, ti)
        ans = D/ti if ti != 0 else 6
        print('Case #{}: {}'.format(seq, ans))
        prnt('\n')

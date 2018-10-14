from threading import currentThread

class TailRecursiveCall(Exception):
    pass

class Rec_f(object):
    def __init__(self, func):
        self.tr_d = {}
        self.func = func

    def __call__(self, *args, **kw):
        self.args = args
        self.kw = kw
        thread = currentThread()
        if thread not in self.tr_d:
            self.tr_d[thread] = {}
            self.tr_d[thread]["depth"] = 0
        self.tr_d[thread]["depth"] += 1
        # Record the arguments passed to function on this thread
        self.tr_d[thread]["args"] = args
        self.tr_d[thread]["kw"] = kw
        depth =  self.tr_d[thread]["depth"]
        # If we are re-entering the same function on the same thread:
        if depth > 1:
            # Effectively detours execution to the "Landing Point",
            # but two execution frames above the current one:
            raise TailRecursiveCall
        over = False
        while not over:
            over = True
            args = self.tr_d[thread]["args"]
            kw = self.tr_d[thread]["kw"]
            try:
                # Execute the function with the latest arguments for this thread.
                result = self.func(*args, **kw)
            except TailRecursiveCall:
                # Landing point if the function tried to recurse itself.
                # Two execution frames above.
                self.tr_d[thread]["depth"] -= 1
                over = False
        self.tr_d[thread]["depth"] -= 1
        return result

def tailrecursive(func):
    return Rec_f(func)



import itertools
import numpy

fn = '/Users/vivanov/Downloads/A-small-attempt1.in'


with open(fn) as f:
    lines = f.read().splitlines()[1:]
    l = []
    i = 0
    while i < len(lines):
        ans1 = [int(k) for k in lines[i].split(' ')][0] - 1
        i += 1
        a = []
        for j in range(4):
            a.append([int(k) for k in lines[i].split(' ')])
            i += 1
        a1 = numpy.array(a)

        ans2 = [int(k) for k in lines[i].split(' ')][0] - 1
        i += 1
        a = []
        for j in range(4):
            a.append([int(k) for k in lines[i].split(' ')])
            i += 1
        a2 = numpy.array(a)
        l.append({ 'ans1' : ans1, 'a1': a1 , 'ans2' : ans2, 'a2': a2})

pass


def search(state):
    a1 = state['a1']
    a2 = state['a2']
    ans1 = state['ans1']
    ans2 = state['ans2']
    equals = []
    res = ''
    for i in a1[ans1]:
        for j in a2[ans2]:
            if i == j:
                equals.append(i)
    if len(equals) == 1:
        res = str(equals[0])
    elif len(equals) > 1:
        res = 'Bad magician!'
    else :
        res = 'Volunteer cheated!'
    return res

with open('out', 'w') as f :
    to_write = []
    for i in range(len(l)):
        to_write.append('Case #%s: %s \n' %((i+1), search(l[i])))
    f.writelines(to_write)






#!/usr/bin/env python
#-*- coding:utf-8 -*-

def test(E, p):
    for e in E:
        if e >= p:
            return True
    return False 

def update(f, p):
    for a in f:
        for b in f:
            if a != b and test(a.intersection(b), p):
                f.remove(a)
                f.remove(b)
                f.append(a.union(b))
                return f
    return None

def update2(f, p):
    for i in range(len(f)):
        for j in range(i+1, len(f)):
            if j >= len(f):
                break
            
            while j < len(f) and test(f[i].intersection(f[j]), p):
                f[i] = f[i].union(f.pop(j))
                
        for j in range(i+1, len(f)):
            if j >= len(f):
                break
            
            while j < len(f) and test(f[i].intersection(f[j]), p):
                f[i] = f[i].union(f.pop(j))
        
    return f


def result(a, b, p):
    f = [set(prime_factors(i)) for i in range(a, b+1)]
    f = update2(f, p)
    return len(f)


if __name__ == '__main__':
    from sys import argv
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:].__iter__()
    
    for n in range(nb_inputs):
        inputs = map(int, lines.next().split(' '))
        print 'Case #%s:' % (n+1), result(*inputs)


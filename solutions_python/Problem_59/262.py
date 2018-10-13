#!/usr/bin/env python



if __name__ == '__main__':
    test_cases = int(raw_input())
    
    for case in xrange(1, test_cases+1):
        n, m = map(int, raw_input().split(' '))
        root_dir = {}
        dirs = []
        for i in xrange(n):
            dirs.append(raw_input())
        dirs.sort()
        for dir in dirs:
            path = dir[1:].split('/')
            aux_dir = root_dir
            for p in path:
                if not aux_dir.has_key(p):
                    aux_dir[p] = {}
                aux_dir = aux_dir[p]
        new_dirs = []
        for i in xrange(m):
            new_dirs.append(raw_input())
        
        result = 0
        for new_dir in new_dirs:
            path = new_dir[1:].split('/')
            aux_dir = root_dir
            for p in path:
                if not aux_dir.has_key(p):
                    result += 1
                    aux_dir[p] = {}
                aux_dir = aux_dir[p]
        
        print "Case #%d: %d" % (case, result)

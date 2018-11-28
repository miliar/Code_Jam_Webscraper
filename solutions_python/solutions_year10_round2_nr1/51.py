#!/usr/bin/env python

DEBUG = 0

def main():
    T = int(raw_input().strip())

    for t in range(T):
        n_to_create = 0

        N, M = [int(x) for x in raw_input().split()]

        existing = {}

        def split_path(path):
            bits = path.lstrip("/").split("/")
            if DEBUG: print "split:",bits
            return bits

        def add_path(path, root):
            bits = split_path(path)
            node = root
            n_created = 0
            for bit in bits:
                child = node.get(bit)
                if child is None:
                    n_created += 1
                    if DEBUG: print "\tcreated %s" % bit
                    child = node[bit] = {}
                node = child
            if DEBUG: print "\tafter add_path:",root
            return n_created

        for n in range(N):
            path = raw_input().strip()
            add_path(path, existing)
        
        if DEBUG: print "--- actual now ---"
        for m in range(M):
            path = raw_input().strip()
            n_to_create += add_path(path, existing)
        
        print "Case #%d: %d" % (t+1, n_to_create)

main()

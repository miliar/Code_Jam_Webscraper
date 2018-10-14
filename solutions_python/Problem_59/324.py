#-*- coding: utf-8 -*-

T = int(raw_input())


class FileSystem(object):
    def __init__(self):
        self.root = {}

    def add(self, path):

        try:
            new, rest = path.split("/", 1)
        except:
            new = path
            rest = ''

        created = 0
        if not new in self.root:
            self.root[new] = FileSystem()
            created = 1
        if rest:
            return created + self.root[new].add(rest)
        else:
            return created

    def __str__(self):
        print self.root.keys()
        for i in self.root.values():
            print i
            
for case in range(1, T+1):
    dirs = FileSystem()
    added_paths = {}
    N, M = raw_input().split()
    N, M = int(N), int(M)

    for i in range(N):
        path = raw_input()
        added_paths[path] = True

        dirs.add(path.lstrip("/"))

    counter = 0
    for i in range(M):
        path = raw_input()

        if path in added_paths:
            continue

        counter += dirs.add(path.lstrip("/"))
        added_paths[path] = True

    print "Case #%s: %s" % (case, counter)

        
        

#! /usr/bin/env python

import sys

f = file(sys.argv[1])
lines = [ln.strip() for ln in f.readlines()]
T = int(lines[0])
print('%s contains %i (T) test cases' % (sys.argv[1],T))

cases = []
ind = 1
for i in range(T):
    #print(lines[ind], lines[ind].split(' '))
    n,m = [int(k) for k in lines[ind].split(' ')]
    #print(n,m)
    ind = ind + 1
    dirsExisting = lines[ind:ind+n]
    ind = ind + n
    dirsToBeCreated = lines[ind:ind+m]
    ind = ind + m
    cases.append([dirsExisting, dirsToBeCreated])
print(cases)

class directoryNode:
    def __init__(self, name, parent, level):
        self.name = name
        self.parent = parent
        self.level = level
        self.folders = []
    def has_folder(self, fname):
        return any([folder.name == fname for folder in self.folders])
    def create_folder(self, fname):
        self.folders.append(directoryNode(fname,self,self.level+1))
    def get_folder(self, fname):
        return self.folders[[folder.name == fname for folder in self.folders].index(True)]
    def __repr__(self):
        return repr(self.parent) + '/' + self.name

def directoryProblem(iDirs, mDirs):
    directoryRoot = directoryNode('',None,0)
    def mkdirs(dirsClean):
        creations = 0
        currentDir = directoryRoot
        dirs = sorted(dirsClean)
        currentFolders = []
        for d in dirs:
            folders = d.split('/')[1:]
            #print('d,folders',d,folders)
            j = 0 
            while j < min(len(folders),len(currentFolders)) and folders[j] == currentFolders[j]:
                j = j + 1
            # rolling back required dirs
            while len(currentFolders) > j:
                currentDir = currentDir.parent
                del currentFolders[-1]
            #print('currentDir, currentFolders',currentDir, currentFolders)
            for fold in folders[j:]:
                if not currentDir.has_folder(fold):
                    currentDir.create_folder(fold)
                    creations = creations + 1
                currentDir = currentDir.get_folder(fold)
            currentFolders = folders
        return  creations
    c1 = mkdirs(iDirs)
    c2 = mkdirs(mDirs)
    return c2


results = []
for t in range(T):
    print('case %i of %i' % (t+1,T))
    print(cases[t])
    res = directoryProblem(*cases[t])
    results.append('Case #%i: %i' % (t+1,res))
    print(results[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(results))
f.close()

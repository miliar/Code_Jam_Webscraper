from time import time
import psyco
import re
import math
psyco.full()

fin = open("c1_input.txt","r")
fout = open("c1_output.txt","w")
cases = int(fin.readline())

def current_val(tree, index):
    if index >= (len(tree)-1)/2:
        return tree[index]
    
    
    if tree[index] == 1:
        if (current_val(tree,index*2+1) == 1 and current_val(tree,index*2+2) == 1):
            return 1
        else:
            return 0
    
    if tree[index] == 0:
        if (current_val(tree,index*2+1) == 1 or current_val(tree,index*2+2) == 1):
            return 1
        else:
            return 0

def get_min_changes(tree, changeable, subindex, desired_value):
    if current_val(tree,subindex) == desired_value:
        return 0
    
    if subindex >= (len(tree)-1)/2:
        return 100000000
    
    if subindex in changeable:
        newtree = tree[:]
        newtree[subindex] = 1 - newtree[subindex]
        if current_val(newtree,subindex) == desired_value:
            pass
        #    return 1
    
    min_change_left = [0,0]    
    min_change_right = [0,0] 
    min_change_left[0] = get_min_changes(tree, changeable, subindex*2+1, 0)
    min_change_left[1] = get_min_changes(tree, changeable, subindex*2+1, 1)
    min_change_right[0] = get_min_changes(tree, changeable, subindex*2+2, 0)
    min_change_right[1] = get_min_changes(tree, changeable, subindex*2+2, 1)
    
    or_min_changes = 0
    and_min_changes = 0
    if desired_value == 1:
        and_min_changes = min_change_right[1] + min_change_left[1]
    if desired_value == 0:
        and_min_changes = min([min_change_right[0] + min_change_left[1],
                              min_change_right[0] + min_change_left[0],
                              min_change_right[1] + min_change_left[0]])
    if desired_value == 1:
        or_min_changes = min([min_change_right[0] + min_change_left[1],
                              min_change_right[1] + min_change_left[1],
                              min_change_right[1] + min_change_left[0]])
    if desired_value == 0:
        or_min_changes = min_change_right[0] + min_change_left[0]
    
    print "node:", subindex,"desired:",desired_value,"or:", or_min_changes, and_min_changes,"change:", subindex in changeable
    if subindex in changeable and tree[subindex] == 1:
        return min(and_min_changes, or_min_changes + 1)
    
    if subindex in changeable and tree[subindex] == 0:
        return min(and_min_changes + 1, or_min_changes)
    
    if tree[subindex] == 1:
        return and_min_changes
    
    return or_min_changes
    
    

t0 = time()
for casenr in range(cases):
    (M,V) = map(int, [e for e in fin.readline().split()])
    tree = []
    changeable = []
    for nodenr in range(M):
        if (nodenr < (M-1)/2):
            (G,C) = map(int, [e for e in fin.readline().split()])
            tree.append(G)
            if C == 1:
                changeable.append(nodenr)
        else:
            value = int(fin.readline())
            tree.append(value)
    
    if (current_val(tree, 0) == V):
        fout.write("Case #%d: %d\n" % (casenr+1, 0))
    else:
    
        min_ch = get_min_changes(tree, changeable, 0, V)
        
        print min_ch
        if min_ch <= 10000:
            fout.write("Case #%d: %d\n" % (casenr+1, min_ch))
        else:
            fout.write("Case #%d: IMPOSSIBLE\n" % (casenr+1))
    print "Time elapsed: %f" % (time() - t0)
    
    
    
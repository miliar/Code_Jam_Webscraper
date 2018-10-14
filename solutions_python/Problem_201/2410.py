#!/usr/bin/python

from sys import stdin

def get_ls_rs(stalls, idx):
    Ls = stalls[idx] - stalls[idx-1] - 1
    Rs = stalls[idx+1] - stalls[idx] - 1
    return (Ls, Rs)

def nextstall(stalls):
    empty_stalls = [stalls[i+1]-stalls[i]-1 for i in range(len(stalls)-1)]
    max_stalls = max(empty_stalls)
    max_stalls_idx = empty_stalls.index(max_stalls) 
    stall = stalls[max_stalls_idx] + (max_stalls+1)/2
    stalls.insert(max_stalls_idx+1, stall)
    Ls, Rs = get_ls_rs(stalls, max_stalls_idx+1)
    return (max_stalls_idx, stall, Ls, Rs)

def laststall(n_stalls, n_people):
    stalls = [0, n_stalls+1];
    for p in range(n_people):
        stall_idx, stall, Ls, Rs = nextstall(stalls)
    return (Ls, Rs)


# main script
nb_tc = int(stdin.readline())
for i in range(nb_tc):
    n_stalls, n_people = stdin.readline().split()
    n_stalls = int(n_stalls)
    n_people = int(n_people)
    Ls, Rs = laststall(n_stalls, n_people)
    print "Case #" + str(i+1) + ": " + str(max(Ls,Rs)) + " " + str(min(Ls,Rs))


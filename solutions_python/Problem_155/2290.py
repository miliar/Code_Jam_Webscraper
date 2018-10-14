#!/usr/bin/python


def getInput(filename):
    input = {}
    fd = open(filename, "r")
    input['testcases'] = int(fd.next().rstrip())
    input['samples'] = [line.rstrip() for line in fd]
    return input

def totalPreviouslevels(level, shyness_map):
    alreadyLostShyness = 0
    for p in xrange(0, level):
        alreadyLostShyness += shyness_map[p]
    return alreadyLostShyness

def inviteFriends(s_max, shyness):
    numFriends = 0
    if not s_max:
        return (0)
    shyness_map = dict(enumerate(shyness))
    for level in xrange(1,s_max+1):
        lostShyness = totalPreviouslevels(level, shyness_map)
        if (lostShyness + numFriends) < level:
            numFriends += (level - (lostShyness + numFriends))
    return numFriends
        
input = getInput("sample.txt")
output = open("result.txt", "w")
current_case = 1
for sample in input['samples']:
    s_max,shyness = sample.split(' ')
    s_max = int(s_max)
    shyness = [int(x) for x in shyness]
    num_friends = 0
    num_friends = inviteFriends(s_max, shyness)
    output.write("Case #%d: %d\n" %(current_case, num_friends))
    print ("Case #%d: %d" %(current_case, num_friends))
    current_case += 1

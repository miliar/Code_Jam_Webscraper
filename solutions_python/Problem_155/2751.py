__author__ = 'alexey'
# https://code.google.com/codejam/contest/6224486/dashboard#s=p0

# fl = open('A-small-attempt0.in.txt')
fl = open('A-large.in.txt')
# fl = open('test.in.txt')

data = fl.readlines()

def calcFriends():
    clapping = people[0]
    friends = 0
    for j in range(1, maxS + 1):
        if people[j] <= 0:
            continue

        diff = j - clapping
        if diff > 0:
            friends += diff
            clapping += diff
        clapping += people[j]
    return friends

fl = open('output.txt', 'w')

for i in range(1, int(data[0]) + 1):
    input = data[i].split();
    maxS = int(input[0]);
    people = map( lambda k : int(k), list(input[1]) )
    # print("maxS %d, people %s" % (maxS, people))
    fl.write("Case #%d: %d\n" % (i, calcFriends()))

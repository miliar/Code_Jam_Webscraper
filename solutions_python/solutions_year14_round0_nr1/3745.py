#!/usr/bin/env python

f = open('magictrick.txt')
lines = f.read()
lines = lines.split('\n')

cases = lines[0]
c = 0
while c < int(cases):
    row1 = 1 + 10*c
    row2 = 6 + 10*c
    cards1 = lines[row1 + int(lines[row1])].split(' ')
    cards2 = lines[row2 + int(lines[row2])].split(' ')
    matches = set(cards1) & set(cards2)
    if len(matches) == 1:
        print("Case #" + str(c+1) + ': ' + list(matches)[0])
    elif len(matches) > 1:
        print("Case #" + str(c+1) + ": " + "Bad magician!")
    else:
        print("Case #" + str(c+1) + ": " +"Volunteer cheated!")
    c = c + 1
f.close()

inp = open("A-large.in", "r")
out = open("out", 'w')

# needed
# standing
# invited
# needed = shyness * number of audience with this shyness level - standing
# standing = number of audience with needs sufficed
# invited = need - standing

T = int(inp.readline())
for i in range(1, T+1):
    invited = 0
    standing = 0
    s = inp.readline().rstrip("\n\r").split()
    n = int(s[0])
    s = s[1]
    # s = 11111 or the number of shyness levels of audience
    for level in range(n+1):
        numofpeople = int(s[level])
        need = level  * numofpeople
        if standing >= level and numofpeople > 0:
            standing += numofpeople
        elif standing < level and numofpeople > 0:
            invitedneeded = level - standing
            invited += invitedneeded
            standing += invitedneeded + numofpeople
    out.write("Case #{0}: {1}\n".format(i, invited))

inp.close()
out.close()
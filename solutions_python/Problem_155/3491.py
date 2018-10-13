def calculate(audience):
    friends = 0
    standing_so_far = 0
    for i in range(len(audience)):
        new_friends = 0
#         print "i: ", i
#         print friends + standing_so_far
        if (friends + standing_so_far < i) and audience[i]>0:
            new_friends = i - friends - standing_so_far
        standing_so_far += audience[i] + new_friends
        friends += new_friends
#         print "new friends: ", new_friends
    return friends

    output = ""

with open('A-small-attempt0.in') as f:
    cases = f.readline()
    for i in range(int(cases)):
        line = f.readline()
        max_shyness = line.split()[0]
        audience = [int(x) for x in line.split()[1]]
        output += "Case #{0}: {1}\n".format(i+1,calculate(audience))

with open('A-small-attempt0_output.in','w') as f:
    f.write(output)
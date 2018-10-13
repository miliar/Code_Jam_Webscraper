import sys

with open(sys.argv[1]) as f:
    inputs = f.read().splitlines()

T = int(inputs[0])

out = open("A-large.out", "w")

for i in range(1, T + 1):
    audience = inputs[i].split(" ")[1:][0]

    members_standing = 0
    required_friends = 0

    for j in range(0, len(audience)):
        if members_standing + required_friends >= j and int(audience[j]) != 0:
            members_standing += int(audience[j])
        else:
            if int(audience[j]) != 0:
                while (members_standing + required_friends < j):
                    required_friends += 1
                members_standing += int(audience[j])

    out.write("Case #" + str(i) + ": " + str(required_friends) + "\n")

out.close()

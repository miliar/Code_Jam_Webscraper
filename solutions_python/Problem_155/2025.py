
n = int(input())
out = open("a-large-out.txt", "w")

for i in range(n):
    line = str(input()).split(' ')
    max_shy = line[0]
    audience = list(line[1])
    #print("Case #{0}: max:{1} audience: {2}".format(i+1, max_shy, audience))

    invite = 0
    standing = 0
    for j in range(int(max_shy)):
        standing += int(audience[j])
        if standing < j+1:
            diff = j+1 - standing
            invite += diff
            standing += diff

    #print("Case #{0}: {1}".format(i+1, invite))
    out.write("Case #{0}: {1}\n".format(i+1, invite))

print("done")
out.close()

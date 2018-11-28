#!python3
with open("p1large.in", 'r') as input, open("p1largeo.txt", 'w') as output:
    T = int(input.readline())
    standing = 0
    friends = 0
    audience = ''
    for t in range(1, T+1):
        standing = 0
        friends = 0
        audience = input.readline().split()[1]
        for shyness, people in enumerate(audience):
            if shyness > standing:
                friends += shyness - standing
                standing += shyness - standing
            standing += int(people)
        output.write("Case #{0}: {1}\n".format(t, friends))
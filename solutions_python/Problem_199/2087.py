def minimumFlips(faces, flipperWidth):
    count = 0
    for bit in range(0, len(faces) - flipperWidth + 1):
        if faces[bit] == 0:
            count += 1
            for pos in range(0,flipperWidth):
                faces[bit + pos] = faces[bit + pos] ^ 1
    for bit in range(len(faces) - flipperWidth, len(faces)):
        if faces[bit] == 0:
            return "IMPOSSIBLE"
    return count

with open('A-large.in', 'r') as f:
    caseCounter = 0
    for line in f:
        if caseCounter != 0:
            inputs = line.split(" ")
            faces = list(map(lambda l: 1 if l == '+' else 0, inputs[0]))
            flipperWidth = int(inputs[1])
            print("Case #" + str(caseCounter) + ": " + str(minimumFlips(faces, flipperWidth)))
        caseCounter += 1

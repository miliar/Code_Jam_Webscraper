t = int(input())
outputlist = []
for i in range(t):
    inline = input()
    inline = inline.split()
    d = int(inline[0])
    n = int(inline[1])

    maintime = 0
    for j in range(n):
        horse = input()
        horse = horse.split()
        time = (d-int(horse[0]))/int(horse[1])
        if time > maintime:
            maintime = time

    v = d/maintime
    outputlist.append('Case #' + str(i+1) + ': ' + str(v))

for i in range(t):
    print(outputlist[i])

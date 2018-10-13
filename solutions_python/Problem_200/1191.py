__author__ = 'ben'

lines = [line.rstrip('\n') for line in open('input')][1:]

outFile = open("output", "w")

def f(srep):
    srep = str(srep)
    print(srep)
    number = list(srep)
    dec = False
    for index, i in enumerate(srep):
        if dec:
            number[index] = "9"
        elif index and int(srep[index - 1]) > int(i):
            number[index] = "9"
            number[index - 1] = str(int(number[index - 1]) - 1)
            # print(len(srep)-index)
            dec = True
    return number

c = 1
for line in lines:
    t = f(line)
    while t != f("".join(t)):
        t = f("".join(t))
    outFile.write("Case #{}: {}\n".format(c, int("".join(t))))
    c += 1

outFile.close()

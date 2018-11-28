



def hits(text, letter):
    hits = []
    iter = 0

    try:
        while True:
            hit = text.index(letter, iter)
            hits.append(hit)
            iter = hit + 1
    except:
        return hits


def recursive(text, string):
    complete = 0
    if string != "":
        letter = string[0]
        for i in hits(text, letter):
            complete += recursive(text[i+1:], string[1:])
    else:
        complete += 1
    return complete






file = open("C-small.in")

output = ""

cases = int(file.readline())
for case in range(1, cases + 1):
    text = file.readline()
    result = recursive(text, "welcome to code jam")
    result = "0000" + str(result)
    output += "Case #%d: %s\n" %(case, result[-4:])

file.close()
file = open("C-small.out", 'w')
file.write(output)
file.close()







from collections import Counter

def analyse(string):

    print("")
    print(string)

    uniques = [("0","Z","ZERO"),
                ("2","W","TWO"),
                ("4","U","FOUR"),
                ("6","X","SIX"),
                ("8","G","EIGHT"),
                ("3","H","THREE"),
                ("5","F","FIVE"),
                ("1","O","ONE"),
                ("7","S","SEVEN"),
                ("9","I","NINE")]

    counts = Counter(string)

    answer = ""

    for digit, unique, word in uniques:
        answer += digit * counts[unique]

        print(digit, unique, word, counts)

        while counts[unique] != 0:
            counts.subtract(Counter(word))

    return ''.join(sorted(answer))

def run(name):
    lines = [l for l in open(name + ".in", mode='r')]
    n = int(lines[0])
    
    out = open(name + ".out",mode='w')
    for i, line in enumerate(lines[1:]):
        answer = analyse(line.rstrip())
        out.write("Case #" + str(i+1) + ": " + answer + "\n")
    out.close()

run("A-large")

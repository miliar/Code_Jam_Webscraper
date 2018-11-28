import sys
import os.path

def solve(line):
    # Parse input
    tokens = line.split(' ')
    
    combine = {}
    oppose = {}
    c = int(tokens[0])
    index = 1
    for i in range(index, c + index):
        combo = tokens[i]
        combine[combo[0] + combo[1]] = combo[2]
        combine[combo[1] + combo[0]] = combo[2]

    index += c
    d = int(tokens[index])
    index += 1
    for i in range(index, d + index):
        combo = tokens[i]
        oppose[combo[0]] = combo[1]
        oppose[combo[1]] = combo[0]

    index += d
    n = int(tokens[index])
    index += 1
    e_list = tokens[index]
    
    # Solve
    magick = []
    
    for i in range(n):
        # Check if the element can be combined.
        e = e_list[i]
        if len(magick) == 0:
            magick.append(e)
        else:
            # Check if it can be combined.
            e_last = magick[-1]
            combo = e_last + e
            if combo in combine:
                magick.pop()
                magick.append(combine[combo])
            elif e in oppose and oppose[e] in magick:
                magick = []
            else:
                magick.append(e)
    
    if len(magick) == 0:
        return "[]"

    magic_str = "["
    for i in range(len(magick)):
        e = magick[i]
        if i != len(magick) - 1:
            magic_str = "%s%s, " % (magic_str, e)
        else:
            magic_str = "%s%s]" % (magic_str, e)

    return magic_str

if __name__ == '__main__':
    input = sys.argv[1]

    output_counter = 0
    output = "output.txt"
    while os.path.isfile(output):
        output = "output%s.txt" % output_counter
        output_counter += 1

    infile = open(input, "r")
    outfile = open(output, "w")

    cases = int(infile.readline())
    for case in range(cases):
        line = infile.readline()
        answer = solve(line)
        print answer
        answer = "Case #%s: %s\n" % (case + 1, answer)
        outfile.write(answer)

    outfile.close()

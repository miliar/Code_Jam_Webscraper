
normal=list("abcdefghijklmnopqrstuvwxyz ")
xlate=("ynficwlbkuomxsevzpdrjgthaq ")

def translate(inputline):
    chars = list(inputline)
    translation = ""
    for c in chars:
        translation += normal[xlate.index(c)]
    return translation

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        filename = "input.in"
    else:
        filename = sys.argv[1]

    read_file = file(filename)
    file_contents = list(read_file.readlines())
    del file_contents[0] # skip first line of input since it's just the number of test cases
    counter = 1
    for line in file_contents:
        line = line[:-1]  # chop off end-of-line
        print "Case #" + str(counter) + ": " + translate(line)
        counter += 1


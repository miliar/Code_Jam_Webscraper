import sys

def main(input):
    f = open(input, 'rU')
    num_lines = int(f.readline())
    for i in range(num_lines):
        googlese = f.readline().strip()
        output = "".join(map(translate, googlese))
        print "Case #" + str(i+1) + ": " + output

def translate(char):
    if char in "ejp mysljylc kd kxveddknmc re jsicpdrysi":
        index = "ejp mysljylc kd kxveddknmc re jsicpdrysi".index(char)
        return "our language is impossible to understand"[index]
    if char in "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd":
        index = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd".index(char)
        return "there are twenty six factorial possibilities"[index]
    if char in "de kr kd eoya kw aej tysr re ujdr lkgc jv":
        index = "de kr kd eoya kw aej tysr re ujdr lkgc jv".index(char)
        return "so it is okay if you want to just give up"[index]
    if char == "z":
        return "q"
    if char == "o":
        return "e"
    if char == "a":
        return "y"
    return "z"

main(sys.argv[1])

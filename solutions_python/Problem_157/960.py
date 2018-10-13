file = open("C-small-attempt3.in", 'r')
file_contents = file.read()
file.close()

contents = file_contents.split("\n")
cases = int(contents[0])
contents = contents[1:(len(contents)-1)]
input_list = []

for i in range(len(contents))[::2]:
    input_list += [(contents[i], contents[i+1])]

def solve(lx, string):
    lx = lx.split()
    X = int(lx[1])
    string = string * X
    i = find_substring("i", string)
    if i is None:
        return False
    string = string[len(i):]
    j = find_substring("j", string)
    if j is None:
        return False
    string = string[len(j):]
    k = find_substring("k", string)
    if k is None:
        return False
    return True
        
def find_substring(letter, string):
    substring = string[0]
    current = string[0]
    if letter == "k":
        for i in range(1, len(string)):
            current = reduce(current, string[i])
            substring += string[i]
        if current == letter:
            return substring
        return None
    elif substring == letter:
        return substring
    for i in range(1, len(string)):
        current = reduce(current, string[i])
        substring += string[i]
        if current == letter:
            return substring

def reduce(x, y):
    if x == 'i':
        if y == 'i':
            return ("-1")
        if y == 'j':
            return ("k")
        if y == 'k':
            return ("-j")
        if y == '-i':
            return ("1")
        if y == '-j':
            return ("-k")
        if y == '-k':
            return ("j")
        if y == '1':
            return ("i")
        if y == '-1':
            return ("-i")
    if x == '-i':
        if y == 'i':
            return ("1")
        if y == 'j':
            return ("-k")
        if y == 'k':
            return ("j")
        if y == '-i':
            return ("-1")
        if y == '-j':
            return ("k")
        if y == '-k':
            return ("-j")
        if y == '1':
            return ("-i")
        if y == '-1':
            return ("i")
    if x == 'j':
        if y == 'i':
            return ("-k")
        if y == 'j':
            return ("-1")
        if y == 'k':
            return ("i")
        if y == '-i':
            return ("k")
        if y == '-j':
            return ("1")
        if y == '-k':
            return ("-i")
        if y == '1':
            return ("j")
        if y == '-1':
            return ("-j")
    if x == '-j':
        if y == 'i':
            return ("k")
        if y == 'j':
            return ("1")
        if y == 'k':
            return ("-i")
        if y == '-i':
            return ("-k")
        if y == '-j':
            return ("-1")
        if y == '-k':
            return ("i")
        if y == '1':
            return ("-j")
        if y == '-1':
            return ("j")
    if x == 'k':
        if y == 'i':
            return ("j")
        if y == 'j':
            return ("-i")
        if y == 'k':
            return ("-1")
        if y == '-i':
            return ("-j")
        if y == '-j':
            return ("i")
        if y == '-k':
            return ("1")
        if y == '1':
            return ("k")
        if y == '-1':
            return ("-k")
    if x == '-k':
        if y == 'i':
            return ("-j")
        if y == 'j':
            return ("i")
        if y == 'k':
            return ("1")
        if y == '-i':
            return ("j")
        if y == '-j':
            return ("-i")
        if y == '-k':
            return ("-1")
        if y == '1':
            return ("-k")
        if y == '-1':
            return ("k")
    if x == '1':
        if y == 'i':
            return ("i")
        if y == 'j':
            return ("j")
        if y == 'k':
            return ("k")
        if y == '-i':
            return ("-i")
        if y == '-j':
            return ("-j")
        if y == '-k':
            return ("-k")
        if y == '1':
            return ("1")
        if y == '-1':
            return ("-1")
    if x == '-1':
        if y == 'i':
            return ("-i")
        if y == 'j':
            return ("-j")
        if y == 'k':
            return ("-k")
        if y == '-i':
            return ("i")
        if y == '-j':
            return ("j")
        if y == '-k':
            return ("k")
        if y == '1':
            return ("-1")
        if y == '-1':
            return ("1")

for i in range(cases):
    ans = solve(input_list[i][0], input_list[i][1])
    if ans is True:
        print("Case #{}: YES".format(i+1))
    else:
        print("Case #{}: NO".format(i+1))


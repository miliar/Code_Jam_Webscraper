def read_file(filename):
    fp = open(filename)
    lines = fp.readlines()
    return lines


def welcome_finder(filename):
    lines = read_file(filename)
    n = int(lines[0])
    string = ""
    for i in range(n):
        num = string_finder(lines[i+1],"welcome to code jam")
        numstr = str(num + 10000)[1:]
        string = string + "Case #" + str(i+1) + ": " + numstr + "\n"
    return string

def string_finder(string, key):
    result = 0
    if len(string) == 0:
        return result
    if string[0] == key[0]:
        if len(key) == 1:
            result = 1 + string_finder(string[1:],key)
        else:
            result = string_finder(string[1:],key) + string_finder(string[1:],key[1:])
        return result % 10000
    else:
        return string_finder(string[1:],key)
    

def run(filename):
    a = open("output.txt","w")
    a.write(welcome_finder(filename))

run("C-small-attempt0.txt")

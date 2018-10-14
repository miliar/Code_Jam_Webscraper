from builtins import print

def is_sorted(lst, key = lambda x: x):
    for i,  el in enumerate(lst[1:]):
        if(key(el) < key(lst[i])):
            return  False
    return True

file = open("B-small-attempt0.in", "r")
out = open("out.txt", "w")
line_count = 0
for line in file:
    integer = int(line)
    string = line
    string = string.replace("\n", "")
    while not(is_sorted(list(string))) and len(list(string)) > 1:
        integer = integer - 1
        string = str(integer)

    line_count = line_count + 1
    out.write("Case #" + str(line_count) + ": " + str(integer) + "\n")
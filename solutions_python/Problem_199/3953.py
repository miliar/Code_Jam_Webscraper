import re

dictionary = {};


def recursive(str, dist, flipsize):
    dictionary[str] = dist;
    for i in range(len(str)-flipsize+1):
        newstr = flip(str, i, flipsize);
        if newstr in dictionary:
            return;
        else:
            recursive(newstr, dist+1, flipsize);

def flip(str, index, flipsize):
    strlist = list(str);
    for i in range(flipsize):
        if strlist[index+i] == '+':
            strlist[index+i] = '-';
        else:
            strlist[index+i] = '+';
    return ''.join(strlist);


size = 0;
with open("A-small-attempt3.in", 'r') as fin, open("text.out", 'w') as fout:
    for index, line in enumerate(fin):
        if index == 0:
            size = int(line);
            continue;
        else:
            tokens = line.split();

            # add root string
            rootstr = "+" * len(tokens[0]);
            # recursively fill dictionary
            recursive(rootstr, 0, int(tokens[1]));

            if tokens[0] in dictionary:
                fout.write("Case #" + str(index) + ": " + str(dictionary[tokens[0]]));
            else:
                fout.write("Case #" + str(index) + ": IMPOSSIBLE");

            if index != size:
                fout.write("\n");

        # empty dictionary
        dictionary = {};
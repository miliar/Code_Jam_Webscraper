import re

f = open('./A-large.in');
fout = open('output.out', 'w');


(null, numwords, numtests) = f.readline().split();

wordlist = list();
regexs = list();

for i in range(int(numwords)):
    wordlist.append(f.readline().strip());

for i in range(int(numtests)):
    regexs.append(f.readline().strip().replace('(', '[').replace(')', ']'));

for i in range(int(numtests)):
    p = re.compile(regexs[i])

    matches = 0
    for string in wordlist:
        if p.match(string):
            matches += 1

    fout.write('Case #' + str(i+1) + ": " + str(matches) + "\n")

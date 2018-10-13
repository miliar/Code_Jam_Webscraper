# Google Codejam 2012
# Qualification Round
# Nivvedan S

INPUT_FILE_NAME="p1.in"
OUTPUT_FILE_NAME="p1.out"
IN = open(INPUT_FILE_NAME, "r")
OUT = open(OUTPUT_FILE_NAME, "w")

lines=IN.readlines()

T=int(lines[0].strip())
lines=lines[1:]

count = 0

for line in lines:
    line = line.strip()
    eng = ""
    for c in line:
        eng = eng+str(replace(c))
    count = count +1
    print "Case #"+str(count)+": "+eng



def replace(e):
    googlerse = {' ':' ', 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
    return googlerse[e]

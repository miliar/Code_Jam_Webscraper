__author__ = 'diana_fisher'

# Speaking in Tongues
# We have come up with the best possible language here at Google, called Googlerese.
# To translate text into Googlerese, we take any message and replace each English
# letter with another English letter. This mapping is one-to-one and onto, which
# means that the same input letter always gets replaced with the same output letter,
# and different input letters always get replaced with different output letters.
# A letter may be replaced by itself. Spaces are left as-is.
#  'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means that "a zoo" will become "y qee"


def translate(text):
    result = ''
    replacements = {
        'a':'y',
        'b':'h',
        'c':'e',
        'd':'s',
        'e':'o',
        'f':'c',
        'g':'v',
        'h':'x',
        'i':'d',
        'j':'u',
        'k':'i',
        'l':'g',
        'm':'l',
        'n':'b',
        'o':'k',
        'p':'r',
        'q':'z',
        'r':'t',
        's':'n',
        't':'w',
        'u':'j',
        'v':'p',
        'w':'f',
        'x':'m',
        'y':'a',
        'z':'q'
       }
    for i in range(len(text)):
        char = text[i]
        if not char in replacements:
            result += ' '
        else:
            result += replacements[char]

    return result


filename = "A-small-attempt0.in"
file = open(filename, "r")
lines = []
for line in file:
    lines.append( line.strip() )

file.close()

numCases = int(lines[0])
for i in range(1, numCases+1):
    case = "Case #" + str(i) + ":"
    print case, translate(lines[i])

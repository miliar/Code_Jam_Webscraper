# Problem A
#
# Google Code Jam 2012
# CWSFDavid
#

index = {'y':'a',
         'n':'b',
         'f':'c',
         'i':'d',
         'c':'e',
         'w':'f',
         'l':'g',
         'b':'h',
         'k':'i',
         'u':'j',
         'o':'k',
         'm':'l',
         'x':'m',
         's':'n',
         'e':'o',
         'v':'p',
         'z':'q',
         'p':'r',
         'd':'s',
         'r':'t',
         'j':'u',
         'g':'v',
         't':'w',
         'h':'x',
         'a':'y',
         'q':'z'}

file_in = list(open('A-Small.in', 'r'))
file_in = file_in[1:]

output = []
tally = 0
for line in file_in:
    tally += 1
    word = ''
    for c in line[:-1]:
        try:
            c = index[c]
        except:
            pass

        word = word + c
                    
                
    output.append('Case #' + str(tally) + ': ' + word)
    
print
for case in output:
    print case
    

#
# Alec Grieser
# 13 April 2012
#
# For Google Code Jam qualifying round, "Speaking in Tongues" problem.
#

translation = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f',
               'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l',
               'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r',
               'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x',
               'a':'y', 'q':'z'}

data = open("A-small-attempt0.in", "r").read().split('\n')

count = int(data[0])

for i in range(count):
    g = data[i + 1]
    g_prime = ''

    for letter in g:
        if letter in translation.keys():
            g_prime += translation[letter]
        else:
            g_prime += letter

    print("Case #%d: %s" % (i + 1, g_prime))

    

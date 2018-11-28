cipher = { ' ':' ', 'y':'a', 'f':'c', 'n':'b', 'c':'e',
          'i':'d', 'l':'g', 'w':'f', 'k':'i', 'b':'h',
          'o':'k', 'u':'j', 'x':'m', 'm':'l', 'e':'o',
          's':'n', 'z':'q', 'v':'p', 'd':'s', 'p':'r',
          'j':'u', 'r':'t', 't':'w', 'g':'v', 'a':'y',
          'h':'x', 'q':'z' }
input = open("A-small-attempt0.in", "r")
output = open("output.txt", "w")
cases = int(input.readline())
count = 1
while(cases>0):
    line = input.readline().strip('\n')
    outline = "Case #" + str(count) + ": "
    for char in line:
        outline = outline + cipher[char]
    output.writelines(outline + '\n')
    cases = cases - 1
    count = count + 1
output.close()
input.close()

import sys
input = sys.stdin.readlines()

t = int(input[0][:len(input[0])-1])

dict = {
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
'z':'q',
' ':' '
}

for i in range(1, t+1):
	S = 'Case #' + str(i) + ': '
	G = input[i]
	if input[i][len(input[i])-1] == '\n':
		G = input[i][:len(input[i])-1]
	for char in G:
		S += dict[char]
	print S


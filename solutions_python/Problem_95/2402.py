
letterMap = { 
'a': 'y',
'b': 'h', 
'c': 'e', 
'd': 's', 
'e': 'o', 
'f': 'c', 
'g': 'v', 
'h': 'x', 
'i': 'd', 
'j': 'u', 
'k': 'i',
'l': 'g',
'm': 'l',
'n': 'b',
'o': 'k',
'p': 'r',
'q': 'z',
'r': 't',
's': 'n',
't': 'w',
'u': 'j',
'v': 'p',
'w': 'f',
'x': 'm',
'y': 'a',
'z': 'q'
 }

lineCount = int( raw_input() )

outputText = ""
for i in range(0,lineCount):
	line = raw_input()
	output = "Case #" + str(i+1) + ": "

	decoded = ''
	for x in line:
		if x in letterMap:
			decoded += letterMap[x]
		else:
			decoded += x
	output += decoded
	outputText += output + "\n"

print (outputText)

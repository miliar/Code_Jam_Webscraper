# Code Jam 2012 - Qualification round - Problem A

def translate(text, dic):
  for i, j in dic.iteritems():
    text = text.replace(i, j)
  return text

finput = open("input.txt", "r")
foutput = open("output.txt", "w")

t = int(finput.readline())

rep1 = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'0', 'k':'`', 'l':'~', 'm':'!', 'n':'@', 'o':'#', 'p':'$', 'q':'%', 'r':'^', 's':'&', 't':'+', 'u':'*', 'v':'(', 'w':')', 'x':'-', 'y':'_', 'z':'='}
rep2 = {'1':'y', '2':'h', '3':'e', '4':'s', '5':'o', '6':'c', '7':'v', '8':'x', '9':'d', '0':'u', '`':'i', '~':'g', '!':'l', '@':'b', '#':'k', '$':'r', '%':'z', '^':'t', '&':'n', '+':'w', '*':'j', '(':'p', ')':'f', '-':'m', '_':'a', '=':'q'}
i=0
while i<t:
	string = finput.readline()
	string = translate(string, rep1)
	string = translate(string, rep2)
	foutput.write("Case #" + str(i+1) + ": " + string)
	i+=1

finput.close()
foutput.close()

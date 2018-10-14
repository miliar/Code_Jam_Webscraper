input = open('A-small-attempt1.in','r')
output = open('output1.txt','w')
dict = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
line = input.readline()
line = line.replace("\n","")
numberOfTestCases = int(line.split(" ")[0])
for i in range(numberOfTestCases):
    line = input.readline()
    line = line.replace("\n","")
    string = "".join(dict.get(c, c) for c in line)
    output.write("Case #"+str(i+1)+": "+string+"\n")
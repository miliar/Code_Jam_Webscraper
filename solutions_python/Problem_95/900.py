import string
def findMapping(text):
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encrypt=["y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"]
    text=list(text)
    for each in range(0,len(text)):
        if text[each] in letters:
            text[each]=letters[encrypt.index(text[each])]
    return "".join(text)


x=open("test8.in")
z=open("output.txt","w")

case=0
currentline=x.readline()


currentline=x.readline().rstrip().lstrip()
while currentline:
    case=case+1
    z.write("Case #"+str(case)+": "+findMapping(currentline)+"\n")
    currentline=x.readline().rstrip().lstrip()
z.close()


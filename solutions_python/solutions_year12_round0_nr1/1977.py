alpha = {"a":"y","b":"h","c":"e","d":"s","e":"o","f":"c","g":"v","h":"x","i":"d","j":"u","k":"i","l":"g","m":"l","n":"b","o":"k","p":"r","q":"z","r":"t","s":"n","t":"w","u":"j","v":"p","w":"f","x":"m","y":"a","z":"q"," ":" ","\n":"\n"}
fr = open("C:\Users\Matt\Desktop\gcj\p1\in.in", "r")
text = fr.readline()
out = ""
lines = text[0]
for i1 in range(0,int(lines)):
    text = fr.readline()
    print text
    out += "Case #" + str(i1+1) + ": "
    for i in text:
        out += alpha[i]
fr.close()
fw = open("C:\Users\Matt\Desktop\gcj\p1\out.txt", "w")
fw.write(out[:-1])
fw.close()

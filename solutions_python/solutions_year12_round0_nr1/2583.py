m = open("mapping","r")
dict = {}
for str2 in m:
        a = str2.split(";")
        dict[a[0]] = a[1].replace("\n","")

g = open("blabla","r")
res = ""
str1 = ""
x = int(g.readline())
for i in range(x):
        res += "Case #"+str(i+1)+": "
        str1 = g.readline();
        for c in str1:
                if c == " ":
                        res += " "
                elif c == "\n":
                        res += "\n"
                else:
                        res += dict[c]
print res    


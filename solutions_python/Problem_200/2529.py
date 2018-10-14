with open("B-large.in") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
f = open("answers 1.odt","w+")
#content = ["4","132","1000","7","111111111111111110"]
for i in range(1,len(content)):
    q = i
    a = list(content[i])
    a.reverse()
    if len(a) > 1:
        for j in range(len(a)-1):
            if int(a[j+1]) <= int(a[j]):
                pass
            if int(a[j]) < int(a[j+1]):
                a[j+1] = str(int(a[j+1]) - 1)
                for k in range(0,j+1):
                    a[k] = "9"
    a.reverse()
    if a[0] == "0":
        a = a[1:]
    s = ""
    p = int(s.join(a))

    f.write("Case #%d: %d\r\n" % (q,p))
    f.write("\r\n")

 #   else:
  #      f.write("Case #%d: IMPOSSIBLE\r\n" % q)
f.close()

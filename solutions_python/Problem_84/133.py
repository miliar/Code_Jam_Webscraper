
def changecolor(pixels):
    for y in xrange(0, len(pixels)-1):
        for x in xrange(0, len(pixels[y])-1):
            if pixels[y][x]=="#" and pixels[y+1][x]=="#" and pixels[y][x+1]=="#" and pixels[y+1][x+1]=="#":
                pixels[y][x]="/"
                pixels[y+1][x]="\\"
                pixels[y][x+1]="\\"
                pixels[y+1][x+1]="/"
    for row in pixels:
        if "#" in row:
            return "Impossible"
    return pixels


data=open("A-large.in","r").read()


data=data.splitlines()[1:]
data.reverse()
out=open("out.txt","w")
c=0
while data:
    c+=1
    rows, columns=[int(i) for i in data.pop().split(" ")]
    pixels=[]
    for i in xrange(0,rows):
        column=data.pop()
        pixels.append(list(column))
    out.write("Case #%i:\n"%c)
    t=changecolor(pixels)
    if t=="Impossible":
        out.write("Impossible\n")
    else:
        for i in t:
            out.write("".join(i)+"\n")
    
out.close()

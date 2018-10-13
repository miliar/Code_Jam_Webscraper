##Fair and Square
##Michael Feliciano
#College of Charleston
# Small solution



files = ["C-small-attempt0.in","C-large.in"]
content = file(files[0])

FandS = [1,4,9,121,484]

cases = int(content.readline())

filename = "output.txt"
File = open(filename,'w')

for i in range(cases):
    s,f = map(int,content.readline().split())
    counter = 0
    for item in FandS:
        if(item >= s and item <= f):
            counter +=1
    File.write("Case #%d: %s" % (i+1,counter ) + "\n")

File.close()



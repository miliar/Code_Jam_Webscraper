def check (string):
    done = True
    for j in range(len(string)):
            if string[j] != "+":
                done = False
    return done

def flip(string):
    if string == "+":
        return "-"
    if string == "-":
        return "+"

file = open("A-large.in","r")
output = open("output_file.txt","w")
testnum = file.readline()
count = 0
o = 0
for line in file:
    count = 0
    information = line.split()
    string = information[0]
    size = information[1]
    for i in range(len(string)-int(size)+1):
        if string[i] == "-":
            j = i
            count+=1
            for k in range(int(size)):
                temp = list(string)
                temp[j] = flip(temp[j])
                string = "".join(temp)
                j+=1
    o+=1
    if (check(string) == False):
        output.write("Case #"+str(o)+": IMPOSSIBLE\n")
    else:
        output.write("Case #"+str(o)+": " + str(count)+"\n")

file.close()
output.close()

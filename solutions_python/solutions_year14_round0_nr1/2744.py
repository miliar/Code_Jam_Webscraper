def run():
    output = open("output",'w')
    input = open("input")
    line = input.readline()
    if line:
        tatal = int(line)
        line = input.readline()
    count = 1
    while line:
        volun = int(line)
        num = 1
        line = input.readline()
        while num < 5:
            if num == volun:
                rows1 = set(line.split())
            line = input.readline()
            num += 1
        volun = int(line)
        num = 1
        line = input.readline()
        while num < 5:
            if num == volun:
                rows2 = set(line.split())
            line = input.readline()
            num +=1
        x = rows1 & rows2
        if len(x) == 0:
            output.write("Case #"+str(count)+": Volunteer cheated!")
        elif len(x) == 1:
            output.write("Case #"+str(count)+": "+x.pop())
        else:
            output.write("Case #"+str(count)+": Bad magician!")
        count += 1
        output.write("\n")
    output.close()
    input.close()

if __name__ == "__main__":
    run()

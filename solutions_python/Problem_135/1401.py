
def process(x,y,x_line,y_line):
    count = 0
    for k in x_line:
        if k in y_line:
            count += 1
            num = k
        if count > 1:
            return "Case #"+str(i+1)+": Bad magician!"
    if count == 0:
        return "Case #"+str(i+1)+": Volunteer cheated!"
    elif count ==1:
        return "Case #"+str(i+1)+": " + str(num)

if __name__ == '__main__':
    f = open('A-small-attempt0.in', 'rb')
    input = f.read().split('\n')
    t = int(input[0])
    fout = open('output.txt','wb')
    for i in range(t):
        baseline = i*10+1
        x = int(input[baseline])
        x_line = [int(j) for j in input[baseline+x].split(" ")]
        y = int(input[baseline+5])
        y_line = [int(j) for j in input[baseline+5+y].split(" ")]
        result = process(x,y,x_line,y_line)
        print(result)

def main():
    inputfile = open("B-small-attempt0.in", 'r')
    outputfile = open("output", 'w')
    inputfile.readline()
    currentcase = 1
    for line in inputfile:
        index = 0
        length = len(line) - 1
        s = ''
        while line[index].isdigit():
            s += line[index]
            index += 1
        C = int(s)
        combine = []
        s = ''
        combinelimit = C * 4 + 1
        while index < combinelimit:
            if line[index] != ' ':
                s += line[index]
            if len(s) == 3:
                combine.append(s)
                s = ''
            index += 1
        index += 1
        s = ''
        while line[index].isdigit():
            s += line[index]
            index += 1
        D = int(s)
        opposed = []
        opposedlimit = index + D * 3
        s = ''
        while index < opposedlimit:
            if line[index] != ' ':
                s += line[index]
            if len(s) == 2:
                opposed.append(s)
                s = ''
            index += 1
        print index
        while not line[index].isalpha():
            index += 1
        output = []
        print index, length
        while index < length:
            output.append(line[index])
            i = 0
            l = len(combine)
            is_combine = False
            while i < l and not is_combine:
                if len(output) >= 2 and ((output[-1] == combine[i][0] and output[-2] == combine[i][1])\
                   or output[-1] == combine[i][1] and output[-2] == combine[i][0]):
                    output.pop()
                    output.pop()
                    output.append(combine[i][2])
                    is_combine = True
                i += 1
            is_opposed = False
            print C, D, output
            if not is_combine:
                for o in opposed:
                    if output[-1] in o:
                        for i in output[:-1]:
                            if (i in o) and i != output[-1]:
                                is_opposed = True
                if is_opposed:
                    output = []
                
            index += 1
        s = '['
        for i in output:
            s += i
            s += ', '
        if len(output):
            s = s[:-2] + ']'
        else:
            s = '[]'
        output = "Case #%d: %s\n" % (currentcase, s)
        outputfile.write(output)
        currentcase += 1
    inputfile.close()
    outputfile.close()
    
    
if __name__ == "__main__":
    main()
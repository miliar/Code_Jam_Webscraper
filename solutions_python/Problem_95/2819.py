import sys
import string

input_str = "yhesocvxduiglbkrztnwjpfmaq"

def read_file(filePath):
    f = open(filePath, 'r')

    try:
        count = int(f.readline().replace("\n", ""))
        if count > 30:
            sys.exit("Beyond limit")
    except ValueError:
        sys.exit("Invalid input")

    file = f.readlines()
    f.close()
    lists = [[] for i in range(count)]
    i = 0
    for line in file:
        if len(line.strip()) == 0:
            break
        lists[i].append("Case #")
        lists[i].append(str(i + 1))
        lists[i].append(": ")
        for char in line:
            if char == " ":
                lists[i].append(" ")
            elif char == "\n":
                pass
            else:
                # print str[(ord(char) - 97)]
                lists[i].append(input_str[(ord(char) - 97)])
        print "".join(lists[i])
        i = i + 1  
    
    w = open('output', 'wb')
    # for list in lists:
        
    
if __name__ == '__main__':
    read_file('A-small-attempt0.in')

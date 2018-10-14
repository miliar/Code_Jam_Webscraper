__author__ = 'rsadykov'

def readInputs():
    input_file = open("B-large.in", "r")
    text = input_file.read()
    text_lines = text.split("\n")
    if text_lines[len(text_lines)-1] == "" : del text_lines[-1]
    return text_lines

def processInputs(lines):
    out_file = open("out_file.txt", "w")
    out_file2 = open("compressed.txt", "w")
    for i in range(0, len(lines), 2):
        answer = processInput(getList(lines[i+1]))
        out_file2.write(lines[i+1] + "\n")
        out_string =  "Case #" + str(i/2+1) + ": "+str(answer) + "\n"
        out_file.write(out_string )


def getList(line):
    plates = line.split(" ")
    plates_int = [int(n) for  n in plates]
    return plates_int

def processInput(plates):
    plates.sort(reverse = True)
    i = 0
    minutes = plates[0]
    #potentially rethink this statement later
    #while i < len(plates):
        #next_index = next_highest_index(plates, i)
    for i in range(plates[0], 1, -1):
        splits = splits_upto(plates, len(plates), i)
        new_minutes = splits + i
        #splits = splits_upto(plates, i, plates[i])
        #new_minutes = splits + plates[i]
        if new_minutes < minutes: minutes = new_minutes
        #i = next_index
    last_value = plates[len(plates)-1]
    #half_value = (last_value&1) + last_value >>1
    '''for i in range(last_value, 1, -1):
        splits = splits_upto(plates, len(plates), i)
        new_minutes = splits + i
        if new_minutes < minutes: minutes = new_minutes
        '''
    return minutes

def splits_upto(plates, index, value):
    splits = 0
    for i in range(0, index):
        if(plates[i] <= value):
            return splits
        splits += plates[i]/value
        if plates[i]%value == 0 : splits-=1
    return splits


def next_highest_index(plates, index):
    highest = plates[index]
    for i in range(index, len(plates)):
        if plates[i] != highest:
            return i
    return len(plates)

read_lines = readInputs()
processInputs(read_lines[1:])


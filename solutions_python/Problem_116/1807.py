import copy

def read_file():
    f = open("qa_in.txt")
    global a
    a = f.readlines()
    global test_cases
    assert int(a[0])
    test_cases = int(a.pop(0))
    a = [s.strip("\n") for s in a]
    f.close()
    
def convert_data():
    global data
    data = []
    for i in range(test_cases):
        data.append([])
        data[i] = a[5*i : 5*i+4]

def single_check_completion(b):
    for line in b:
        for char in line:
            if char == ".":
                return False
    return True
                    
def check_completion():
    global completions
    completions = []
    for d in data:
        completions.append(single_check_completion(d))
    
def single_check_for_lines(b):
    p_lines = [] # possible rows
    # rows
    for row in b:
        p_lines.append(row)
    # columns
    for i in range(4):
        p_lines.append("")
        for j in range(4):
            p_lines[-1] += b[j][i]
    # both diagonals
    p_lines.append(b[0][0]+b[1][1]+b[2][2]+b[3][3])
    p_lines.append(b[0][3]+b[1][2]+b[2][1]+b[3][0])
    # check
    for line in p_lines:
        if line == "XXXX" or line == "XXXT" or line == "XXTX" or line == "XTXX" or line == "TXXX":
            return "X" # assert there is always only one line
        elif line == "OOOO" or line == "OOOT" or line == "OOTO" or line == "OTOO" or line == "TOOO":
            return "O" # assert there is always only one line
    return None

def check_for_lines():
    global lines
    lines = []
    for d in data:
        lines.append(single_check_for_lines(d))
           
def write_to_file():
    f2 = open("qa_out.txt", 'wt') 
    for i in range(len(data)):
        result = ""
        if lines[i] == None and completions[i] == True:
            result = "Draw"
        elif lines[i] == None and completions[i] == False:
            result = "Game has not completed"
        elif (lines[i] == "X" or lines[i] == "O"):
            result = lines[i]+" won"
        f2.writelines("Case #"+str(i+1)+": "+str(result)+"\n")   
    f2.close()

def debug():
    print data
    print completions
    print lines

def main():    
    read_file()
    convert_data()
    check_completion()
    check_for_lines()
    write_to_file() # < check first for rows, then completion
    #debug()

if __name__ == "__main__":
    main()

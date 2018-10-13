
def process(data):
    for line in data:
        Xconut = line.count("X")
        Ocount = line.count("O")
        Tcount = line.count("T")
        if (Tcount + Xconut + Ocount) != 4:
            return False 
        else:
            return True

def process_row(data):
    for line in data:
        Xconut = line.count("X")
        Ocount = line.count("O")
        Tcount = line.count("T")
        if Xconut == 4 or (Xconut == 3 and Tcount == 1):
            return "X won" 
        elif Ocount == 4 or (Ocount == 3 and Tcount == 1):
            return "O won"

def process_column(data):
    for column_number in range(4):
        column_data = []
        for index in range(4):
            column_data.append(data[index][column_number])
        Xconut = column_data.count("X")
        Ocount = column_data.count("O")
        Tcount = column_data.count("T")
        if Xconut == 4 or (Xconut == 3 and Tcount == 1):
            return "X won" 
        elif Ocount == 4 or (Ocount == 3 and Tcount == 1):
            return "O won"


def process_diagonal(data):
    diagonal_data = []
    for number in range(4):
        diagonal_data.append(data[number][number])
    Xconut = diagonal_data.count("X")
    Ocount = diagonal_data.count("O")
    Tcount = diagonal_data.count("T")
    if Xconut == 4 or (Xconut == 3 and Tcount == 1):
        return "X won" 
    elif Ocount == 4 or (Ocount == 3 and Tcount == 1):
        return "O won"

    diagonal_data = []
    for number in range(4):
        diagonal_data.append(data[number][3-number])
    Xconut = diagonal_data.count("X")
    Ocount = diagonal_data.count("O")
    Tcount = diagonal_data.count("T")
    if Xconut == 4 or (Xconut == 3 and Tcount == 1):
        return "X won" 
    elif Ocount == 4 or (Ocount == 3 and Tcount == 1):
        return "O won"

File = file("A-small-attempt0.in")
total = File.readline().strip()
for index in range(int(total)):
    result = ""
    data = []
    for i in range(5):
        line = File.readline().strip()
        if line:
            data.append(line)
        else:
            break
    FLAG = process(data)
    result = process_row(data)
    if not result:
        result = process_column(data)
    if not result:
        result = process_diagonal(data)
    if (not result) and FLAG:
        result = "Draw"
    if (not result) and (not FLAG): 
        result = "Game has not completed"

    end_result = "Case #%s: %s" % (index+1, result)
    print end_result

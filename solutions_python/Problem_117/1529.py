def convert_input(a):
    result_list = a.split(" ")


    return result_list


def check_horizontal(n, m, a):
    checked_lawn = a;
    for i in range(0, n):
        if a[i][0] == '1': 
            fail = 0
            for j in range(1, m):
                if a[i][j] != '1':
                    fail = fail + 1
            if fail == 0:
                for k in range(0, m):
                    checked_lawn[i][k] = 'X'    
    return checked_lawn

def check_vertical(n, m, a):
    checked_lawn = a;
    for i in range(0, m):
        if a[0][i] == '1' or a[0][i] == 'X': 
            fail = 0
            for j in range(1, n):
                if (a[j][i] != '1') and (a[j][i] != 'X'):
                    fail = fail + 1
            if fail == 0:
                for k in range(0, n):
                    checked_lawn[k][i] = 'X'    
    return checked_lawn


def check_no_one(n, m, a):
    
    one_num = 0
        
    for i in range(0, n):
        for j in range(0, m):
            if(a[i][j]=='1'):
               one_num += 1
               
    if one_num == 0:
        return "YES"
    else:
        return "NO"


input = open('B-small-attempt2.in', 'r')
T = int(input.readline())
for i in range(0, T):
    text = input.readline()
    temp = text.split("\n")[0]
    n = int(temp.split(" ")[0])
    m = int(temp.split(" ")[1])
    lawn = []
    for j in range(0, n):
        text = input.readline()
        
        temp = text.split("\n")[0]
        
        converted = convert_input(temp)
        lawn.append(converted)
    new_lawn = check_horizontal(n, m, lawn)
    new_lawn = check_vertical(n, m, new_lawn)
    result = check_no_one(n, m, new_lawn)
    if((n==1) or (m==1)):
        result = "YES"
    print "Case #" + str(i+1) + ": " + str(result) 

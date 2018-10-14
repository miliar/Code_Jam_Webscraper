lines = [line.strip() for line in open("c:\Users\Mingan\Downloads\A-small-attempt1.in","r")]
data = []
def clean_data(lines,data):
    for i in lines:
        data.append(list(i))
        temp = []
        temp2 = []
        if len(data[-1]) <= 3:
            temp2.append(int(''.join(data[-1])))
        else:        
            for j in data[-1]:
                if j != " ":
                    temp.append(j)
                else:
                    temp2.append(int(''.join(temp)))
                    temp = []
            temp2.append(int(''.join(temp)))
        data[-1] = temp2
    return data            

data = clean_data(lines,data)

T = data[0][0]
data.remove([T])
print  data

def clean_game(data):
    for i in data:
        if len(i) == 1:
            break
        else:
            data.remove(data[0])
    return data
    
def lets_play_a_game(data,i):
    #Get answer 1
    ans1 = data[0][0]
    if check_cheater(ans1,i) == 0:
        print "turn" + str(i)
        data = clean_game(data)
        return data
    data.remove([ans1])
    #Check mage matrix 1    
    a = []
    for j in range(4):
        a.append(data[0])
        data.remove(a[-1])
    temp = []
    for j in a:
        temp.append(sum(j))
    if sum(temp) != 136:
            print "Case #" + str(i+1) + ": Bad magician!"
            return data
    #Get selected row
    a_pick = a[ans1 - 1]
    
    #Get answer 1    
    ans2 = data[0][0]
    if check_cheater(ans2,i) == 0:
        print "turn" + str(i)
        data = clean_game(data)
        return data
    data.remove([ans2])
    #Check mage matrix 2
    b = []
    for j in range(4):
        b.append(data[0])
        data.remove(b[-1])
    temp = []
    for j in b:
        temp.append(sum(j))
    if sum(temp) != 136:
            print "Case #" + str(i+1) + ": Bad magician!"
            return data
    #Get selected row
    b_pick = b[ans2 - 1]
    #Check both selected rows for solution
    solution = check_solution(a_pick,b_pick,i)
    if solution == 0:
        return data
    else:
        print "Case #" + str(i+1) + ": " + str(solution)

def check_cheater(ans,i):
    if 4 < ans or ans < 1: 
        print "Case #" + str(i+1) + ": Volunteer cheated!"
        return 0

def check_solution(a_pick,b_pick,i):
    sol_list = []
    for j in a_pick:
        for k in b_pick:
            if j == k:
                sol_list.append(j)
    if len(sol_list) > 1:
        print "Case #" + str(i+1) + ": Bad magician!"
        return 0
    elif len(sol_list) < 1:
        print "Case #" + str(i+1) + ": Volunteer cheated!"
        return 0
    else:
        return sol_list[0]
        
for i in range(T):
    lets_play_a_game(data,i)
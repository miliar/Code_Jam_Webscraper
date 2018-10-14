input_file = open('/Users/arisha/Desktop/Python/codejam/Alien Language/A-large-practice.in')
#output_file = open('/Users/arisha/Desktop/Python/codejam/Alien Language/A-large-practice.out', 'w')

T = int(input_file.readline().strip())

cases = []

for i in range(T):
    cases.append([])
    for j in range(4):
        cases[i].append([list(input_file.readline().strip())])
    input_file.readline()
print cases

for i in range(T):
    ans = ''
    case = cases[i]
    sols = []
    unfilled = False
    for j in ["X", "O"]:
        curr_case = []
        for k in range(4):
            curr_case.append([1 if (x==j or x=='T') else 0 for x in case[k]])
            if '.' in case[k]:
                unfilled = True
                
        for k in range(4):
            curr_case.append([case[x][k] for x in range(4)])
        curr_case.append([case[x][x] for x in range(4)])
        curr_case.append([case[x][x] for x in range(0,4,-1)])
        if [1, 1, 1, 1] in curr_case:
            ans = sym + " won"
            break

    if ans == '':
        if unfilled:
            ans = "Game has not completed"
        else:
            ans = "Draw"
    ans = "Case%d: %s\n" %(i+1, ans)
    print ans

input_file.close()
#output_file.close()
        
        
        
    

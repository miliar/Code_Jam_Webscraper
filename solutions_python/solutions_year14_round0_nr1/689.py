

def find(row1, row2, arr1, arr2):
    p = arr1[row1-1]
    q = arr2[row2-1]

    ans = 0
    
    for i in range(4):
        for j in range(4):
            if p[i] == q[j]:
                if ans == 0:
                    ans = p[i]
                else:
                    ans = 17;
            
    return ans

def output(out, case, ans):
    if ans > 0 and ans < 17:
        out.write("Case #" + str(case) + ": " + str(ans) + "\n")
    elif ans == 0:
        out.write("Case #" + str(case) + ": " + "Volunteer cheated!" + "\n")
    elif ans == 17:
        out.write("Case #" + str(case) + ": " + "Bad magician!" + "\n")

def main():
    file_in = open('A-small-attempt0.in')
    file_out = open('out.txt', 'w')

    total_cases = int(file_in.readline())

    for i in range(total_cases):
        row1 = int(file_in.readline())
        arr1 = [[],[],[],[]]
        for j in range(4):
            line = file_in.readline()
            new_line = line.split(" ")
            for x in new_line:
                arr1[j].append(int(x))
                
        row2 = int(file_in.readline())
        arr2 = [[],[],[],[]]
        for j in range(4):
            line = file_in.readline()
            new_line = line.split(" ")
            for x in new_line:
                arr2[j].append(int(x))

        ans = find(row1, row2, arr1, arr2)
        output(file_out, i+1, ans)
        
        
    file_in.close()
    file_out.close()

main()




















    

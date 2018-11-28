testcase = int(input())
'''
def negate(ch):
    if ch == "+":
        return "-"
    elif ch == "-":
        return "+"
    else:
        raise ValueError("Error in negate")
'''
for tc in range(testcase):
    linestr = input()
    temppancakestr = linestr.split(" ")[0]
    pancakes = []
    for i in range(len(temppancakestr)):
        pancakes.append(temppancakestr[i] == "+")
    K = int(linestr.split(" ")[1])
    ans = 0
    for i in range(len(pancakes) - K + 1):
        #print(pancakes)
        if pancakes[i] == False:
            ans += 1
            for j in range(K):
                pancakes[i+j] = not pancakes[i+j]
    #print(pancakes)
                
    status = True
    for i in range(K):
        if pancakes[-i] == False:
            status = False
            break

    #print("Case #"+str(tc+1)+": ")
    if status:
        print("Case #"+str(tc+1)+": "+str(ans))
    else:
        print("Case #"+str(tc+1)+": "+"IMPOSSIBLE")

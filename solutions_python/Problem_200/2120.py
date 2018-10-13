def simplify(N):
    for number in range(len(N)-1):
        if int(N[-(number+1)]) < int(N[-(number+2)]):
            nines = ""
            for i in range(number+1):
                nines += "9"
            return simplify(N[:-(number+2)] + str(int(N[-(number+2)]) - 1) + nines)
    return N

TestCases = int(input(""))
number = 0
for i in range(TestCases):
    number+=1
    N = str(input(""))
    result = simplify(N)
    if result[0] == "0":
        result = result[1:]
    print("CASE #" + str(number) + ": " + result)
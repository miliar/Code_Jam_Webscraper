

cases = int(input())

def solve(number):
    str_number = list(str(number))
    for i in range(0,len(str_number)-1):
        if int(str_number[i]) > int(str_number[i+1]):
            number -= number % pow(10,len(str_number)-i-1)+1
            return solve(number)
    return number
            








for i in range(0,cases):
    inflow = int(input())
    for j in range(0,18):
        inflow = solve(inflow)
    print("Case #"+str(i+1)+": "+ str(solve(inflow)))
            


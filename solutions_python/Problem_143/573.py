def main(input_address):
    input_file = open(input_address, "r")
    solve(input_file, open("D:\\output.txt","w"))

def solve(input_file, output_file):
    cases_number = int(input_file.readline())
    for k in range(cases_number):
        parameters = toInt(input_file.readline().split())
        answer = str(pairs(parameters))
        output_file.write("Case #" +
                          str(k+1) + ": " + answer + "\n")
    input_file.close()
    output_file.close()

def toInt(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def pairs(l):
    cnt = 0
    for i in range(l[0]):
        for j in range(l[1]):
            if i&j<l[2]:
                cnt+=1
    return cnt

main("D:\\input.in")

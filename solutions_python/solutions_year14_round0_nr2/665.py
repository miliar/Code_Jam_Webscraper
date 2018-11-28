
def find(C, F, X, S):
    ans = 0.0
    
    while X/S*1.0 > C/S*1.0 + X/(F+S)*1.0:
       ans += C/S
       S = F+S
       
    ans += X/S
    return ans

def main():
    file_in = open('B-large.in')
    file_out = open('out.txt', 'w')
    
    cases = int(file_in.readline())
    for case in range(cases):
        line = file_in.readline()
        new_line = line.split(" ")
        ans = find(float(new_line[0]), float(new_line[1]), float(new_line[2]), 2.0)
        file_out.write("Case #"+ str(case+1) + ": " + str(ans) + "\n")


    
    file_in.close()
    file_out.close()

main()

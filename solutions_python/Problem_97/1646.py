## KAMRA - YO YO ##

def get_cycles(n):
    cycles = []
    div = 10
    while div < n:
        a = n / div
        b = n % div
        c = int(str(b) + str(a))
        cycles.append(c)
        div = div * 10
    return list(set(cycles))    


def solve(input):
    A, B = input.split(" ")
    A = int(A)
    B = int(B)
    
    pairs = 0
    for n in range(A, B):        
        cycles = get_cycles(n);
        for m in cycles:
            if m > n and m <= B:
                pairs = pairs + 1;
    
    return pairs 
  
#####################################################################
def main():
    in_file_name = "C-small-attempt0.in"
    out_file_name = "C-small-attempt0.out"
    
   
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    reader.readline()
    for case_no, input in enumerate(reader):
        result = solve(input)
        writer.write("Case #" + str(case_no+1)+ ": " + str(result) + "\n")   
    writer.close()
    
#####################################################################
if __name__== "__main__":
    main()
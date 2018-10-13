import time

def solve(case):
    A, B = [int(x) for x in case.split(" ")]
    result = 0
    digits = len(str(A))
    used = {}
    
    for a in range(A, B):
        a_str = str(a)
        #print a_str
        for i in range(1, digits):
            b_str = a_str[i:] + a_str[:i]
            
            if b_str[0] == '0':
                continue
            
            b = int(b_str)
            
            if a < b and b <= B:
                pair = a_str + b_str
                
                if pair in used:
                    continue
                
                result += 1
                used[pair] = 1
    
    return result


def main():
    input = open('C-large.in')
    output = open('output.txt', 'w')
    total_case_num = int(input.readline().strip())
    
    for case_num in range(1, total_case_num + 1):
        case = input.readline().strip()
        result = solve(case)
        output.write("Case #%s: %s\n" % (case_num, result))

if __name__ == '__main__':
    #solve("1111 2222")
    #s = time.time()
    #solve("1000000 2000000")
    #print time.time() - s
    main()


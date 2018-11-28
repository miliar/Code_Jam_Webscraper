# generate palindromes whose squares are also palindromes
# 3 digits:
#       aba = 101a + 10b
#       aba^2 = (101a + 10b)(101a + 10b) = 2020*a*b + 100*b**2 + 10201*a**2
#       aba^2 has 5 or 6 digits
#       5 digits: cdedc = 10001c + 1010d + 100e = 2020ab + 100b^2 + 10201a^2

#       6 digits: cdeedc = 10001c + 10010d + 1100e = 2020ab + 100b^2 + 10201a^2

# find all solutions of 10001c + 1010d + 100e - 2020ab + 100b^2 + 10201a^2 = 0
# a^2, b^2, ab, c, d, e
# [10201, 100, -2020, 10001, 1010, 100] = [0]
# 

def is_palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    return False

def solution(parsed_line, plist):
    A = int(parsed_line.split(' ')[0])
    B = int(parsed_line.split(' ')[1])

    result = 0
    for i in plist:
        if i >= A:
            if i <= B:
                result += 1
    return result
            
        
def parse_input(f):
    data = open(f).read().split("\n")
    result = []
    T = int(data[0])

    for i in range(1, len(data)):
        if data[i] != '':
            result.append(data[i])

    return result
                      
def solve():
    plist = list(set([int(i) for i in open("all p.txt").read().split('\n') if i != '']))

    process_output = lambda l: str(l)

    f = 'C-large-1.in'
    fout = open('output.txt', 'w')
    parsed_input = parse_input(f)

    for line in range(len(parsed_input)):
        
        s = "Case #" + str(line + 1) + ": " + process_output(solution(parsed_input[line], plist)) + "\n"
        fout.write(s)

    fout.close()


def generate_plist():
    all_f = open("all p.txt", "w")
    
    i = 0
    m = 0
    while i < (10 ** 7) + 1:
        if i % 100000 == 0:
            print i
        s = str(i)
        s1 = s + s[::-1]
        s2 = s + (s[::-1][1:])

        if is_palindrome(int(s1) ** 2):
            all_f.write(str(int(s1) ** 2) + '\n')
        if is_palindrome(int(s2) ** 2):
            all_f.write(str(int(s2) ** 2) + '\n')
        i += 1
    all_f.close()

solve()
                      

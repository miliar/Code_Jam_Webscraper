import sys, math

def is_palindrome(n):
    s = str(n)
    #print(" is_palindrome " + s)
    for i in range(0, int(len(s) / 2)):
        #print("  comp: " + str(i) + s[i] + " with " + s[-i])
        if not s[i] == s[-i-1]:
            #print("  ret: false");
            return False
    #print("  ret: true")
    #print(n)
    return True

def solve(line):
    a, b = map(int, line.split())
    #print("[a,b]:" + str(a) + "," + str(b))

    aa, bb = math.ceil(math.sqrt(a)), math.floor(math.sqrt(b))
    #print("[a',b']:" + str(aa) + "," + str(bb))
    base = filter(is_palindrome, [x for x in range(aa, bb+1)])
    squares = [x ** 2 for x in base]
    #print(squares)
    fairs = list(filter(is_palindrome, squares))

    #for i in fairs:
    #    print(i)

    #is_palindrome("a")
    #is_palindrome("abb")
    #is_palindrome("ababa")
    #is_palindrome("aa")

    #print(fairs)

    return len(fairs)

if __name__ == "__main__":
    fin = open("./input/C-small-attempt0.in")
    fout = open("./output/C-small-attempt0.out", "w")

    lines = fin.readlines()
    n_case = int(lines[0])
    #print(n_case)

    num = 1
    for line in lines[1:]:
        #print(line, file=fout)
        n = solve(line)
        print("Case #" + str(num) + ": " + str(n))
        print("Case #" + str(num) + ": " + str(n), file=fout)
        num = num + 1
        
    fout.flush()

    fin.close()
    fout.close()







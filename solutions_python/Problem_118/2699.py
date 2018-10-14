# find all squares
# so find all square roots

from math import sqrt

def main():
    file = open("C-small-attempt6.in")
    lines = file.read().split()
    file.close()
    #print(lines)
    #print(len(lines))
    number = int(lines[0])
    lines = lines[1:]
    result = ""
    for i in range(number):
        a = int(lines[2*i])
        b = int(lines[2*i+1])
        result += "Case #" + str(i + 1) + ": " + count(a, b)
    file = open("C-small-out6.txt", 'w')
    file.write(result)
    file.close()

def count(a, b):
    n = int(sqrt(a))
    m = int(sqrt(b)) + 1
    if n * n != a:
        print("yes!")
        n += 1
    print(str(n) + " " + str(m) + ":")
    c = 0
    for i in range(n, m):
        print(i)
        if is_fair(str(i)):
            if is_fair(str(i*i)):
                print("fair")
                c += 1
    return str(c) + "\n"
    

# n is a string
def is_fair(n):
    if len(n) < 2:
        return True
    elif n[0] == n[-1]:
        return is_fair(n[1:-1])
    else:
        return False
    

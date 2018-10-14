

def step(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            for fix in range(i+1, len(s)):
                s[fix] = "9"
            s[i] = str(int(s[i])-1)
            return False
    return True


def main():
    n = int(raw_input())
    for i in range(n):
        number = list(raw_input())
        while not step(number):
            pass
        number = int("".join(number))
        print "Case #" + str(i+1) + ": " + str(number)
            
main()
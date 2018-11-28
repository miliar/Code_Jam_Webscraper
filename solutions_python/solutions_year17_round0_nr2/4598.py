def tidy(n):
    while True:
        if is_tidy(n):
            print(n)
            return
        n -= 1

def is_tidy(n):
    digits = str(n)
    prev = digits[0]
    for d in digits:
        if int(prev) > int(d):
            return False
        prev = d
    return True

t = int(input())

for i in range(1, t + 1):
    print("Case #" + str(i) + ": ", end="")
    inp = int(input())
    tidy(inp)
    
 

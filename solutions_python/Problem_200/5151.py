def is_tidy(n):
    dig = map(int,list(str(n)))
    prev = -1
    for num in dig:
        if num < prev:
            return False
        prev = num
    return True

def last_tidy(n):
    while not is_tidy(n):
        n -= 1
    return n
    

n = int(input())
for i in range(n):
    print("Case #%d: %d" % (i+1, last_tidy(int(input()))))

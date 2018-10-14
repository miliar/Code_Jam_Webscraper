def generic_function(n):
    val = int(n)
    while val > 0:
        newVal = check(val)
        if newVal[0]:
            return val
        val = newVal[1]
    return val
        
def check(i):
    i = list(str(i))
    loc = -1
    for a, b in zip(i[:-1], i[1:]):
        loc += 1
        if int(a) > int(b):
            i[loc] = str(int(i[loc]) - 1)
            for c in range(loc+1, len(i)):
                i[c] = '9'
            return (False, int(''.join(i)))
    return (True, i)
    
value = int(input())  # read a line with a single integer
for i in range(1, value + 1):
    n = input()
    out = generic_function(n)
    print("Case #{}: {}".format(i, out))

    
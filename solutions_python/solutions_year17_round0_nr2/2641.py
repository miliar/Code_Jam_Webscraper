t = int(input())
def isTidy(n):
    ns = str(n)
    if "0" in ns:
        return False
    for i in range(1, len(ns)):
        if not ns[i] >= ns[i-1]:
            return False
    return True
def find(num, prints):
    ns = str(num)
    new = ""
    for i in range(1, len(ns)):
        if ns[i] < ns[i-1]:
            new = ns[0:i-1] + str(int(ns[i-1])-1)
            new += "9" * (len(ns)-len(new))
            if isTidy(int(new)):
                if prints:
                    print("Case #" + str(test+1) + ": " + str(int(new)))
                    return None
                else:
                    return None
            else:
                find(int(new), False)
                
for test in range(0, t):
    num = int(input())
    if isTidy(num):
        print("Case #" + str(test+1) + ": " + str(num))
    else:
        find(num, True)

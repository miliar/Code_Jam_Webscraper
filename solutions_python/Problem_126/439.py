def check(s):
    mo = ["a", "i", "u", "e", "o"]
    for val in s:
        if val in mo:
            return False
    return True

def calc(k, index):
    for i in index:
        if k <= i:
            return i

T = int(raw_input())
i = 1
while i <= T:
    s,n = raw_input().split(" ")
    n = int(n)
    j = 0
    length = len(s)
    index = []
    while j+n <= length:
        if check(s[j:j+n]):
            index.append(j)
        j += 1

    suma = 0
    for k in range(length-n+1):
        l = calc(k, index)
        if l != None:
            suma += (length - l - n + 1)
    print "Case #" + str(i) + ": " + str(suma)
    i += 1

def tidy_numb(n):
    for i in range(n, 0, -1):
        if list(str(i)) == sorted(list(str(i))):
            return i

n = int(input())
cas = ""
for i in range(1, n+1):
    cas+="Case #{0}: {1}".format(i, tidy_numb(int(input())))+"\n"
print(cas)


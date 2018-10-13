T = int(raw_input())

squares = [(i,i*i) for i in range(1,10**7 + 1)]
palindromes = []
for i,j in squares:
    if i == int(str(i)[::-1]) and j == int(str(j)[::-1]):
        palindromes.append(j)

def calc(A,B):
    count = 0
    for i in palindromes:
        if i >= A and i <= B:
            count += 1
        if i > B:
            break
    return count

for test in range(1, T + 1):
    A, B = [int(i) for i in raw_input().split()]

    print "Case #%d: %d" % (test, calc(A, B))

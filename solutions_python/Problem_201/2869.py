from decimal import Decimal, ROUND_HALF_UP

def simulate(n, k):
    stalls = [n]
    for i in range(k-1):
        curr = stalls.pop(0)-1
        stalls.append(Decimal(curr/2).quantize(0, ROUND_HALF_UP))
        stalls.append(int(curr/2))
        stalls.sort(reverse=True)
    curr = stalls.pop(0)-1
    return str(Decimal(curr/2).quantize(0, ROUND_HALF_UP)) + ' ' + str(int(curr/2))

def main():
    f1 = open('in.txt', 'r')
    f2 = open('out.txt', 'w')
    t = int(f1.readline())
    for i in range(0, t):
        data = f1.readline().split(' ')
        n = int(data[0])
        k = int(data[1])
        header = 'Case #' + str(i+1) + ': '
        f2.write(header + simulate(n, k) + '\n')
main()
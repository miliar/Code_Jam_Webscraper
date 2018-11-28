n = int(raw_input(''))

for i in range(n):
    num = int(raw_input(''))
    candys = raw_input('').split()
    count = 0
    candy_total = 0
    smallest = 10000000
    for j in range(num):
        count = count ^ int(candys[j])
        candy_total = candy_total + int(candys[j])
        smallest = min(smallest, int(candys[j]))
                       
    if count == 0:
        print '''Case #%d: %d''' % (i+1, candy_total - smallest)
        
    else:
        print '''Case #%d: NO''' % (i+1)

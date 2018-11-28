#! /usr/bin/python

def pat_sum(numbers, start, end):
    sum = numbers[start]
    for i in range(start+1, end+1):
        sum = sum^numbers[i]
    return sum

def sea_sum(numbers,start, end):
    sum = numbers[start]
    for i in range(start+1, end+1):
        sum = sum+numbers[i]
    return sum

def solve(n, numbers):
    found = False
    sum_out = 0
    numbers.sort()
    for j in range(0,n-1):
        if pat_sum(numbers,0,j)==pat_sum(numbers,j+1,n-1):
            if not found:
                sum_out = sea_sum(numbers,j+1,n-1)
            found = True                
            
    out = ''
    if not found:
        out = 'NO'
    else:
        out = '%d'%sum_out
    return out

if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        numbers = []
        line = f.readline().split()
        n = int(line[0])
        line = f.readline().split()
        for i in range(1,n+1):
            numbers.append(int(line[i-1]))
        answer = solve(n, numbers)
        g.write("Case #%d: %s\n" % (case,answer))
    f.close()
    g.close()
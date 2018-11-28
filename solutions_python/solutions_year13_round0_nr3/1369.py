import math

def reverse_int(n):
    return str(n)[::-1]

def search(n, dep, num):
    global TOTAL, DEPTH, A, B
    if 2*dep >= DEPTH :
        num1 = int(str(num) + reverse_int(num))
        if num >= 10 :
            num2 = int(str(num) + reverse_int(num/10))
        else:
            num2 = num
        while num1 % 10 == 0 and num1 != 0 :
            num1 = num1 / 10;
        while num2 % 10 == 0 and num2 != 0 :
            num2 = num2 / 10;
        if num1 * num1 <= B and num1 * num1 >= A:
            TOTAL += 1;
        if num2 * num2 <= B and num2 * num2 >= A:
            TOTAL += 1;
    else:
        for i in range(int(math.sqrt(n))):
            if i<3:
                search(n-i*i, dep+1, num*10 + i)

t =  input()
for i in range(t):
    A, B =  [int(x) for x in raw_input().split()]
    DEPTH = len(str(B)) / 2 + len(str(B)) % 2
    TOTAL = 0
    search(9, 0, 0) 
    if A <= 9 and B>=9 :
        TOTAL += 1
    print 'Case #' +str(i+1)+ ':', TOTAL


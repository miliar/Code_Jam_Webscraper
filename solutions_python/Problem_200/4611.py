number = int(input())

rj = []

def is_tidy(n) :
    digits = []
    while n > 0 :
        digits.append(n%10)
        n = int(n / 10)
    for i in range(len(digits)-1) :
        if digits[i] < digits[i+1] :
            return False
    return True


def last_tidy(n) :
    for i in range(n, 0, -1) :
        if is_tidy(i) :
            return i


while number > 0 :
    number-=1
    inp = int(input())
    rj.append(last_tidy(inp))

for i, val in enumerate(rj) :
    msg = "Case #" + str(i+1) + ": " + str(val)
    print(msg)

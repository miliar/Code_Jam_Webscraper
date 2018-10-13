import math 

def load_file(filename):
    return [int(row.replace('\n', '')) for row in open(filename).readlines()][1:]

def tidy_number(n):
    if n < 10:
        return n
    else:
        digits = []
        x = n
        while( x >= 10):
            d = x % 10
            x = math.floor(x//10)
            digits = [d] + digits
        digits = [x] + digits
        i = len(digits) - 2
        while(i >= 0):
            if digits[i] > digits[i + 1]:
                j = len(digits)-1
                while(j > i):
                    digits[j] = 9
                    j-=1

                digits[i] = digits[i] - 1
                if digits[i] == 0:
                    j = len(digits)-1
                    while(j >= i):
                        digits[j] = 9
                        j-=1
                    while(j >= 0):
                        if digits[j] > 1:
                            digits[j] = digits[j] - 1
                            break
                        else:
                            digits[j] = 9
                        j-=1
                    if j == -1:
                        digits = digits[1:]
                    break
            i -= 1
        num = ""
        for d in digits:
            num += str(d)
        return int(num)
            

results = [tidy_number(x) for x in load_file("tidy.in")]

f = open("tidy.out", "w")
i = 1
for r in results:
    f.write("Case #{}: {}\n".format(i, r))
    i+=1
f.close()
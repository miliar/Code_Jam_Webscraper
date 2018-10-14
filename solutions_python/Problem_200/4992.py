num = int(input())

def get_tidy_number(num):
    while num:
        number = str(num)
        if "".join(sorted(number)) == number:
            return number
        num -= 1

for i in range(num):
    val = int(input())
    print("Case #" + str(i+1) + ": " + get_tidy_number(val))
def is_tidy(num):
    num = str(num)
    num = num[::-1]
    if num.count("0"):
        return False
    current,last=int(num[0]),int(num[0])
    for i in num:
        current =int(i)
        if current != last:
            if last >= current:
                last = current
            else:
                return False

    return True

def last_tidy_before(num):
    while True:
        if is_tidy(num):
            return num
            break
        num = str(num)
        if num.count("0"):
            num = int(num) - int(num[num.find("0"):])
        else:
            num = int(num)
        num -=1

def main():
    T = int(input())
    for i in range(1,T+1):
        number= int(input())
        print("Case #{}: {}".format(i,last_tidy_before(number)))

main()

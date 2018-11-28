pos9 = 0
def print_case(case, ans):
    print("Case #"+str(case)+": " + str(ans))
#if last number is more than second last make last 9 and second last one less
def find_tidy(n,sub):
    global pos9
    l = len(n)
    if(l == 1):
        if(sub):
            if n == "1":
                return ""
            return str(int(n)-1)
        return n
    last = int(n[l-1])
    second_last = int(n[l-2])
    subr = False
    if(sub):
        if(second_last != 0):
            second_last -= 1
    result = ""
    if(last < second_last):
        if(second_last == 0):
            result = n[:l-2]+"99"
            subr = True
        else:
            result = n[:l-2]+str(second_last-1)+"9"
        pos9 = len(n)
    else:
        result = n
    return find_tidy(result[:l-1],subr)+result[l-1]
def is_tidy(n):
    last = "0"
    for c in n:
        if(int(c) < int(last)):
            return False
        last = c
    return True
def main():
    global pos9
    t = int(input())
    for i in range(t):
        n = input()
        pos9 = 0
        if is_tidy(n):
            result = n
        else:
            result = find_tidy(n,False)[:pos9] + "9"*(len(n)-pos9)
        print_case(i+1,result.lstrip("0"))
main()
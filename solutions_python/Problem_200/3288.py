def solve(num):
    
    while True:
        if len(num)==1: return num
        changed = False
        for i in range(1,len(num)):
            if num[i-1]>num[i]:
                changed = True
                num = str(int(num)-int(num[i:])-1)
                break
        if not changed: return num

if __name__ == "__main__":
    test_cases_num = int(input())
    for case_num in range(1, test_cases_num+1):
        given = input()
        print("Case #%i: %s" % (case_num, solve(given)))
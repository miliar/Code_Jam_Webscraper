def solve(d, n, k, s):
    longest=0
    for i in range(n):
        leftover=(d-k[i])/s[i]
        if leftover>longest: longest = leftover
    return d/longest

if __name__ == "__main__":
    test_cases_num = int(input())
    for case_num in range(1, test_cases_num+1):
        # given = input()
        d, n = [int(x) for x in input().split()]
        k=[]; s=[]
        for _ in range(n):
            ki, si = input().split()
            k.append(int(ki))
            s.append(int(si))
        # print (given.split())
        print("Case #%i: %f" % (case_num, solve(d, n, k, s)))
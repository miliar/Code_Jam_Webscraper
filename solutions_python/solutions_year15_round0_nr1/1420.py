def do_case(case_num, ss):
    result = 0
    curr_sum = 0
    for i in range(len(ss)):
        if i > curr_sum:
            result += i - curr_sum
            curr_sum = i
        curr_sum += int(ss[i])
    print "Case #%d: %d" % (case_num, result)

def main():
    T = int(raw_input())
    for case_num in range(1, T + 1):
        maxS, ss = raw_input().strip().split()
        do_case(case_num, ss)

if __name__ == "__main__":
    main()

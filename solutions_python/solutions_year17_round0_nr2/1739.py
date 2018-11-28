from sys import stdin

def get_answer():
    n = int(stdin.readline().strip())
    nums = [int(el) for el in str(n)]
    prev_increase = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[prev_increase] = nums[prev_increase] - 1
            for j in range(prev_increase + 1, len(nums)):
                nums[j] = 9
            break
        else:
            if nums[i] > nums[i - 1]:
                prev_increase = i
    return int("".join([str(el) for el in nums]))

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()

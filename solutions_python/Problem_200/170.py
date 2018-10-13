#Henry Maltby
#Code Jam 2017

def tidy_numbers(n):
    """
    Returns the largest integer less than or equal to n that has digits in 
    non-decreasing order.
    """
    nums = [int(x) for x in list(str(n))]
    threshold, j = nums[0], 0
    ans = n
    i = 1
    while i < len(nums):
        if nums[i] < threshold:
            nums[j] -= 1
            ans = int("".join([str(x) for x in nums[:j + 1]] + ['9'] * (len(nums) - j - 1)))
            break
        if nums[i] > threshold:
            threshold, j = nums[i], i
        i += 1
    return ans

def B():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('B-large.in')
    g = open('B-large.out', 'w')

    T = int(f.readline())
    for i in range(T):
        ans = str(tidy_numbers(int(f.readline())))
        g.write("Case #" + str(i + 1) + ": " + ans)
        if i != T - 1:
            g.write("\n")

B()

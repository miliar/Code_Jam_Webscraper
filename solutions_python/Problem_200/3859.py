FAIL = '\033[91m'
ENDC = '\033[0m'

def printError(error):
    print FAIL + str(error) + ENDC

def expect(expectValue, actualValue):
    if expectValue != actualValue:
        printError("%s is equal %s" % (expectValue, actualValue))


def run(input):
    
    # Check Sorted
    arr_nums = sorted(list(input))
    if "".join(arr_nums) == input:
        return input
    
    nums = [int(x) for x in input]
    result_nums = []
    last_index = -1
    for index in range(0, len(nums) - 1):
        if nums[index] > nums[index + 1]:
            last_index = index
            break

    nums[last_index] = nums[last_index] -1

    for index in range(last_index + 1, len(nums)):
        nums[index] = 9

    for index in reversed(range(1, last_index + 1)):
        if nums[index] < nums[index - 1]:
            nums[index] = 9
            nums[index - 1] = nums[index - 1] - 1

    result = "".join(str(i) for i in nums).replace('0','')
    return result

expect(run('123'), '123') 
expect(run('112'), '112')
expect(run('222'), '222')
expect(run('3344'), '3344')

expect(run('132'), '129')
expect(run('11110'), '9999')
expect(run('5544'), '4999')
expect(run('1000'), '999')
expect(run('1133445556667747'), '1133445556666999')
expect(run('9988'), '8999')

        

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()
  result = run(n)
  print "Case #{}: {}".format(i, result)
'''
  script finds the last tidy number before an input number n
  def tidy number: digits are sorted in non-decreasing order

  call script in this format: tidy_numbers.py < input_file_name > output_file_name
'''

#find the last tidy number counted before a given number n
def findLastTidyNumber(n):

    #get the digits of n in a list form
    digit_list = getDigits(n)

    #handle case where result will be all nines
    if digit_list.count(1) == len(digit_list) - 1 and digit_list[len(digit_list) - 1] == 0:
        return reduce(lambda x, y : x + y, [ 10**i * 9 for i in range(len(digit_list) - 1) ])

    #iterate through digits and decrement first digit that is greater than the digit following it
    i = 1
    same = 0
    lastDigit = digit_list[0]
    while i < len(digit_list):
        if digit_list[i] == lastDigit: same += 1
        else: 
            if digit_list[i] < digit_list[i - 1]: return changedInt(digit_list, i - same - 1)
            same = 0 
            lastDigit = digit_list[i]
        i += 1

    #n is tidy
    return n
    
#parse int from list where digit at index i is decremented, and all digits following it are replaced by 9s
def changedInt(digit_list, i):
    digit_list[i] -= 1
    i += 1
    while i < len(digit_list):
        digit_list[i] = 9
        i += 1
    return reduce(lambda x, y : x + y, [ 10**i * digit_list[len(digit_list) - i - 1] for i in range(len(digit_list)) ])

#decrement a given number of digits before the index
def decrementPrevious(digit_list, index, number):
    for num in range(number): digit_list[index - 1 - num] =9
    digit_list[index - 1 - number] -= 1

#return a list of the digits of an integer n in incrementing order
def getDigits(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n = n // 10
    answer.reverse()
    return answer

#parse input, call alrogithm, and format output
def solution():

    num = int(input())
    for i in range(1, num+1):
        print("Case #{}: {}".format(i, findLastTidyNumber(int(input()))))


solution()





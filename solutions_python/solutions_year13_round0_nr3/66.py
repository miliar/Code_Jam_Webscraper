import math
import sys
from bisect import bisect


def FairSquare(upper_bound):
  answers = set([])
  for left_part in range(1000):
    for center_digit in range(10):
      palindrome = long(str(left_part) + str(center_digit) + str(left_part)[::-1])
      if left_part == 0:
        palindrome = center_digit
      if palindrome == 0:
        continue      
      square = palindrome * palindrome
      if square <= upper_bound and str(square) == str(square)[::-1]:
        #print palindrome, square
        answers.add(square)
    palindrome = long(str(left_part) + str(left_part)[::-1])
    if palindrome == 0:
      continue
    square = palindrome * palindrome
    if square <= upper_bound and str(square) == str(square)[::-1]:
      #print palindrome, square
      answers.add(square)
  return answers


def FairSquareBig(upper_bound):
  if upper_bound < 10:
    return FairSquare(upper_bound)
  answers = FairSquare(10)
  for length in range(2, 51):
    half_length = length / 2
    palindrome = long("2" + "".join(["0"] * (length - 2)) + "2")
    square = palindrome * palindrome
    if square <= upper_bound and str(square) == str(square)[::-1]:
      answers.add(square)
    if length % 2 == 1:
      palindrome = long("2" + "".join(["0"] * ((length - 3) / 2)) + "1" + "".join(["0"] * ((length - 3) / 2)) + "2")
      square = palindrome * palindrome
      if square <= upper_bound and str(square) == str(square)[::-1]:
        answers.add(square)
      for dig in range(3):
        main_str = "1" + "".join(["0"] * ((length - 3) / 2)) + str(dig) + "".join(["0"] * ((length - 3) / 2)) + "1"        
        palindrome = long(main_str)
        square = palindrome * palindrome
        if square <= upper_bound and str(square) == str(square)[::-1]:
          answers.add(square)
        for i in range(1, (length - 1) / 2):
          copy_str = list(main_str)
          copy_str[i] = "1"
          copy_str[len(copy_str) - i - 1] = "1"
          palindrome = long("".join(copy_str))
          square = palindrome * palindrome
          if square <= upper_bound and str(square) == str(square)[::-1]:
            answers.add(square)
          if dig <= 1:
            for j in range(i + 1, (length - 1) / 2):
              copy_str2 = copy_str[:]
              copy_str2[j] = "1"
              copy_str2[len(copy_str2) - j - 1] = "1"
              palindrome = long("".join(copy_str2))
              square = palindrome * palindrome
              if square <= upper_bound and str(square) == str(square)[::-1]:
                answers.add(square)
              for k in range(j + 1, (length - 1) / 2):
                copy_str3 = copy_str2[:]
                copy_str3[k] = "1"
                copy_str3[len(copy_str3) - k - 1] = "1"
                palindrome = long("".join(copy_str3))
                square = palindrome * palindrome
                if square <= upper_bound and str(square) == str(square)[::-1]:
                  answers.add(square)
    else:
      main_str = "1" + "".join(["0"] * (length - 2)) + "1"
      palindrome = long(main_str)
      square = palindrome * palindrome
      if square <= upper_bound and str(square) == str(square)[::-1]:
        answers.add(square)
      for i in range(1, length / 2):
        copy_str = list(main_str)
        copy_str[i] = "1"
        copy_str[len(copy_str) - i - 1] = "1"
        palindrome = long("".join(copy_str))
        square = palindrome * palindrome
        if square <= upper_bound and str(square) == str(square)[::-1]:
          answers.add(square)
        for j in range(i + 1, length / 2):
          copy_str2 = copy_str[:]
          copy_str2[j] = "1"
          copy_str2[len(copy_str2) - j - 1] = "1"
          palindrome = long("".join(copy_str2))
          square = palindrome * palindrome
          if square <= upper_bound and str(square) == str(square)[::-1]:
            answers.add(square)
          for k in range(j + 1, length / 2):
            copy_str3 = copy_str2[:]
            copy_str3[k] = "1"
            copy_str3[len(copy_str3) - k - 1] = "1"
            palindrome = long("".join(copy_str3))
            square = palindrome * palindrome
            if square <= upper_bound and str(square) == str(square)[::-1]:
              answers.add(square)
  return answers

      


def main():
  #all_answers = FairSquare(long("100000000000000"))
  all_answers = FairSquareBig(long("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))
  list_answers = list(all_answers)  
  list_answers.sort()
  """
  list_answers2 = list(all_answers2)  
  list_answers2.sort()
  if list_answers != list_answers2:    
    print "answers:"
    for answer in list_answers:
      print long(math.sqrt(answer))
    print "answers2:"
    for answer in list_answers2:
      print long(math.sqrt(answer))   
  """
  if 12345678987654321 in list_answers:
    print "YES"
  else:
    print "NO"
  fin = open("C.in", "r")
  fout = open("C.out", "w")
  tests = int(fin.readline())
  for test_index in range(tests):
    (A, B) = map(int, fin.readline().strip().split(" "))
    if test_index % 100 == 0:
      print A, B
    result = bisect(list_answers, B) - bisect(list_answers, A - 1)
    fout.write("Case #%d: " % (test_index + 1) + str(result) + "\n")
    if test_index % 100 == 0:
      print result
  fin.close()
  fout.close()


if __name__ == '__main__':
  main()
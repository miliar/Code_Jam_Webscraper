import sys
import collections

num_rows = 4
user_row = []
num_tests = int(raw_input())
for i in range(num_tests):
   first_row = int(raw_input()) 
   for j in range(num_rows):
      row = sys.stdin.readline()
      if j is first_row  - 1:
         user_row = map(int, row.split(' '))
   second_row = int(raw_input())
   for j in range(num_rows):
      row = sys.stdin.readline()
      if j is second_row - 1:
         temp_row = map(int, row.split(' '))
         user_row = [num for num in user_row if num in temp_row]
         if len(user_row) == 1:
            print 'Case #' + str(i + 1) + ': ' + str(user_row[0])
         elif len(user_row) > 1:
            print 'Case #' + str(i + 1) + ': ' + 'Bad magician!'
         elif len(user_row) == 0:
            print 'Case #' + str(i + 1) + ': ' + 'Volunteer cheated!'
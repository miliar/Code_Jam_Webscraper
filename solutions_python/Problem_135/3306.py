#reads num lines from stdin 
def skip_lines(num):
  while num:
    raw_input()
    num -= 1

#reads every row and returns row row_num
def get_row(row_num):
  skip_lines(row_num-1)
  row = raw_input()
  skip_lines(4-row_num)
  return map(int, row.split())


#Format string for answer output
answer = 'Case #{0}: {1}'

num_cases = int(raw_input())
for case in range(1,num_cases+1):
  
  #Get the rows that matter
  first_answer = int(raw_input())
  first_row = get_row(first_answer)
  second_answer = int(raw_input())
  second_row = get_row(second_answer)
  
  #The intersection of the rows makes up the possible cards
  intersection = list(set(first_row) & set(second_row))

  #Print the appropriate answer
  if len(intersection) == 0:
    print answer.format(case, 'Volunteer cheated!')
  elif len(intersection) == 1:
    print answer.format(case, intersection[0])
  else:
    print answer.format(case, 'Bad magician!')

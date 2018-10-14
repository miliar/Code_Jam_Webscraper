def read_data(filename):
  with open(filename, 'rb') as infile:
    num_of_cases = int(infile.readline().strip())
    case_list = []
    for i in range(num_of_cases):
      ans1 = int(infile.readline().strip())
      mat1 = []
      for count in range(4):
        row = [int(ele) for ele in infile.readline().strip().split(' ')]
        mat1.append(row)
      ans2 = int(infile.readline().strip())
      mat2 = []
      for count in range(4):
        row = [int(ele) for ele in infile.readline().strip().split(' ')]
        mat2.append(row)
      case_list.append((ans1, mat1, ans2, mat2))
  return case_list


# given two arrangement of cards
# and the volunteer's answer to the two questions
#       1. the row number of the selected card in the first arrangement
#       2. the row number of the selected card in the second arrangement

# determine: 1. which card the volunteer chose
#            2. if more than one card, the magician did a bad job
#            3. if not card, the volunteer cheated

def every_round(ans1, mat1, ans2, mat2):
  row1 = mat1[ans1-1]
  row2 = mat2[ans2-1] 
  hit_list = []
  for idx1 in range(4):
    for idx2 in range(4):
      if row1[idx1] == row2[idx2]:
        hit = row2[idx2]
        hit_list.append(hit)
  return hit_list

def magician(filename):
  case_list = read_data(filename)
  with open('output.txt', 'wb') as outfile:
    counter = 1 
    for ans1, mat1, ans2, mat2 in case_list:
      result = every_round(ans1, mat1, ans2, mat2)
      num = len(result)
      if num == 0:
        outfile.write('Case #' + str(counter) + ': Volunteer cheated!\n')
      elif num == 1:
        outfile.write('Case #' + str(counter) + ': ' + str(result[0]) + '\n')
      else:
        outfile.write('Case #' + str(counter) + ': Bad magician!' + '\n')
      counter += 1


if __name__ == "__main__":
  magician('A-small-attempt2.in.txt')
  

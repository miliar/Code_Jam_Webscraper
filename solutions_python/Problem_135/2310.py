#!/usr/bin/env python
## File: Problem_A.py
## Author: Yunqi Zhang
## Email: yunqi@umich.edu

def get_content(file_path):
  fp = open(file_path)
  content = []
  for line in fp:
    content.append(line)
  return content

def main():
  content = get_content("QA_input.txt")
  # Number of cases
  number_of_cases = int(content[0].strip())
  i = 1
  for j in range(number_of_cases):
    # answer to the first question
    row_first = int(content[i].strip())
    first_items = content[i + row_first].strip().split()
    i = i + 5
    # answer to the second question
    row_second = int(content[i].strip())
    second_items = content[i + row_second].strip().split()
    i = i + 5
    # output to the question
    both_items = [item for item in first_items if item in second_items]
    if len(both_items) == 0:
      print("Case #{0}: Volunteer cheated!".format(j + 1))
    elif len(both_items) == 1:
      print("Case #{0}: {1}".format(j + 1, both_items[0]))
    else:
      print("Case #{0}: Bad magician!".format(j + 1))

if __name__ == "__main__":
  main()

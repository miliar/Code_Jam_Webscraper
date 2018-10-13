#!/usr/bin/env python
## File: Problem_B.py
## Author: Yunqi Zhang
## Email: yunqi@umich.edu

def get_content(file_path):
  fp = open(file_path)
  content = []
  for line in fp:
    content.append(line)
  return content

def main():
  content = get_content("QB_input.txt")
  # Number of cases
  number_of_cases = int(content[0].strip())
  for i in range(1, number_of_cases + 1):
    items = content[i].strip().split()
    C = float(items[0])
    F = float(items[1])
    X = float(items[2])
    # Keep track of time
    basetime = 0.0
    j = 0
    prev_time = X / 2.0
    while True:
      basetime = basetime + C / (2.0 + j * F)
      time = basetime + X / (2.0 + (j + 1) * F)
      if time > prev_time:
        break
      prev_time = time
      j = j + 1
    print("Case #{0}: {1:.7f}".format(i, prev_time))

if __name__ == "__main__":
  main()

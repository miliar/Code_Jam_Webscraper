import sys
from pprint import pprint

def get_num_input():
  num = sys.stdin.readline()
  try:
    num = int(num)
  except ValueError:
    print("Error : first line of input is not an int")
    exit()
  return num

def line_to_item(line):
  item = {}
  first_line = line.split(" ")
  # extract D and N
  try:
    item["D"] = int(first_line[0])
    item["N"] = int(first_line[1])
  except ValueError:
    print("could not extract D and N")
  # extract competing horses
  item["horses"] = []
  for i in range(item["N"]):
    n_line = sys.stdin.readline().split(" ")
    try:
      item["horses"].append({
        "K": int(n_line[0]),
        "S": int(n_line[1])})
    except ValueError:
      print("could not extract " + str(i) + "th horse")
  return item

def compute(item):
  t_arrive = []
  for i in range(item["N"]):  #for each competing horses
    cur_horse = item["horses"][i]
    t_arrive.append((item["D"] - cur_horse["K"]) / cur_horse["S"])
  return item["D"] / max(t_arrive)
      

def main():
  num = get_num_input()

  #MAIN LOOP
  i = 0
  for line in sys.stdin:
    i += 1
    print("Case #" + str(i) + ": ", end='')
    item = line_to_item(line)
    pprint(compute(item))

main()


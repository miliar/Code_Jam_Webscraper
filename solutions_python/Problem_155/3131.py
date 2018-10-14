def run(input_f, output_f):
  f = open(input_f)
  o = open(output_f, "w")
  case = int(f.readline())

  for i, line in enumerate(f.readlines()):
    max_s, s = line.split(" ")
    result = solve(int(max_s), s)
    o.write("Case #%d: %d\n"%(i+1, result))

  o.close()

def solve(max_s, s):
  standing_num = 0
  friend_num = 0
  for i in range(max_s+1):
    need_friend_num = i - standing_num
    if need_friend_num > 0:
      friend_num += need_friend_num
      standing_num += need_friend_num
    standing_num += int(s[i])

  return friend_num

if __name__ == "__main__":
  import sys
  run(sys.argv[1], sys.argv[2])
    

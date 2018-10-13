#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# author Ladislav Vrbsky
# Google Code Jam 2017
# Round 1B
# Problem A.


def horse_speed(d, n, k, s):
  max_time = 0

  for horse in range(n):
    t_i = get_completion_time(d-k[horse], s[horse])
    max_time = max(max_time, t_i)

  speed = d/max_time

  return speed

def get_completion_time(dist, velocity):
  return dist/velocity

def main():
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    d,n = [int(inp) for inp in input().split(" ")]  # read a list of integers, 2 in this case
    k, s = [], []
    for i_n in range(n):
      i_k, i_s = [int(inp) for inp in input().split(" ")]
      k.append(i_k)
      s.append(i_s)

    print("Case #{}: {}".format(i, horse_speed(d, n, k, s)))

if __name__ == '__main__':
  main()
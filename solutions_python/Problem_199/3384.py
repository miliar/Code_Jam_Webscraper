import heapq
from math import floor, ceil

def main():
  with open("out.txt","w") as out:
    with open("in.txt","r") as file:
      num_tests = int(file.readline().rstrip())
      for b in range(num_tests):
        data = file.readline().rstrip().split()
        cakes = list(data[0])
        size = int(data[1])

        cnt = 0
        flag = True

        for i in range(len(cakes)):
          if cakes[i] == '-':
            cnt += 1

            if i + size - 1 >= len(cakes):
              out.write("CASE #{}: IMPOSSIBLE\n".format(b+1))
              flag = False
              break

            for a in range(size):
              cakes[i+a] = '-' if cakes[i+a] == '+' else '+'

        if flag:
          out.write("CASE #{}: {}\n".format(b+1, cnt))


if __name__ == '__main__':
  main()
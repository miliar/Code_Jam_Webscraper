import heapq
from math import floor, ceil

def main():
  with open("out.txt","w") as out:
    with open("in.txt","r") as file:
      num_tests = int(file.readline().rstrip())
      for b in range(num_tests):
        vals = file.readline().rstrip().split()
        stalls = int(vals[0])
        people = int(vals[1])

        print b

        h = []
        heapq.heappush(h, -stalls)

        for i,x in enumerate(range(people)):
          a = heapq.heappop(h)
          heapq.heappush(h, ceil((a+1)/2.))
          heapq.heappush(h, ceil((a+1)/2.) - (a+1) % 2)

          if i == people-1:
            out.write("Case #{}: {} {}\n".format(b+1, -int(ceil((a+1)/2.) - (a+1) % 2), -int(ceil((a+1)/2.))))


if __name__ == '__main__':
  main()
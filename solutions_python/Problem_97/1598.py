def is_recycled(a, b):
  a_str = str(a)
  b_str = str(b)

  for i in range(1, len(a_str)):
    recycled_a = ""
    recycled_a += a_str[i:]
    recycled_a += a_str[:i]
    if recycled_a == b_str:
      return True
  
  return False

def main():
  f = open("recyclednumbersoutput.txt", "w")
  
  n = input()
  for i in range(n):
    line = raw_input().split()
    a = int(line[0])
    b = int(line[1])

    counter = 0
    for u in range(a, b + 1):
      for j in range(u + 1, b + 1):
        if (is_recycled(u, j)):
          counter += 1
    f.write("Case #%d: %d\n" % (i + 1, counter))
  
  f.close()

if __name__ == "__main__":
  main()
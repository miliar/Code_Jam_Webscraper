def solve(data):
  # Work backwards
  digits = list(data.strip())
  while 1:
    valid = True
    for d in range(0, len(digits) - 1):
      if digits[d] > digits[d + 1]:
        valid = False
        digits[d] = str(int(digits[d]) - 1)
        for x in range(d + 1, len(digits)):
          digits[x] = "9"
        break;
    if valid:
      return int(''.join(digits))
      

def main():
    inp = input("")
    file = open(inp, 'r')

    count = 1
    first = True 
    for l in file:
        if (first):
            first = False
            continue
        print("Case #{}: {}".format(count, str(solve(l))))
        count += 1

main()
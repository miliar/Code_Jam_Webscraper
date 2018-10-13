def turnside (string, step, count):
    while 1:
        if string.count('+')== len(string):
            return count
        else:
            start = string.index('-')
            if start <= (len(string)-step):
                count += 1
                turn = ['+' if i == '-' else '-' for i in string[start:start+step]]
                new = list(string[:start] + turn + string[start+step:])
                string = new
            else:
                return 'IMPOSSIBLE'

t = int(input())
for i in range(1, t + 1):
  line = input()
  string, k = list(line.split(" ")[0]),int(line.split(" ")[1])
  count =0
  if string.count('+')== len(string):
      print("Case #{}: {}".format(i, 0))
  else:
      print("Case #{}: {}".format(i, turnside(string, k, 0)))

def binary(n):
  #n -= 1
  
  moves = []
  while n > 1:
    if n % 2 == 0:
      moves.append(True) # right
    else:
      moves.append(False) # left
    n //= 2
  return moves
  

def answer(n, k):
  for is_right in binary(k):
    n -= 1
    if is_right:
      n = n // 2 + n % 2
    else:
      n = n // 2

  n -= 1
  return n // 2 + n % 2, n // 2

def case_number(i):
    return "Case #" + str(i + 1) + ":"

if __name__ == "__main__":
    for i in range(int(input())):
        n, k = map(int, input().split())
        x, y = answer(n, k)
        print(case_number(i), x, y)

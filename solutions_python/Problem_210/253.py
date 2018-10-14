def MyFunc(x):
  return x

if __name__ == '__main__':
  T = int(input())
  for i in range(1, T + 1):
    S = input()
    output = MyFunc(S)
    print('Case #{}: {}'.format(i, output))

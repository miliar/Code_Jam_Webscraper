# -*- coding: utf-8 -*-


def calc(start, end):
  ans = 0
  for i in range(start, end + 1):
    target = list(str(i))
    while 1:
      head = target.pop(0)
      target.append(head)
      if target[0] == '0':
        continue
      replaced = int(''.join(map(str, target)))
      if i == replaced:
        break
      if start <= replaced <= end and replaced <= i:
        ans += 1
  return ans


def main():
  f = open('C-small-attempt0.in', 'r')
  lines = f.readlines()
  for i, line in enumerate(lines[1:]):
    inputs = line.split()
    ans = calc(int(inputs[0]), int(inputs[1]))
    print 'Case #' + str(i + 1) + ': ' + str(ans)

if __name__ == '__main__':
    main()

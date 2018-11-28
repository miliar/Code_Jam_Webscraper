import sys

fin = sys.stdin

def main():
  num_cases = int(fin.readline().strip())
  for i in range(num_cases):
    case_num = i + 1
    mask, flip_size = fin.readline().strip().split()
    mask = convert_mask(mask)
    flip_size = int(flip_size)

    count = 0

    for index in range(len(mask) - flip_size + 1):
      if not mask[index]:
        # flip!
        for j in range(flip_size):
          mask[index + j] = not mask[index + j]
        count += 1

    success = all(mask[-(flip_size - 1):])

    if not success:
      output = 'IMPOSSIBLE'
    else:
      output = str(count)

    print('Case #%d: %s' % (case_num, output))

def convert_mask(mask):
  mask = mask.strip()
  rv = [False for i in range(len(mask))]
  for (i, c) in enumerate(mask):
    if c == '+':
      rv[i] = True
  return rv


if __name__ == '__main__':
  main()

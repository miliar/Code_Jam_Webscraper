if __name__ == '__main__':
  T = input()

  for case in xrange(1, T+1):
    row1 = input()
    rows1 = [[int(x) for x in raw_input().split()] for _ in xrange(4)]

    row2 = input()
    rows2 = [[int(x) for x in raw_input().split()] for _ in xrange(4)]

    out = [i for i in rows1[row1-1] if i in rows2[row2-1]]

    if len(out) > 1:
      print 'Case #' + str(case) + ': Bad Magician!'
    elif len(out) == 0:
      print 'Case #' + str(case) + ': Volunteer cheated!'
    else:
      print 'Case #' + str(case) + ': ' + str(out[0])

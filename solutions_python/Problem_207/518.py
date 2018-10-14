T = int(input())
for i in range(1, T + 1):
  N, R, O, Y, G, B, V = map(int, input().split(' '))
  if O == 0 and G == 0 and V == 0:
    if R == 0 and Y == 0 and B == 0: ret = ''
    elif R == 1 and Y == 0 and B == 0: ret = 'R'
    elif R == 0 and Y == 1 and B == 0: ret = 'Y'
    elif R == 0 and Y == 0 and B == 1: ret = 'B'
    elif R + Y < B or Y + B < R or B + R < Y: ret = 'IMPOSSIBLE'
    elif R + Y == B: ret = 'RB' * R + 'YB' * Y
    elif Y + B == R: ret = 'YR' * Y + 'BR' * B
    elif B + R == Y: ret = 'BY' * B + 'RY' * R
    elif (R + Y + B) % 2 == 0:
      ret = 'RB' * ((R + B - Y) // 2) + 'RY' * ((R + Y - B) // 2) + 'BY' * ((B + Y - R) // 2)
    else:
      ret = 'RB' * ((R + B - Y - 1) // 2) + 'RY' * ((R + Y - B + 1) // 2) + 'BY' * ((B + Y - 1 - R) // 2) + 'B'
  print('Case #{}: {}'.format(i, ret))

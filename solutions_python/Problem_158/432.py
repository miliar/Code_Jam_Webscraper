ALWAYS_WIN = 'GABRIEL'
CAN_LOSE = 'RICHARD'

CASES = {
  (2,1,2): ALWAYS_WIN,
  (2,1,4): ALWAYS_WIN,
  (2,2,2): ALWAYS_WIN,
  (2,2,3): ALWAYS_WIN,
  (2,2,4): ALWAYS_WIN,
  (2,3,4): ALWAYS_WIN,
  (2,4,4): ALWAYS_WIN,
  (3,1,3): CAN_LOSE,
  (3,2,3): ALWAYS_WIN,
  (3,3,3): ALWAYS_WIN,
  (3,3,4): ALWAYS_WIN,
  (4,1,4): CAN_LOSE,
  (4,2,4): CAN_LOSE,
  (4,3,4): ALWAYS_WIN,
  (4,4,4): ALWAYS_WIN,
}


def solve(line):
  x,r,c = line
  if x == 1:
    return ALWAYS_WIN
  if x > r and x > c:
    return CAN_LOSE
  if (r*c) % x != 0:
    return CAN_LOSE
  return CASES[(x,r,c) if r <= c else (x,c,r)]

if __name__ == "__main__":
  from codejam import CodeJam, parsers
  CodeJam(parsers.ints, solve).main()
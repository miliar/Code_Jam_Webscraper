import sys

if __name__ == "__main__":
  f = sys.stdin
  if len(sys.argv) >= 2:
      fn = sys.argv[1]
      if fn != '-':
          f = open(fn)

  num_cases = int(f.readline())

  # Do the thing
  for case in range(1, num_cases+1):
      case_params = f.readline().rstrip()
      s_max = case_params.split()[0]
      
      audience = [int(x) for x in list(case_params.split()[1])]
      
      standing = 0
      invited = 0
      for level, level_size in enumerate(audience):
        # print("Case %s: %s standing, level %s has %s people" % (case, standing, level, level_size))
        if standing >= level:
          standing += level_size
        elif level_size > 0:
          new_invites = level - standing
          invited += new_invites
          standing += new_invites + level_size

      print("Case #%s: %s" % (case, invited))
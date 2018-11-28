from string import split

def calc(data):
  (n, pd, pg) = data
  if pg == 100:
    return output(pd == 100)
  elif pg == 0:
    return output(pd == 0)
  else:
    for d in range(1, min(n, 100)+1):
      if d*pd % 100 == 0:
        return output(True)
    return output(False)

def output(tf):
  if tf:
    return "Possible"
  else:
    return "Broken"

def main(fileprefix):
  data = parse(fileprefix + '.in')
  f = open(fileprefix + '.out', 'w')
  i = 1;
  for trial in data:
    export('Case #{0:d}: {1:s}'.format(i, calc(trial)), f)
    i += 1;
  f.close()

def parse(filename):
  f = open(filename, 'r')
  t = int(f.readline())
  data = []
  for iline in range(t):
    data.append(tuple(map(int, split(f.readline()))))
  f.close()
  return data

def export(str, file):
  print str
  file.write(str + '\n')


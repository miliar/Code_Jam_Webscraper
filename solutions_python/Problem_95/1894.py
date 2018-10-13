def inp(f_name = 'input.txt'):
  fin = open(f_name)
  t = int(fin.readline())
  inps = []
  for i in range(t):
     line = fin.readline()
     inps.append(line)
  fin.close()
  return inps

def out(res, f_name = 'out.txt'):
  fout = open(f_name, 'w')
  i = 1
  for r in res:
    tmp = 'Case #%d: %s\n' %(i, r)
    i += 1
    fout.write(tmp)
  fout.close()

char_map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 
	'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
	'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n',
	'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
	'x': 'm', 'z': 'q', 'q': 'z'}

def process(inps):
    res = []
    for line in inps:
	ls = line.split()
	for i in range(len(ls)):
	    ls[i] = get_word(ls[i])
	res.append(' '.join(ls))
    return res

def get_word(w):
    ls_c = list(w)
    ls_c = [char_map[x] for x in ls_c]
    return ''.join(ls_c)
	
	

def main():
  import sys
  fin_name = 'input.txt'
  fout_name = 'out.txt'
  try:
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]
  except:
    pass
  inps = inp(fin_name)
  res = process(inps)
  out(res, fout_name)

if __name__ == '__main__':
  main()

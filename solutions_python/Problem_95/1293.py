import sys

def main():
  if len(sys.argv)<=1:
      print 'Usage: python A.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fout = open(arg[:-3]+'out', 'w')
  fr = f.readline()
  fr = fr[:-1]
  english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','']
  googlerese = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' ','\n']
  for i in range(int(fr)):
    line = f.readline()
    translated = ''
    for char in line:
      translated += english[googlerese.index(char)]
    fout.write("Case #"+str(i+1)+": "+translated)
    if(i<int(fr)-1):
      fout.write('\n')
  return

if __name__ == '__main__':
  main()
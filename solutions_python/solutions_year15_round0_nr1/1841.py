def main(x):
  max_shy=int(x.split(' ')[0])
  aud_list=x.split(' ')[1]
  cur_aud=0
  inv_guest=0
  total_guest=0
  for i in xrange(len(aud_list)):
    
    
    if cur_aud<max_shy and cur_aud<i and int(aud_list[i])<>0:
      inv_guest=-cur_aud+i
      total_guest+=inv_guest
      cur_aud=int(aud_list[i])+cur_aud+inv_guest
    else:
      cur_aud=int(aud_list[i])+cur_aud
    
  return total_guest
  
if __name__ == '__main__':
	import sys
	inpf=open('1.txt')
	outp=open('output.txt','w')
	N = int(inpf.readline())
	for i in xrange(N):
		inp=inpf.readline().strip()
		res = main(inp)
		outp.write("Case #%d: %s\n" % (i + 1, res))
	outp.close()
	
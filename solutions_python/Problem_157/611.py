import sys

mul_dict = {
  '1': {'1':'1','i':'i','j':'j','k':'k'},
  'i': {'1':'i','i':'1','j':'k','k':'j'},
  'j': {'1':'j','i':'k','j':'1','k':'i'},
  'k': {'1':'k','i':'j','j':'i','k':'1'}
  }
mul_neg = {
  '1': {'1':False,'i':False,'j':False,'k':False},
  'i': {'1':False,'i':True ,'j':False,'k':True },
  'j': {'1':False,'i':True ,'j':True ,'k':False},
  'k': {'1':False,'i':False,'j':True ,'k':True }
  }
def mul(a,b):
  if (a[0]==b[0]):
    positive_ans = True
  else:
    positive_ans = False
  ans = mul_dict[a[1]][b[1]]
  if mul_neg[a[1]][b[1]]:
    positive_ans = not positive_ans
  return (positive_ans,ans)

def mul_str(s):
  ret = (True,'1')
  for c in s:
    ret = mul(ret,(True,c))
  return ret

def do_case(arg1,arg2):
  repeat = int(arg1[1])
  input_str = arg2 * repeat
        
  product1=(True,'1')
  s1e_valid=[]
  for s1e in range(len(input_str)-2):
    product1 = mul(product1,(True,input_str[s1e]))          # split after split1
    if product1 == (True,'i'):
      s1e_valid.append(s1e)
  
  product3=(True,'1')
  s3s_valid=[]
  for s3s in range(len(input_str)-1,1,-1):
    product3 = mul((True,input_str[s3s]),product3)
    if product3 == (True,'k'):
      s3s_valid.append(s3s)
  
  s3s_valid = reversed(s3s_valid)
  for s1e in s1e_valid:
    product2=(True,'1')
    for s2e in range(s1e+1,len(input_str)-1):
      product2=mul(product2,(True,input_str[s2e]))
      if product2[0] and product2[1] == 'j' and (s2e+1) in s3s_valid: return True
  return False



ncases = int(sys.stdin.readline())
for i in range(ncases):
  out="Case #%i: "%(i+1)
  arg1=sys.stdin.readline().rstrip('\n').split(' ')
  arg2=sys.stdin.readline().rstrip('\n')
  
  if do_case(arg1,arg2):
    out += 'YES'
  else:
    out += 'NO'
  print(out)
  
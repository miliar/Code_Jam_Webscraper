def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return is_palindrome(x) and is_palindrome(apositiveint)


def is_palindrome(seq):
    word = str(seq)
    if word == "".join(reversed(word)):
        return True
    return False

fname = "C-small-attempt1.in"
with open(fname) as f:
    content = f.readline().strip()
    #print content
    T = int(content);
    for i in range(T):
        line = f.readline().strip().split(" ")
        A,B = int(line[0]),int(line[1])
        j = A
        count = 0
        while(j<=B):
            if j==1:
                count+=1
                j+=1
                continue
            if(is_square(j)):
                count+=1
                #print j
            j+=1
        print "Case #"+str(i+1)+": "+str(count)

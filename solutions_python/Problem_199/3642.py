import sys
def func(arr, w):

    s = [0]*len(arr)
    sum = ans = 0
    for i in range(len(arr)):
        s[i] += (arr[i]+sum)%2 != 1
        sum += s[i]- (s[i-w+1] if (i>= w-1) else 0)
        ans += s[i]

        if(i > len(arr)-w and s[i] != 0):
            return 'IMPOSSIBLE'
    return str(ans)
        
        


fname = 'input2.txt'
with open(fname) as f:
    content = f.readlines()
    lines = content[1:]
	
orig_stdout = sys.stdout
fout = open('out1.txt', 'w')
sys.stdout = fout
for j,line in enumerate(lines):
    st, w = line.split()
    arr = [(1 if i =='+' else 0) for i in st]
    print 'Case #'+str(j+1)+': '+func(arr, int(w))
sys.stdout = orig_stdout
f.close()
fout.close()

	

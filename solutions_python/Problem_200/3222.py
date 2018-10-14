from os.path import expanduser

problem = "B-large"
path = expanduser('C:/Users/SWAPNIL/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'

def f(x):
    s=str(x)
    if x<int(s[0]*len(s)):
        return True   
        
with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	lines = fin.read().splitlines()
	case = 1

	for l in lines[1:]:
	    s=str(l)
            ans=""
            if len(s)==1:
                ans=str(s)
            else:
                for i in range(0,len(s)-1):
                    if f(int(s[i:])):
                        ans+=str(int(s[i])-1)+"9"*(len(s)-i-1)
                        break
                    elif i<(len(s)-2):
                        ans+=s[i]
                    else:
                        ans+=s[i]+s[i+1]      
            output = 'Case #%d: %s\n' % (case,str(int(ans)))
	    fout.write(output)
	    case += 1
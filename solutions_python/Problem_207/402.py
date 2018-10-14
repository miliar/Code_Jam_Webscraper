from os.path import expanduser
import math

problem = "B-small-attempt0 (1)"
path = expanduser('C:/Users/SWAPNIL/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'
      
with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
    lines = fin.read().splitlines()
    case = 1
    for l in lines[1:]:
	N,R,O,Y,G,B,V=map(int,l.split(' '))
        ans=""
        if ((R>Y+B) or (Y>R+B) or (B>R+Y)):
            ans="IMPOSSIBLE"
        else:    
            m=max(R,Y,G)
            if m==R:
                ans+="R"
                R-=1
            elif m==Y:
                ans+="Y"
                Y-=1
            else:
                ans+="B"
                B-=1
            while R>0 or Y>0 or B>0:
                if ans[-1]=="R":
                    if Y>=B:
                        ans+="Y"
                        Y-=1
                    else:
                        ans+="B"
                        B-=1
                elif ans[-1]=="Y":
                    if R>=B:
                        ans+="R"
                        R-=1
                    else:
                        ans+="B"
                        B-=1
                elif ans[-1]=="B":
                    if R>=Y:
                        ans+="R"
                        R-=1
                    else:
                        ans+="Y"
                        Y-=1      
        output = 'Case #%d: %s\n' % (case,ans)
	fout.write(output)
	case += 1
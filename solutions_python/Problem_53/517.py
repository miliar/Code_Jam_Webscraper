# Snapper-chain Google-Code Jam 2010 (World)
# Javier Fernandez (javierfdr@gmail.com)


# Returns wheter the chain is totally connected or not
def snap(chain,first_plug):

    first_plug[1] = not(first_plug[1])
    prev = first_plug
    for s in chain:
        # toggle if was connected
        if (s[0]):
            s[1]=not(s[1])
            
            # connected if previous is now connected and on
        if (prev[0] and prev[1]):
            s[0] = True
        else:
            s[0] = False
        prev = s
            
    return (prev[0] and prev[1])

def snapper_chain(n,k):
    
    # list of pairs [power,on-off]
    first_plug = [True,False]
    chain =  [[False,False] for r in range(1,n)]    
    res = False
    for s in range(0,k):        
        res = snap(chain,first_plug)

    if (res):
        return 'ON'
    else:
        return 'OFF'
        
import sys

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())


for c in range(1,num_cases+1):
    tok = map(int,in_file.readline().strip('\n').split())
       
    case = 'Case #'+str(c)+': '
    res = snapper_chain(tok[0],tok[1])
    out_file.write(case+res+'\n')

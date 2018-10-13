import sys
import re



def solve(A, motes):
    if A == 1:
        return len(motes)

    ans = 0
    
    while len(motes) > 0:
        while len(motes) > 0 and A > motes[0]:
            A += motes.pop(0)
        if len(motes) == 0:
            return ans
        
        temp = A
        temp2 = 0
        while temp <= motes[0]:
            temp = 2*temp-1
            temp2 += 1

        if temp2 < len(motes):
            while A <= motes[0]:
                A = 2*A-1
                ans += 1
        else:
            return ans + len(motes)
    
    return ans

        
def main():
    f = open('A-small-attempt2.in', 'r')
    output = open('A-small-attempt2.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    numcases = int(lines[0])
    i = 1
    
    for numcase in range(1, numcases+1):
        [A, N] = [int(z) for z in lines[i].split(' ')]
        i += 1
        motes = [int(z) for z in lines[i].split(' ')]
        i += 1
        motes.sort()
        
        ans = solve(A, motes)
        output.write('Case #' + str(numcase) + ': ' + str(ans) +'\n')
        
    output.close()
    
    

if __name__ == '__main__':
    main()


def solve():
    with open(r'd:\output.out','w') as output:
        with open(r'd:\A-small-attempt1.in','r') as file:
            numofcase = int(file.readline().strip())
            for i in range(numofcase):
                ans1 = int(file.readline().strip())
                for _ in range(ans1-1):
                    file.readline()
                ansset1 = set(file.readline().strip().split(' '))
                for _ in range(4-ans1):
                    file.readline()
                ans2 = int(file.readline().strip())
                for _ in range(ans2-1):
                    file.readline()
                ansset2 = set(file.readline().strip().split(' '))
                for _ in range(4-ans2):
                    file.readline()
                result = ansset1 & ansset2
                if len(result)==1:
                    output.write('Case #%d: %s\n' % (i+1,result.pop()))
                elif len(result)>1:
                    output.write('Case #%d: Bad magician!\n' % (i+1))
                elif len(result)==0:
                    output.write('Case #%d: Volunteer cheated!\n' % (i+1))

solve()

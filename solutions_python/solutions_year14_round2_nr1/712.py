import os, subprocess

class Input:
    @staticmethod
    def parse():
        if False:
            problem='problem.txt'
        else:
            path=os.path.join(os.environ['HOME'],'Downloads')
            problem=subprocess.check_output(['ls','-t',path]).split('\n')[0]
            problem=os.path.join(path,problem)
        print(problem)
        Input.file=open(problem,'r')
        return int(Input.file.readline())

    @staticmethod
    def case():
        for i in range(0, Input.parse()):
            yield Input.parseCase()

    @staticmethod
    def parseCase():
        case = Case()
        case.count = int(Input.file.readline())
        case.strings=[]
        for i in range(0, case.count):
            string=Input.file.readline().strip()
            case.strings.append(string)
        return case


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


class Output:
    @staticmethod
    def log(result):
        try:
            Output.file==None
        except:
            Output.file=open('solution.txt','w')
            Output.index=0
        Output.index+=1



        result=str(result)


        result='Case #'+str(Output.index)+': '+result
        print(result+'\n\n'
                     '********************************************\n')
        Output.file.write(result+'\n')


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


class Case:
    def __str__(self):
        output=[]
        for i in sorted(set(dir(self))-(set(dir(Case())))):
            output.append(str(i)+" : "+str(getattr(self, i)))
        return '\n'.join(output)

    def solve(self):
        print(str(self))

        # Init result
        result="GOOD"

        canonical=set()
        repetition=[]
        for string in self.strings:
            can=""
            index=0
            rep=0
            for c in string:
                if can=="":
                    can+=c
                    rep=1
                elif c != can[-1]:
                    can+=c
                    try:
                        repetition[index].append(rep)
                    except:
                        repetition.append([rep,])
                    rep=1
                    index+=1
                else:
                    rep+=1
            try:
                repetition[index].append(rep)
            except:
                repetition.append([rep,])

            canonical.add(can)
        if len(canonical) != 1:
            return "Fegla won"

        move=0
        for rep in repetition:
            avg = round(sum(rep)/len(rep))
            for i in rep:
                move+=int(abs(i-avg))
        return move

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


def main():
    for case in Input.case():
        result = case.solve()
        Output.log(result)

main()
class Input:
    @staticmethod
    def parse():
        Input.file=open('problem.txt','r')
        #Input.file=open('test.txt','r')
        Input.caseCount=int(Input.file.readline())

    @staticmethod
    def case():
        for i in range(0, Input.caseCount):
            yield Input.parseCase()

    @staticmethod
    def parseCase():
        case = Case()
        case.weightCount=int(Input.file.readline())
        case.naomi = [ float(i) for i in Input.file.readline().strip('\n').split(' ') ]
        case.ken= [ float(i) for i in Input.file.readline().strip('\n').split(' ') ]
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

    def ken_war_strategy(self, ken_hand, naomi):
        for play in ken_hand:
            if play > naomi:
                return play
        return ken_hand[0]

    def naomi_war_strategy(self,naomi_hand):
        return naomi_hand.pop()

    def naomi_dwar_strategy(self,naomi_hand, ken_hand):
        ken_hand.sort()
        ken_hand.reverse()

        min_ken=min(ken_hand)
        max_ken=max(ken_hand)

        play=naomi_hand[0]
        for w in naomi_hand:
            if w > min_ken:
                naomi_hand.remove(w)
                return max_ken

        return naomi_hand.pop()

    def solve(self):
        self.ken.sort()
        self.naomi.sort()

        print(str(self))

        # Setup War game
        naomi_hand=list(self.naomi)
        ken_hand=list(self.ken)
        naomi_hand.sort()
        ken_hand.sort()
        war_score=0

        # Play game
        for i in range(0, self.weightCount):
            naomi = self.naomi_war_strategy(naomi_hand)
            ken = self.ken_war_strategy(ken_hand, naomi)
            ken_hand.remove(ken)
            if naomi>ken:
                war_score+=1


        # Setup D War game
        naomi_hand=list(self.naomi)
        ken_hand=list(self.ken)
        naomi_hand.sort()
        ken_hand.sort()
        dwar_score=0

        # Play game
        for i in range(0, self.weightCount):
            naomi = self.naomi_dwar_strategy(naomi_hand, list(ken_hand))
            ken = self.ken_war_strategy(ken_hand, naomi)
            ken_hand.remove(ken)
            print(str(naomi),'vs',str(ken))
            if naomi>=ken:
                dwar_score+=1
                print('Naomi wins')
            else:
                print('Ken wins')

        result=str(dwar_score)+' '+str(war_score)
        return result


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


def main():
    caseCount = Input.parse()
    for case in Input.case():
        result = case.solve()
        Output.log(result)

main()
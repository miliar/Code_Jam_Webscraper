class Bots:

    def __init__(self, nactions, orange_actions, blue_actions):

        self.nactions = nactions
        self.action = 1

        self.o_actions = orange_actions
        self.b_actions = blue_actions

        self.o_loc = 1
        self.b_loc = 1

        if self.o_actions == []:
            self.o_next = None
        else:
            self.o_next = self.o_actions.pop(0)

        if self.b_actions == []:
            self.b_next = None
        else:
            self.b_next = self.b_actions.pop(0)


    def _go_orange(self):

        if self.o_next == None:
            return "done"

        # at button?
        if self.o_loc == self.o_next[1]:
            # check if it's time to press it
            if self.action == self.o_next[0]:
                # press it
                self.action += 1

                # get next action
                if self.o_actions == []:
                    self.o_next = None
                else:
                    self.o_next = self.o_actions.pop(0)
                
                # indicate you pressed it
                return "pressed"

            # it wasn't time yet
            return "waiting"


        # in front of button
        if self.o_loc > self.o_next[1]:
            # move back
            self.o_loc -= 1
            return "back"

        # behind button
        if self.o_loc < self.o_next[1]:
            # move back
            self.o_loc += 1
            return "forward"

        return "WTF?"


    def _go_blue(self, ostat):

        if self.b_next == None:
            return "done"

        # at button?
        if self.b_loc == self.b_next[1]:
            # check if it's time to press it
            if self.action == self.b_next[0] and ostat != "pressed":
                # press it
                self.action += 1

                # get next action
                if self.b_actions == []:
                    self.b_next = None
                else:
                    self.b_next = self.b_actions.pop(0)
                
                # indicate you pressed it
                return "pressed"

            # it wasn't time yet
            return "waiting"


        # in front of button
        if self.b_loc > self.b_next[1]:
            # move back
            self.b_loc -= 1
            return "back"

        # behind button
        if self.b_loc < self.b_next[1]:
            # move back
            self.b_loc += 1
            return "forward"

        return "WTF?"




    def perform(self):
        
        nsteps = 0
        while (self.action <= self.nactions):
            ostat = self._go_orange()
            bstat = self._go_blue(ostat)
            nsteps += 1

        return nsteps



if __name__ == "__main__":

    out_fmt = "Case #{}: {}\n"

    with open("A-large.in", "r") as fin, open("A-large.out", "w") as  fout:
        ncases = int(fin.readline())
        for case in range(1, ncases + 1):
            
            raw_case = fin.readline().split(" ")

            blue_actions = []
            orange_actions = []
            nactions = int(raw_case.pop(0))

            for n in range(1, nactions + 1):
                color = raw_case.pop(0)
                if color == "B" : blue_actions.append((n,int(raw_case.pop(0))))
                if color == "O" : orange_actions.append((n,int(raw_case.pop(0))))
                
            b = Bots(nactions, orange_actions, blue_actions)
            fout.write(out_fmt.format(case, b.perform()))

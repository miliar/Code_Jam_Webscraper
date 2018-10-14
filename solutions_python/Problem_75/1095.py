#5
#0 0 2 EA
#1 QRI 0 4 RRQR
#1 QFT 1 QF 7 FAQFDFQ
#1 EEZ 1 QE 7 QEEEERA
#0 1 QW 2 QW

class Magicka:
    def analyze(self, path):
        file = open(path)
        nrOfLines = file.readline()
        for i,case in enumerate(file):
            yield "Case #%d: %s" % (i+1, self.analyze_case(case))
            
    def analyze_case(self, case):
        vals = case.split(" ")
        nrOfBase = (int)(vals.pop(0))
        baseElements = {}
        for i in range(nrOfBase):
            b = vals.pop(0)
            baseElements[b[0]]={"partner":b[1],"form":b[2]}
            baseElements[b[1]]={"partner":b[0],"form":b[2]}
        nrOfOpposingForces = (int)(vals.pop(0))
        for i in range(nrOfOpposingForces):
            b = vals.pop(0)
            if not baseElements.has_key(b[0]):
                baseElements[b[0]]={}
            if not baseElements.has_key(b[1]):
                baseElements[b[1]]={}
            baseElements[b[0]]["enemy"]=b[1]
            baseElements[b[1]]["enemy"]=b[0]
        nrOfInvokees = (int)(vals.pop(0))
        resList = []
        baseNumberString = vals.pop(0)
        for i in range(nrOfInvokees):
            value = baseNumberString[i]
            if value in baseElements:
                currBase = baseElements.get(value)
                hadPartner = False
                deleted = False
                if len(resList)>0:
                    if "partner" in currBase:
                        if resList[-1]==currBase.get("partner"):
                            resList[-1]=currBase.get("form")
                            hadPartner=True
                    if "enemy" in currBase and not hadPartner:
                        if resList.count(currBase.get("enemy"))>0:
                            resList = []
                            deleted = True
                if not hadPartner and not deleted:
                    resList.append(value)
            else:
                resList.append(value)
        retString = "["
        retString = '['+', '.join(resList)+']'
        return retString

cases = Magicka()
for i in cases.analyze("B-small-attempt3.in"):
    print i            
            
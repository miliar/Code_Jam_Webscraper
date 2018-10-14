import sys

class AlienLanguage:
    
    def __init__(self, words):
        self.words = words

    def getCount(self, case):
        clist = []
        multi = False
        tmp = ""
        for c in case:
            if c == "(":
                multi = True
            elif c == ")":
                multi = False
            else:
                tmp += c
            if not multi:
                clist.append(tmp)
                tmp = ""
        
        cnt = 0
        for word in self.words:
            if self.match(word, clist):
                cnt += 1
        return cnt
    
    def match(self, word, clist):
        for i in range(len(word)):
            if word[i] not in clist[i]:
                return False
        return True

def main():
    nums = sys.stdin.readline().split()
    words = []
    for i in range(int(nums[1])):
        words.append(sys.stdin.readline())
    ins = AlienLanguage(words)
    for i in range(int(nums[2])):
        print ("Case #%d: %d" %(i+1, ins.getCount(sys.stdin.readline())))


if __name__ == "__main__":
    main()
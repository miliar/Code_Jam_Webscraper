# -*- coding: utf-8 -*-
import gcj.base
import math

IDX_GGLER_COUNT = 0
IDX_SURPRISING_COUNT = 1
IDX_P = 2
IDX_SCORES_TOP = 3
class C(gcj.base.GcjBase):

    def solve(self):
        print self.q
        i = 1
        for q in self.q:
            #print q
            ans = 0
            n =  self.nextPalindrome(q['min'] -1)
            while n <= q['max']:
                if self.isFlatSqrt(n):
                    ans += 1
                n =  self.nextPalindrome(n)
            text = "Case #" + str(q['no']) + ": " + str(ans)
            #print text
            self.out_lines.append(text);
        return

    def nextPalindrome(self,num):
        length=len(str(num))
        oddDigits=(length%2!=0)
        leftHalf=self.getLeftHalf(num)
        middle=self.getMiddle(num)
        if oddDigits:
            increment=pow(10, length/2)
            newNum=int(leftHalf+middle+leftHalf[::-1])
        else:
            increment=int(1.1*pow(10, length/2))
            newNum=int(leftHalf+leftHalf[::-1])
        if newNum>num:
            return newNum
        if middle!='9':
            return newNum+increment
        else:
            return self.nextPalindrome(self.roundUp(num))
        
    def getLeftHalf(self,num):
        return str(num)[:len(str(num))/2]

    def getMiddle(self,num):
        return str(num)[(len(str(num))-1)/2]

    def roundUp(self,num):
        length=len(str(num))
        increment=pow(10,((length/2)+1))
        return ((num/increment)+1)*increment
    
    def isP(self,num):
        strnum = str(num)
        if strnum == strnum[::-1]:
            return True
        else:
            return False
        
    def isFlatSqrt(self,num):
        sqr = math.sqrt(num)
        isqr = int(sqr)
        return sqr == isqr and self.isP(isqr)
        
    def readInFile(self):
        gcj.base.GcjBase.readInFile(self)
        self.line_num = int(self.in_lines[0])
        del self.in_lines[0];
        self.q = []
        qi = 0
        i = 1
        for l in self.in_lines:
            if l == '':
                continue
            p = l.split(' ')
            self.q.append({'no': i ,'min': int(p[0]),'max': int(p[1])})
            i += 1
        return
    
    def isWin(self,data,sb):
        if data == '':
            return False
        #g = gcj.grid.Grid()
        #g.makeGrid(4,4)
        #g.fillGrid(data)
        #g.showGrid()
        data = data.replace('T', sb)
        print data
        winline = sb + sb + sb + sb
        # row
        s = [0,4,8,12]
        for i in s:
            print i
            line = data[i] + data[i+1] + data[i+2] + data[i+3]
            if line == winline:
                return True
        # column
        s = [0,1,2,3]
        for i in s:
            line = data[i] + data[i+4] + data[i+8] + data[i+12]
            if line == winline:
                return True

        # diagonal
        if (data[0] + data[5] + data[10] + data[15] == winline) or (data[3] + data[6] + data[9] + data[12] == winline):
            return True
        return
        


c = C()
#b.mizumashi(1000)
c.execute()

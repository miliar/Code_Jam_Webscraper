# -*- coding: utf-8 -*-
import gcj.base

"""
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing two positive integers K and N, representing the number of keys you start with and the number of chests you need to open.

This is followed by a line containing K integers, representing the types of the keys that you start with.

After that, there will be N lines, each representing a single chest. Each line will begin with integers Ti and Ki, indicating the key type needed to open the chest and the number of keys inside the chest. These two integers will be followed by Ki more integers, indicating the types of the keys contained within the chest.

最初の行はテストケースの数T
各テストケースは
K N 
Kの数だけ取得できる鍵を表した行がある

K:最初に持っているキーの数
N:あけるチェストの数

3
----
1 4
1 最初の鍵
1 0
1 2 1 3
2 0
3 1 2
---
3 3
1 1 1 最初の鍵
1 0
1 0
1 0
---
1 1
2 最初の鍵
1 1 1

"""
class D(gcj.base.GcjBase):

    def solve(self):
        """
        1.手に入れるべき鍵の探索
        2.全部手元にあるときは１から順番にあける
        
        3.現在あけることのできる鍵の探索する
            チェストをあけることで手にはいる鍵と失う鍵を更新
        4.1に戻る
        
        """
        i = 1
        for q in self.q:
            # 1.
            #print self.useKey([1,2,3],1);
            ret = self.open(q,q['keys'],q['chests'],[])
            if len(ret) == q['chest_count']:
                print ret
                text = "Case #" + str(q['no']) + ": " + ' '.join([str(t) for t in ret])
            else:
                text = "Case #" + str(q['no']) + ": IMPOSSIBLE"
            print text
            self.out_lines.append(text)
            #print i
            #print canopen
            i += 1
        return 


    def getKeyNeeds(self,chests):
        needs = []
        for c in chests:
            needs.append(c['open_key'])
        return needs

    def getOpenOrder(self,q):
        canopen = self.checkCanOpenAll(q['keys'],q['chests'])
        if canopen:
            needs = self.getKeyNeeds(q['chests'])
            return needs
        return

    def useKey(self,keys,key):
        if key in keys:
            i = keys.index(key)
            del keys[i]
            #print "use key:" + key
            return keys
        return keys 
                

    def open(self,q,skeys,schests,sorder):
        """
        1.あけるべきチェストが無く、チェストの数＝開けた数ならorderを返す
        2.今あるキーで全部開けられるなら順番にあける。orderを返す
        2.もう開けられるチェストがなければIMPOSIBLE
        3.開けられるチェストが1つしかなければそれを開ける
        4.開けられるチェストが複数あればそれぞれについて試行する
        """
        keys = skeys[:]
        chests = [x for x in sorted(schests[:],key=lambda x:x['number'])]
        order = sorder[:]
        if len(chests) == 0 and q['chest_count'] == len(order):
            #print str(q['no']) + ": 全部開いている"
            return order
        #print "order"
        #print order
        needs = self.getKeyNeeds(chests)
        canopen = self.checkCanOpenAll(keys[:],chests[:])
        if canopen:
            #print str(q['no']) + ": 全部開けられる"
            ox = order + [x['number'] for x in chests]
            print ox
            return ox

            #print order
            #print  (order + [x['number'] for x in chests])
            #return self.open(q,[],[],ox)
        else:
            ava = [x for x in chests if (x['open_key'] in keys) == True]
            if len(ava) == 0:
                print str(q['no']) + "不可能"
                return []
            elif len(ava) == 1:
                print str(q['no']) + ":１つだけ開けられる"
                left_chests = [x for x in chests if x['number'] != ava[0]['number']]
                mykeys = self.useKey(keys[:],ava[0]['open_key'])
                mykeys = mykeys + ava[0]['in_key']
                order.append(ava[0]['number'])
                self.open(q,mykeys,left_chests,order)
            else:
                print str(q['no']) + "複数開けられる"
                print ava
                for c in ava:
                    print "try: " + c['number']
                    left_chests = [x for x in chests if x['number'] != c['number']]                    
                    mykeys = self.useKey(keys[:],c['open_key'])
                    mykeys = mykeys + c['in_key']
                    order.append(c['number'])
                    o = self.open(q,mykeys,left_chests,order)
                    if len(o) == q['chest_count']:
                        print "END"
                        return o
                    else:
                        print "del"
                        del order[len(order) -1]
                return []
            return []

    def getCanOpenChest(self,keys,chests):
        can = []
        for c in chests:
            if c['open_key'] in key:
                can.append(c)
        return c
    
    def checkCanOpenAll(self,key,chests):
        needs = self.getKeyNeeds(chests)
        for n in needs:
            if n in key:
                i = key.index(n)
                del key[i]
            else:
                return False
        return True
        
    def readInFile(self):
        gcj.base.GcjBase.readInFile(self)
        self.line_num = int(self.in_lines[0])
        del self.in_lines[0];
        ci = 0
        self.q = []
        qno = 1
        for i in self.in_lines:
            if i  == '':
                continue
            if ci == 0:
                p = i.split(' ')
                data = {'no': qno ,'key_count': int(p[0]), 'chest_count': int(p[1])}
                qno += 1
                ci = -1
            elif ci == -1:
                data['keys'] = i.split(' ')
                data['chests'] = []
                ci = 1
            else:
                ck = i.split(' ')
                in_key_count = int(ck[1])
                if in_key_count == 0:
                    in_key = []
                else:
                    in_key = ck[in_key_count * -1:]
                cdata = {'number': str(ci),'open_key':ck[0],'in_key_count':in_key_count,'in_key':in_key}
                data['chests'].append(cdata)
                ci += 1
            if ci > data['chest_count']:
                self.q.append(data)
                ci = 0
        return
    
        


d = D()
#b.mizumashi(1000)
d.execute()

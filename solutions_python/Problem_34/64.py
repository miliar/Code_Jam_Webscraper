#!/usr/bin/python
import sys
import copy

##szfile = './A-small.in.txt'
##szfile = './A-small-attempt0.in'
##szfile_output = './A-small.output.txt'
szfile = './A-large.in'
szfile_output = './A-large.output.txt'

class Price:
    def __init__(self):
        pass

    def RunFile(self) :
# using file set
        f = open(szfile,'rb')
        s = f.read()
# ---
        l_s = s.splitlines()
        str_line_1 = l_s[0]
        l_s = l_s[1:]
        L, D, N = str_line_1.split()
        print L, D, N
        L = int(L);        D = int(D);        N = int(N);
        l_word = l_s[0:D]
        l_s = l_s[D:]
##        print l_word
        l_ptn = l_s[0:N]
##        print l_ptn

        l_output = []
        trie = self.BuildTree(l_word)
        for i, str_ptn in enumerate(l_ptn):
            num = i+1;
            result = self.GetCase(trie, str_ptn)
            l_output.append('Case #%(num)d: %(result)d' %locals())
        print l_output

# using file set
        f = open(szfile_output,'wb')
        f.write('\n'.join(l_output))
# ----

    def BuildTree(self, l_word):
        tree_root = {}

        for str_word in l_word:
            tree_nd = tree_root
            for ch in str_word:
                if(tree_nd.has_key(ch) == False):
                    tree_child_nd = {}
                    tree_nd[ch] = tree_child_nd
                tree_nd = tree_nd[ch]
##        print tree_root
        return tree_root


    def GetCase(self, tree_root, str_ptn):
        ncase = 0;
        l_entry = []
        str_temp = str_ptn;
        while(str_temp != ''):
            str_entry = ''
            if(str_temp[0] == '('):
                str_temp = str_temp[1:]
                while(str_temp[0] != ')'):
                    str_entry += str_temp[0]
                    str_temp = str_temp[1:]
                str_temp = str_temp[1:]
            else:
                str_entry = str_temp[0]
                str_temp = str_temp[1:]
            l_entry.append(str_entry)
##        print 'entry:', l_entry

        ncase = self.Trace(tree_root, l_entry)
        return ncase

    def Trace(self, tree_node, l_ptn):
        ncase = 0;

        if(len(l_ptn) == 0 and tree_node == {}):
            return 1;
        elif (len(l_ptn) == 0):
            return 0;
        for x in l_ptn[0]:
            if(tree_node.has_key(x)):
                ncase += self.Trace(tree_node[x], l_ptn[1:])

        return ncase;

if __name__ == "__main__":
    cm = Price()
##    cm.GetMinExtract(['code', 'jam', 'foo', 'bar', 'google',], [20, 15, 40, 30, 60,])
##    cm.GetMinExtract(['code', 'jam', 'foo', 'bar', 'google',], [20, 15, 40, 50, 60,])

##    A = ['code', 'foo']
##    B = ['jam']
##    print A < B
    A = ['needle', 'hair']
    B = ['needle', 'knee']
    print sorted(A) < sorted(B)

    cm.RunFile()




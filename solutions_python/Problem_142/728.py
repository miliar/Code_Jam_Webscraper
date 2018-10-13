#!/usr/bin/python
#
# This script was written by Norio TAKEMOTO 2014-5-4.

##################################
#infname='input_sample.dat'
#outfname='output_sample.dat'
infname='A-small-attempt0.in'
outfname='outputsmallA000.dat'
##################################

import re


def solve_small(str1, str2):

    flg_possible=False
    nmov=0
    j1=0
    j2=0
    c1=str1[j1]
    c2=str2[j2]
    if c1!=c2:
        return (flg_possible, nmov)
    while j1<len(str1) and j2<len(str2):
        if c1==c2:
            j1+=1
            j2+=1
            if j1==len(str1) and j2==len(str2):
                flg_possible=True
                break
            elif j1==len(str1):
                print 'branch1'
                for i2 in range(j2, len(str2)):
                    if c2==str2[i2]:
                        nmov+=1
                        flg_possible=True
                    else:
                        flg_possible=False
                        break
                break
            elif j2==len(str2):
                print 'branch2'
                for i1 in range(j1, len(str1)):
                    if c1==str1[i1]:
                        nmov+=1
                        flg_possible=True
                    else:
                        flg_possible=False
                        break
                break
            c1p=c1
            c2p=c2
            c1=str1[j1]
            c2=str2[j2]
        elif c1==c2p:
            nmov+=1
            j1+=1
            if j1==len(str1):
                for i2 in range(j2, len(str2)):
                    print 'branch 3'
                    if c2==str2[i2]:
                        nmov+=1
                        flg_possible=True
                    else:
                        flg_possible=False
                        break
                break
            c1p=c1
            c1=str1[j1]
        elif c2==c1p:
            nmov+=1
            j2+=1
            if j2==len(str2):
                print 'branch4'
                for i1 in range(j1, len(str1)):
                    if c1==str1[i1]:
                        nmov+=1
                        flg_possible=True
                    else:
                        flg_possible=False
                        break
                break
            c2p=c2
            c2=str2[j2]
        else: 
            break

    return (flg_possible, nmov)


infile=open(infname,'r')
numcaseT=int(infile.readline())
list_numstrN=[]
listlist_str=[]
for jcase in range(numcaseT):
    numstrN=int(infile.readline())
    list_numstrN.append(numstrN)
    list_str=[]
    for jstr in range(numstrN):
        list_str.append(infile.readline().strip())
    listlist_str.append(list_str) 
infile.close()

outfile=open(outfname,'w')
for jcase in range(numcaseT):
    (flg_possible, nmov)=solve_small(listlist_str[jcase][0], listlist_str[jcase][1])
    if flg_possible:
        outfile.write('Case #%i: %i\n'%(jcase+1,nmov))
    else:
        outfile.write('Case #%i: Fegla Won\n'%(jcase+1))
outfile.close()

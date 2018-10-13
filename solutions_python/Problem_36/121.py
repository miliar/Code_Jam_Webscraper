gcj welcome
system:sage

{{{id=1|

///
}}}

{{{id=36|
welcome='welcome to code jam'
///
}}}

{{{id=18|
letters = set(welcome)
///
}}}

{{{id=34|

///

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/notebook/sage_notebook/worksheets/admin/5/code/83.py", line 7, in <module>
    infile = open(DATA+'problem.in')
IOError: [Errno 2] No such file or directory: '/home/notebook/sage_notebook/worksheets/admin/5/data/problem.in'
}}}

{{{id=20|
letterposition = {}
for l in letters:
    letterposition[l]=[]
for cnt in range(len(welcome)):
    l = welcome[cnt]
    letterposition[l].append(cnt)
///
}}}

{{{id=42|
infile = open(DATA+'problemlarge.in')
lines = infile.readlines()
N = int(lines[0].strip())
infile.close()
///
}}}

{{{id=24|
outfile = open('welcomelarge.out', 'w')
///
}}}

{{{id=26|
for casecnt in range(N):
    teststring = lines[casecnt+1].strip()
    subcnt = list(welcome)
    for cnt in range(len(welcome)):
        subcnt[cnt]=0
    for testletter in teststring:
        if testletter in letters:
            for pos in letterposition[testletter]:
                if pos == 0:
                    subcnt[0]=subcnt[0]+1
                else:
                    subcnt[pos]=(subcnt[pos]+subcnt[pos-1])%10000
    outfile.write('Case #'+str(casecnt+1)+': '+str(subcnt[-1]+10000)[1:]+'\n')
///
}}}

{{{id=35|
outfile.close()
///
}}}

{{{id=45|

///
}}}

{{{id=44|
lines
///

['100\n', 'aoot dm co dodeln\n', 'wwelccommme too code jaamm\n', 'welcome tto code jam\n', 'welclomce toe tco dced  jaaamm\n', 'w\n', 'welco  cme two mecode de jam\n', 'welcomee tt o codej jam\n', 'welcomoe tto cto dece tjtam\n', 'wweelcommet tco coede jjam\n', 'wewellcome  tt o codde  jjjamm\n', 'wweecolcome  to coode jam\n', 'q welcome to code jam p\n', 'welccomem to code j amm\n', 'wwellecoomme too codeo dj aamm\n', 'welcoooooooooome to code jam\n', 'wellcome too code  jjam\n', 's amtm ledelcmcod\n', 'welcome to code jam\n', 'ntaclemgomejowz\n', 'wellcomee t o coedej jam\n', 'wenrlgcsomef tzgro cqiodeu jam\n', 'wwellcome to code jaam\n', 'j  ojeoa m eaow x\n', 'wmt cco eleelt tlewdeeode ex\n', 'ejeomll cxeeemt js\n', 'welcome to codejam\n', 'to cemcaeaewbdb\n', 'welcoome to code jajam\n', 'wwelcome oto code jam\n', 'welcomme  t o ocode edj aam\n', 'welcpome to  h cccgxode jafmmm\n', 'wwelcome tooo ccode jam\n', 'welccocmom eo  to codee jaam\n', 'welcome to code jam\n', 'pmm lcleeeeie et\n', 'wwelcoome  tto cooddedej jdamm\n', 'xttc dwoe atdmmlmf\n', 'q o coowwdec czoz\n', 'yawmfacsaewec w\n', 'weelclomem to tcoodeede jajaam\n', 'wweellccoommee to code qps jam\n', 'bm welocomeo tov lcoede  jeams\n', 'welcomde to code jamj\n', 'weelocomeeo to  ccodde jamm\n', 'wellcoomee  to ccooede jam\n', 'welcocme t o co cdde jaamm\n', 'weellcoemet to ocode  jajamm\n', 'weelcccoomee  toc code  jam\n', 'q cjmcs oe o dlecw\n', 'wweclcooeme too code jamm\n', 'welcome to code jam\n', 'nmmto mt ee  twach\n', 'wewlcomlme ltto  ocodje jam\n', 'weelcoomme tot  cocdeede jaam\n', 'welcooeme t o code jam\n', 'welcome  to code jjamm\n', 'weeleocoemeem  to  ccode jjamm\n', 'weelclcomee to c codeee jajmm\n', 'wellcomee to coodej jam\n', 'wellcomme t oo code jam\n', 'lmacdw otme aoe  c cmcjomxm\n', 'weelccome otoo code  jaam\n', 'dwtcdooaoecte   s\n', 'welcome to code jamjamjamjam\n', 'z\n', 'weeclmcome  to c docodej jmam\n', 'iwmocmme c daeh\n', 'wwelcoeme to code jam\n', 'ymt ooajj dccav\n', 's cewlecw eevoh\n', 'wdelc ome to tce odde jam\n', 'wwelcocomem to ocode ejajmm\n', 'iwoelvccommel to code r jam\n', 'wwwelllcome tto code jjjjjamm\n', 'welcome to coode jjam\n', 'ldtwle mbcnccdtr\n', 'zewltwbceet awmcetv\n', 'wedlcoomme  to coded  jjaam\n', 'wwelcome wto  cooduect eej dam\n', 'welccome tto code jam\n', 'welcome to code jamm\n', 'kam l aoelmoivh\n', 'wwellcoomje  to  ccdode  j aam\n', 'welllcooomeee ttto coddde jam\n', 'mcjadeeetmjteoo te oletoh\n', 'weelcome etto coode jjaam\n', 'wwellcocomme ttoo ocode  jam\n', 'wwelcoome to code jamm\n', 'elcomew elcome to code jam\n', 'welcome  to codee ajam\n', 'weelcomme to ccode jam\n', 'not really a welcome message\n', 'weellcome tto cocde ejjaam\n', 'welcome to code jam\n', 'wnelcccooooome to coooddde jam\n', 'wwellclcomee ttoo cocoede jamm\n', 'vjatcj wm ejoaledof\n', 'you are welcomed to code jam\n', 'welcomee to code jam\n', 'wwwwwwwelcome to code jjjam\n']
}}}

{{{id=46|

///
}}}
#print "Case #%d: %d" % (t, mtime)
import fileinput
import re
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
for line in fileinput.input():
    if not fileinput.isfirstline():
        reps = {'y':'-a'}
        reps2 = {'e':'-o'}
        reps3 = {'d':'-s'}
        #,'o':'e','c':'f','v':'g','x':'h','d':'i','u':'j','i':'k','g':'l','l':'m','b':'n','k':'o','r':'p','t':'r','n':'s','w':'t','j':'u','p':'v','f':'w','m':'x','a':'y','q':'z'
        
        #correct = replace_all(line,reps)
        #correct = replace_all(correct,reps2)
        #correct = replace_all(correct,reps3)
        correct = re.sub('(?<!-)y','-a',line)
        correct = re.sub('(?<!-)e','-o',correct)
        correct = re.sub('(?<!-)d','-s',correct)
        correct = re.sub('(?<!-)c','-e',correct)
        correct = re.sub('(?<!-)f','-c',correct)
        correct = re.sub('(?<!-)a','-y',correct)
        correct = re.sub('(?<!-)g','-v',correct)
        correct = re.sub('(?<!-)h','-x',correct)
        correct = re.sub('(?<!-)i','-d',correct)
        correct = re.sub('(?<!-)j','-u',correct)
        correct = re.sub('(?<!-)k','-i',correct)
        correct = re.sub('(?<!-)l','-g',correct)
        correct = re.sub('(?<!-)m','-l',correct)
        correct = re.sub('(?<!-)n','-b',correct)
        correct = re.sub('(?<!-)b','-h',correct)
        correct = re.sub('(?<!-)o','-k',correct)
        correct = re.sub('(?<!-)p','-r',correct)
        correct = re.sub('(?<!-)r','-t',correct)
        correct = re.sub('(?<!-)s','-n',correct)
        correct = re.sub('(?<!-)t','-w',correct)
        correct = re.sub('(?<!-)u','-j',correct)
        correct = re.sub('(?<!-)v','-p',correct)
        correct = re.sub('(?<!-)w','-f',correct)
        correct = re.sub('(?<!-)x','-m',correct)
        correct = re.sub('(?<!-)z','-q',correct)
        correct = re.sub('(?<!-)q','-z',correct)
        correct = re.sub('-','',correct)
        print "Case #%d: %s" % (fileinput.lineno() - 1, correct)
        #print line.replace('y','a')
        #print correct
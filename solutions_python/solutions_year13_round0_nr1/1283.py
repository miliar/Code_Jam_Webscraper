import sys, re
size = int(sys.stdin.readline())
lines = [sys.stdin.readline()[0:4] for i in range(size*5-1)]

for case in range(size):
    begin = case*5
    if begin+4 <= len(lines):
        game = '/'.join(lines[begin:(begin+5)])

        if re.match('(.{5})*[XT]{4}.*|.*([XT].{4}){3}[XT].*|.*([XT][^/].{4}){3}[XT].*|.*([XT]([^/][^/]/|[^/]/[^/]|/[^/][^/])){3}[XT].*', game) != None:
            print 'Case #%d: X won' % (case+1)
        elif re.match('(.{5})*[OT]{4}.*|.*([OT].{4}){3}[OT].*|.*([OT][^/].{4}){3}[OT].*|.*([OT]([^/][^/]/|[^/]/[^/]|/[^/][^/])){3}[OT].*', game) != None:
            print 'Case #%d: O won' % (case+1)
        elif re.match('.*\..*', game) != None:
            print 'Case #%d: Game has not completed' % (case+1)
        else:
            print 'Case #%d: Draw' % (case+1)

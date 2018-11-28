#! /usr/bin/env python
# -*- coding: utf8 -*-
# vim:ts=4:sw=4:expandtab:
# vi:ts=4:sw=4

def do_calc(comb_rule, oppo_rule, invk_elems):
    result = []
    while len(invk_elems) > 0:
        cur_elem = invk_elems.pop(0)
        result.append(cur_elem)
        if len(result) > 1:
            last_two = result[-2:]
            last_two.sort()
            for cond in comb_rule:
                if last_two == cond[0]:
                    del result[-2:]
                    result.append(cond[1])
                    cur_elem = cond[1]
        for cond in oppo_rule:
            if cur_elem in cond:
                ban_canc = cond[:]
                ban_canc.remove(cur_elem)
                if ban_canc[0] in result:
                    del result[:]

    return result


def main():
    for c in range(input()):
        comb_rule = []
        oppo_rule = []
        invk_num = 0
        invk_elems = ''
        inarg = map( str, raw_input().split() )

        for i in range( int( inarg.pop(0) ) ):
            rule_str = inarg.pop(0)
            from_elem = [rule_str[0],rule_str[1]]
            from_elem.sort()
            comb_rule.append( [from_elem,rule_str[2]] )

        for i in range( int( inarg.pop(0) ) ):
            rule_str = inarg.pop(0)
            from_elem = [rule_str[0],rule_str[1]]
            oppo_rule.append( from_elem )

        invk_num = int( inarg.pop(0) )
        invk_elems = list(inarg.pop(0)[:invk_num])

        result = do_calc(comb_rule, oppo_rule, invk_elems)

        print 'Case #%d: [%s]' % ( c+1, ', '.join(result) )

if __name__ == '__main__':
    main()

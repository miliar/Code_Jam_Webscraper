#! /usr/bin/env python
# -*- coding: utf8 -*-
# vim:ts=4:sw=4:expandtab:
# vi:ts=4:sw=4

def do_calc(seq, o_seq, b_seq):
    o_pos = 1
    b_pos = 1
    time = 0
    while len(seq) > 0:
        pushed = False
#     	print "-----"
#     	print time, seq
#     	print o_seq, b_seq
#     	print o_pos, b_pos
        if ( len(o_seq) > 0 ) and ( o_seq[0] != o_pos ):
            o_pos += (o_seq[0] - o_pos) / abs(o_seq[0] - o_pos)
        elif seq[0] == [ 'O', o_pos ]:
#     	    print "O Push"
            pushed = True
            o_seq.pop(0)

        if ( len(b_seq) > 0 ) and ( b_seq[0] != b_pos ):
            b_pos += (b_seq[0] - b_pos) / abs(b_seq[0] - b_pos)
        elif seq[0] == [ 'B', b_pos ]:
#     	    print "B Push"
            pushed = True
            b_seq.pop(0)

        if pushed == True:
            pushed = False
            seq.pop(0)

        time+=1

    return time


def main():
    for c in range(input()):
        seq = []
        o_seq = []
        b_seq = []
        input_seq = map( str, raw_input().split() )

        for i in range( int( input_seq.pop(0) ) ):
            elem = [input_seq[i*2], int(input_seq[i*2+1])]
            if elem[0] == 'O':
                o_seq.append( elem[1] )
            else:
                b_seq.append( elem[1] )
            seq.append(elem)
#        print len(seq), seq
#        print o_seq
#        print b_seq

        seq_time = do_calc(seq,o_seq,b_seq)

        print 'Case #%d: %d' % ( c+1, seq_time )

if __name__ == '__main__':
    main()

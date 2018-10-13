input_text = """
100
132
1000
7
122
246
408
80
591
291
1
807
378
153
984
8
506
595
117
726
212
961
730
677
249
216
177
654
463
929
367
384
659
471
37
995
963
238
157
955
871
297
293
379
82
646
611
565
704
414
854
178
588
841
473
311
829
853
402
563
198
281
294
368
445
734
972
692
114
796
908
925
300
124
656
155
949
63
87
622
173
577
526
193
865
539
722
544
304
500
329
790
946
607
735
686
942
999
879
525
255
""".strip()

# prepare data
input_array = input_text.split('\n')
cases = int(input_array[0])
input_array = [int(x) for x in input_array[1:]]

def checkn(n):
    ns = list(str(n))
    if(len(ns) == 1):
        return True
    else:
        tn = ns[0]
        for _n in ns[1:]:
            if _n >= tn:
                tn = _n
            else:
                return False
        return True

for i in range(0, cases):
    n = input_array[i]
    for j in reversed(range(n + 1)):
        if(checkn(j)):
            print "Case #%d: %d" % (i+1, j)
            break



#print input_array

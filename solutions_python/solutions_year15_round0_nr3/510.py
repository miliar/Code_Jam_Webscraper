import sys
sys.setrecursionlimit(100000)
import time

q = {

    ('1', '1'): ('1', 0),
    ('1', 'i'): ('i', 0),
    ('1', 'j'): ('j', 0),
    ('1', 'k'): ('k', 0),

    ('i', '1'): ('i', 0),
    ('i', 'i'): ('1', 1),
    ('i', 'j'): ('k', 0),
    ('i', 'k'): ('j', 1),

    ('j', '1'): ('j', 0),
    ('j', 'i'): ('k', 1),
    ('j', 'j'): ('1', 1),
    ('j', 'k'): ('i', 0),


    ('k', '1'): ('k', 0),
    ('k', 'i'): ('j', 0),
    ('k', 'j'): ('i', 1),
    ('k', 'k'): ('1', 1),

}


def quat_multiply(q1, q2):
    q1m, q1s = q1
    q2m, q2s = q2

    rm, rs = q[(q1m, q2m)]

    return rm, (q1s+q2s+rs) % 2

def apply_multiplication_2(t, start, end, memo):

    memo_key = (start, end)
    if memo_key in memo:
        return memo[memo_key]

    if (start, end-1) in memo or (start+1, end) in memo:
        if (start, end-1) in memo:
            r = memo[(start, end-1)]
            to_add = (t[end-1], 0)

            r = quat_multiply(r, to_add)
        else:
            r = memo[(start+1, end)]
            to_add = (t[start], 0)

            r = quat_multiply(to_add, r)

    else:
        if (start, '*') in memo:
            partial_end = memo[(start, '*')]

            if partial_end >= end:
                print 'bug'
            #else:
            #     print 'cache hit req (%d, %d), hit (%d, %d)' % (start, end, start, partial_end)

            partial_r = memo[(start, partial_end)]

            right_side = apply_multiplication_2(t, partial_end, end, memo)
            r = quat_multiply(partial_r, right_side)
        else:
            r = (t[start], 0)

            for i in xrange(start+1, end):
                r = quat_multiply(r, (t[i], 0))

        memo[(start, '*')] = end

    memo[memo_key] = r
    return r


def solve(s):
    memo = {}
    # find possibiities for i
    poss_i = []

    time_s = time.time()
    for i in xrange(1, len(s)):
        if apply_multiplication_2(s, 0, i, memo) == ('i', 0):
            poss_i.append(i)

    #print 'find i', time.time() - time_s

    time_s = time.time()

    poss_k = []
    for k in reversed(xrange(2, len(s))):
        if apply_multiplication_2(s, k, len(s), memo) == ('k', 0):
            poss_k.append(k)

    #print 'find k', time.time() - time_s
    time_s = time.time()

    for posi in poss_i:
        poss_k_r = list(reversed(poss_k))
        for posk in poss_k_r:
            if posk <= posi:
                continue

            if apply_multiplication_2(s, posi, posk, memo) == ('j', 0):
                #print 'check j', time.time() - time_s
                return True

    return False


# print solve('ik') == False
# print solve('ijk') == True
# print solve('kji') == False
# print solve('ji' * 6) == True
# print solve('i' * 10000) == False
# print solve('kjkkjiiijjj') == True
# print solve('kjkkjiiijjj'*20000) == True
# print solve('kikjkiijjjijkijjjjijikkjkikkjkjjkikikkjjikjiikjjjjikjikkikjjikikjijijijjijikjkjkjkjkikkjiijjijiiijjjjjikkjkjjjiikjjikjjijikijkikjjijjiiiiiikjikjkjkjijikjijijkjkkiikijjijjjjijjikkjjikjikjikiikkjkjjjikkkkkiikkjikijkjijjjjjjkjikiikjkkjikjikikkjiijiikkjiikijijkjikjijjiijijjijijijiikjkjkjkkkjjiijkjiikkjiiikjiiikjjjjjikijikkiikkjikiijjjjjiiikiiijjjkkiikjkjikkjikkjjikjikkjkjkkiikkkjjkkjijkjjjiikjiiikkkjkjiikkkkkjiijkjikjikjiijjjjiijjiikikikiikjjijikkikikijijikjkkikkjiikikkjkkjiijkiijikkjjiiikkkjkikjjjjjjjiijkikikijikijjjijikjkjkijkkijikjkjkjkijjiijjkkiikjijkkikjikkkjiiikjjjjjjkkkiikkjjikjjiikkkkijjkjikjkjjkjjjkkjijkjikiijjijiikjjijikjjikjijjkkkjjikkjjiikkjikkjijikijiikjijkjiikikkjjkkjkjkjikkkjjkkijijijikkjjjiiiijjiijiiijkkjiikjjkjjkkkikkkkkjikjiikikkijjkkjiikjikiijkjikkjkkkjjjjiikkjikikijikjjij')
# print solve('jiikikijkikjjkkkjjijkijiijjjjkjjjijiijjkiijjijjjijiiikkijkkkjiiiijkikkjijkjjkiiijjkjkikjijkikiikjikikkkjjiijkjjkkkkjjijkjijkkikkkkkikkijjjikjijjikikkkikkiiikjikjijiiikjkkkijijjijkikikkkjijkjkjjkiijikjikiijijijjkjkikkjijiiikjkkikiiijikikjkijikjijjkkkjjikkjikjjijikijijjikjikjiijkijkjjkkjiikkijjjijikkjikjjkkjkiijkikjjjikijkijkjjjkikkkjkiikkkkiikiiikjkijkkkjkkikkkiikjjjjikkkiikiijkjjijijkkjjkjjiiikjkijkijkjjijjjkjijkkkkkkjkijkkkjikikjkjikjkkijijikjkjiiiijjkkkjjijjkkjkkjkjijjjijjjjkjkjkjikiiiijikkjkiijjiijjkjjjjjkikkiikkjiikijjikkkjjijjjikkiijjikkkjkkiijkjikkiijjkjkkiijijjkkiikiikjijjiijkikkijjjikjjjiijijjjjiijjkjjijjkijjjjkkkjjjiiiijiiikikiijkikkijikjijiijjkjijkkkjjkiikijiiikijjiijikkjkiijjjjjiiijkiikjikkiikkjjijjkkkkijkijkkjjkkkjkkjijkjjijijkiiiiijkjiiikkkkikiiikiijkkkkkkjjijjjjjkkjikijiijikikjjiiiikkjkkjjkkjkjjijijikikjkiijijiijikkkiikkkijkikjjikkjjjjkjikkjijiikjkjkikkjkjkjkjkiiikjkkikkkjiiijkikkjikkjjjijiikjikkjkkiiikijikkjjijkjijkiijkkiiiiikjkjkkkiijkijijkiijkjikijiiijkjjikjjikkkkikikijkkkjkiikkjkikkijkkikjijjikiikiikjjkikjkkiiikjkkjjkjjjjkiikkiikjiikjkijkikkiikkkjkikkkkjjiikiijijkkikjjkikjiijjkjkjjjikijjjkiikiikjkjiiikjjijjkkijikiijijkiiijijjkjijjiijkkkjjijkiijkkijijjjjikjjjijjijkijjjkiikkijjjikjjikkjijjkjkikjjiijjjijjiiijiijkjkjjijkikkkijkikkijkkjkkkikiijkjkjijjjiikjjjkjjjkkjjkijkjkkkijiikijjkjikjkiijkjjiijkjjkjkijikjjijijjiikiiikijikkikkjkjijkkijjkkjkkiijkiijkkjkjiikijiijikkikjjijjijkiiikkjjiiijjkikijjikijijiikjkijkkiikkkikkjikkkkikjkiiiikkiikjijikjkiiikkkkjkkjjkjjijjjjjijkikikiiijiikijikkkijjjkkkjjikiikiikiikjijkiikjijjijkjikjkkkkkkkkkkijijikijikikjkjjiijijkjjijjkkijiijikikiijijkjjikkjjjikkkjkikjijkikjkiikiiijkkjkikjijijkkkikjkiijikkikiijjjjkkijkiijjjijjjkjjikkiiijiikkjikikijjikikkjkkijikjkkikjjjjkjiikjkkijjkkiikjjijijjkjjiijjkijjkkjkijkkjikiijikkkjikkjijjjiijjikijikkijkijkkjkjijjikkjkkjkjiiikjkjkkiijjkjjjjjjkjikkkikiijkjiijjkkjijiiiijkijiijiiikijijiikkjjjjiijjkkkkijkkiiikjkkikkkjiikkiiijkiikkjiikkijjiiikjkjkjjkjiiikikjkjijkkkikjkkkkiikiikjikkjikkkjikikjkiikikjijikjijiikjikkkiikjkkjjkikjikkikjkjikikjkkjkikiiiiiijkkjkkkkkjkkjkkjiijkjjjjiijjkkjkjijkkkjkjkikijiikijkkijiikiijiijjjjjjjjjjjiijjkkjkkkkkjjkkikikjjjkjiiiijjijiijjiiikjjjkkjiiikjkkkkiiijjjjijjikjikkikijjijjikjkijkjkjkkikkkijkjkkiiijkjikkkkkikjkkiikikkkijjikkjkkkjjkijjikkiijjjkjjkijiiikjjkikijkkijjkiiijkjkjijkkjjkkjkkjiikkjikijjjjikkiikkiikkikikjkjijjkiijikkkkkijiijkiijjkiiijkkjkiikkjjkkijkkjijijijjkjikjiiikjiijjijjikkiijjiiiijjkjjjijkiijjkiiiijjjijjijikkkiikijkkjkijiijkijikkiijijkkkkkjijijkkjkikkiiiikjikjkikijikijjkkkjkikkikjiiijikiijjiijikjkkkjjijjkjjkiikiiiikikkkjjkjkkkikkikkijiijjjkjjkijikkjjjkiijikiijjkiiikijkjkijiiikikjjjjkiikkkkkkikkikkiijkkikkjkikjijkkkikkjjikijijjijjikjikkiiiijijkkijikkkijjkkjjkkkiikkkjkkjkjjjiiijikkiikikkijjijijjkijkjijjkjjjjjjikjjiijiiiiiikiikkiikkikikijkikjkkkijikjijjkijkikkkjijkiijkjkkkkijjkijjkiiijijjikkikkiiijkiikiiiikkikjjkjijikjjkikjjikjjjiijjiiijikkjkkjikkiijkjkjiikkkkkkkkikkkijjjikjjjjijjjkikjijijjikkjkjkjkjjjikkkiikjkkjjiikjjkkjkiiijkiiijjikkkjkjjkijjijijikkjikijkiiiijikikiijjkkkkikkjkkiikikjijjijikkijijikijkiijkiiijjijikjjijkjkjijikjkjkkkijiiiiijijiijiikjijkjkijjiiijjkkjjjjkkjkkiikijkjjjkijkjijikjjikkkiikjijkjjkkiiikkijkjkjkkkjjikjjjkijkkkkkkijikkikiijjikkjkkijjjkijjjiiijkiijijiijjjjkjiikikkkjijjjikjjjiijkjikjkkjkjikjiikikkikjkjkikkiijiiijkkkikjiiikiiiiiikjkiijkikjkkjjikkjiikjjijkjjjjijkkjjkikjjjjiikiiijjikkkkkjjkjijjijijiikiikjjjjikjiikjjjikkikjikjkjiikikijkiikjjiijkjkjjjjkkikikiijjkkkjikkjjjkikiikkikjijkjjjikiikjjjjikiijikkjjiijikiiiikkijikiiijkkkijikkjjijjiijkkkjkjkiijjkiikikijkkjiikjikkjjkkikiijjijjjjjjkkjjiiiiikkijikkkkijkkikkiiijkikkikiikijkkijkjkijkkjjkjiijkjkkijkkkijikiijkjjikkkikikijiiiiijikkkjijjiijkjijkjjkiiikkkiijijkikiikijikkjjjjiiiiiiiiikkjjjikkiijijkkjikjjkjkiiijjjjkikkikjjjiiikjjjjjjjjkkjjkjjijjjiikijkjikkjjkkiijjjjikkkkiikijjkkikjkkjjjkjiiijkjjkjijjkkikkjjkkkkkjkkkjijkjikjiijijjikiiijkijkkkkjkiijjjkkkjkiikjikkjiiijkjjijjjkikjjjkjkkiikikiiikkikjkikjkkjjkijiikijikiijjiikjikjkkjjiiijkkjjjjikiiiikijkjkijjijijkjkikkkjjijkikikjjkkkjijjkiikjikkkiiijkiikiikjikjkiiiijjkkjjkkkjkjjiikjikiiiikkiiikkikjkkkkiiiiijjiijjjjkijikijjjiijjkjjiikiiikijikijiijiiikikkjkjiijkjiiikikiiijikijkikjjikjikjijkiiiiijiikkiikkkjjkjiikjjjiijkkjkkijiikkjkiiijikjkjjkjkikjkiikjkkkjkjjijkjikiiiijkkkiikjijikjjjikjkjjkijjikiijikkijkkikkkkjkkiijikkkkiijjjjijjiikijiiikjiijkjjijkjijjikiijjkkikikjjjkjijkkjkkikikjjkkjikiikkjjkkijiiiikkjjijkjkiikkjiikijikikjijiijjkjkkkkkijkjiikikiikijkikkkijkjjiikkkkjijkkijkjjiiiikijjjjkikjkjkkjiiijiikikkjijjkkjiijjjiikkkkijjjjjkjkjiiiiiijkkiikjkkkiiijkijkjkikijjjijjiiiikikjjjiiijjijiijkjkjkijjjjikjkjjiiijjjkjjjkjikkikikjkjjjiijjkjjjkijjkiijikkijjjjkikjjjjjkkjjkikjiikikkkkkiikjijiikjjkijkjijijkijjkikijjikiijkiiikikkjiijjiikikjkkikjjijikkkjijjjjkkjijjijkkkjjjiikkkjkkkjikkiiiiijiikkjkkkikjjiiiijikjiiiikkijijkjjkkkkjkkjijkjijkkjjkjkkiikikkkijjijkikijkijiijkkjikjikiijikijiijjjjijjjkikjijkkiijjiikkkkjjiijkiikikjkijjijkjjjikiiikkijkkkjkijjjiiikijkiikkjiiijiikijkkjjjiijkiikjjijijkijjkkiijijkjjjjiijjiiikkkjjijkjiijjkkkkiikiijjjjjkijkkiiijkjiikjjjjikjkiijkjkiiijiikjikikikjijkkikkiijjijkiijijjkjiiikikjjkijkkiikijkkjjjikjjjjkjkjjjkjkjjkijkjijjkijikkkjkkkjiijiikijiiikkiijkjjiikkiikjjkkkjiijijjkkkjikkijikkkijkkiijjiikkkijkkjkjkjikkiijkjijjkijkiikkkkkkkjkijjijjijjkijjkkiikjjkkkjikjjikjkkjjjjkiikjkjkjikikjkjjiijkkkijkkijkkjjkkijkjjjkkjkikiijjkkkijiijiijjjkikjjiikkkkikijkkiijjkjkkikjkkkiijkjkjjjiijikjiiiiikkjikjiikijkjjijijkiijijiiiikjijikjjikkijikijkiikjjiiijijjikkiijiiiikjiijjjjkiijijjkikkkkjkikjijijijkkkjiijjjiikkjjjjiikkjiijikijkkkjijkiijiijjkkjikjkiijkkjijkijjjkkikjjjjijikkikkjiijjjjkijikkikijiijiikkjikijkkjijijjkkkiijikkkkiijjjjijiikkkjjkkjkkiiiiijiijkijkikkiiikjkkiijjjkikkjikjkjjjjijijjijjjiijiijjkikkkjkjjjkjiikkiiiikjjijjjjkiikiiikkjkkkkkkkjiijjjkikjkkjijijjikiijkjikijjjikiikkijjjiikkkkikjjkiikjikkjkikkjjiiijkiijiiikkkijkkkkjjkikiikkjjikkikjijjijiikikkkkikjkjiikikkjjjjjjijjkkjjijikijjjkikkkjkkikjkkijikijjikkkiijiikkijikikkjijkkjikikkijjkikiiijkikjikjkjjjjjikikjiikikjkkiiikkikjikjkkijjkiikjjkijiijikiiiijijkkkkikikjiiikjjjjijiikjjiikjkkikjiijjkikikkkkkjjkikjjijjkkjjikkkjijjikjjkkjijjjiiiiiikjjkjijikjjkijikiiijkikjjjikkkiijijjkijjijikiijjjikikikjikiiiikjiijjiiikkkikjkkkiijkjjkijjkjjikkijiiikjkikikiikiijikiiiikjkkjkkjjjiikjkjijijjjijkkkiijkikkjjijikkkijkjjkjjiikjjkijjkjkkkkiiijijkkkkijjiijjijjikijkjkjjkijiiijkikikiiijjjikkiiiiijjkkkkjjkjiiikikjjjkkijikkkijikiikkkkijkjiijkkiikjjjjkjiiijijkijjjkikikijijkjijkjkkijjikikikijkjijikkjikijkijkjiijkkkjkkjkkjijijkkkiijijiijjjjkjikkkijijiijkkjkjjiikjjkiiijkkijkiikijikkkkjijikjjiiijijkiiijkikijkkkijiiikjkikkkkkkikjjjikiiikkjkjjijikjjjjiikjkkjijiiijijijjijjijjkikikjkjkjikjjkjikkkkkkkjijjjjkjjijiiikjkkkkkkijiijikkjjkijkkkkkjikiikkiikikikjikjkiikijjjikkikikkkkijikijjkijjjjijkkkj')

def read_list_of(numtype):
    return map(numtype, raw_input().split())

def main():
    for case_number in xrange(int(raw_input())):
        num_chars, repeat = read_list_of(int)
        s = raw_input() * repeat

        result = solve(s)

        print 'Case #%d: %s' % (case_number+1, {False: 'NO', True: 'YES'}[result])


main()

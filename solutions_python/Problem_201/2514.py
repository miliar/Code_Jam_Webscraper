if __name__ == "__main__":

    T = int(raw_input())
    for count in range(1, T+1):
        N, K = map(int, raw_input().strip().split())
        
        t = [N]
        t1 = []
	i = 1
        while i < K:
            m_val = max(t)
            val = m_val / 2
            if m_val % 2:
                t2 = [val, val]
            else:
                t2 = [val-1, val]
            index = t.index(m_val)
            t1 = t[0:index] + t2 + t[index+1:]
            t = t1
            i += 1

	#print "N: {0}, K: {1}".format(N, K)
	#print i,
	#print t
	#print "m_val: {0}".format(max(t))
        m_val = max(t)
        val = m_val / 2
        if m_val % 2:
            m, n  = [val, val]
        else:
            m, n = [val, val-1]

        print "Case #{0}: {1} {2}".format(count, m, n)

for _ in range(int(raw_input())):
            s, k =  map(str,raw_input().split())
            n, k = len(s), int(k)
            s = list(s)
            ans = 0
            for i in range(n - k + 1):
                if s[i] == "-":
                    ans += 1
                    for j in range(k):
                        s[i + j] = "-" if s[i + j] == "+" else "+"
            if "-" in s:
            	print "Case #%d: IMPOSSIBLE" % (_ + 1)
            else:
            	print "Case #%d: %d" %((_+1),ans)
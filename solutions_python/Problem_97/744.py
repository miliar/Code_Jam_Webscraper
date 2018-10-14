#
# Alec Grieser
# 13 April 2012
#
# For Google Code Jam qualifying round, "Recycled Numbers" problem.
#

data = open("C-large.in", "r").read().split('\n')
fout = open("recycle.out", "w")

count = int(data[0])

for i in range(count):
    bound_str = data[i + 1].split(' ')
    small = int(bound_str[0])
    big = int(bound_str[1])

    recycles = set()

    for m in range(small, big + 1):
        m_temp = m
        digits = len(str(m_temp))

        for k in range(digits):
            m_temp = m_temp//10 + (m_temp % 10)*(10**(digits - 1))

            #print(m_temp)

            if m_temp >= small and m_temp <= big and m_temp != m:
                recycles.add( (min(m, m_temp), max(m, m_temp)) )

    fout.write("Case #%d: %d\n" % (i + 1, len(recycles)))
    print("%d" % len(recycles))

fout.close()


    

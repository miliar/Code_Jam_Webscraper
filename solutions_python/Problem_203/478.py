"""
Bathroom stalls
"""
import heapq

OUTPUT = 'Case #%d:'

def main():
    """
    I/O
    """
    T = int(raw_input().strip())

    for t in xrange(1, T+1):
        R, C = raw_input().strip().split()

        R = int(R)
        C = int(C)
        cake = list() #append R rows

        for r in range(R):
            row = list(raw_input().strip())
            c = 0
            while c < C:
                if row[c] != '?':
                    left = c-1
                    while left >= 0 and row[left] == '?':
                        row[left] = row[c]
                        left -= 1
                    right = c+1
                    while right < C and row[right] == '?':
                        row[right] = row[c]
                        right += 1
                    c = right
                else:
                    c += 1
            cake.append("".join(row))
        
        #left over question marks
        r = 0
        while r < R:
            while cake[r][0] == '?':
                r += 1
            k = r - 1
            while k >= 0 and cake[k][0] == '?':
                cake[k] = cake[k+1]
                k -= 1
            k = r + 1
            while k < R and cake[k][0] == '?':
                cake[k] = cake[k-1]
                k += 1
            r = k

        print OUTPUT % t
        for r in range(R):
            print cake[r]


if __name__ == '__main__':
    main()

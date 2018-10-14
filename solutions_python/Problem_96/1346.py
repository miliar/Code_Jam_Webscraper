from sys import stdin


def main():
    n_cases = int(stdin.readline()) 

    for i_case in range(1, n_cases+1):
        line = stdin.readline().split(" ")

        n = int(line[0])
        s = int(line[1])
        p = int(line[2])

        result = 0

        for i in range(0, n):
        	punt = int(line[3+i])
        	
        	x = punt - p

        	if punt < p:
        		continue
			
        	if x >= 2*p-2:
        		result += 1
        	elif x>=2*p-3 and s != 0:
        		result += 1
        		s-=1
        	elif x>=2*p-4 and s != 0:
        		result += 1
        		s-=1

        print "Case #" + str(i_case) + ": " + str(result)



if __name__ == '__main__':
    main()

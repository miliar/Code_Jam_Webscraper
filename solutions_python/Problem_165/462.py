
def solve(R, C, W):
    if W == 1:
        hits = R*C
    else:
        hits = max(1, (C-W)/W) if C>W else 0
        hit = 0
        if C > W:
            hits = 1
            rem = C-(W+1)
            if rem > 0:
                hits += rem/W
        hits += W + C*(R-1)/W
    return str(hits)

def main(source, dest):
    fd = open(source, 'r')
    fo = open(dest, 'w')
    T = int(fd.readline())
    for i in range(1,T+1):
        R, C, W = fd.readline().rstrip().split(' ')
        result = solve(int(R), int(C), int(W))
	
        print 'Case #' + str(i) + ': ' + result + '\n',
        fo.write('Case #' + str(i) + ': ' + result + '\n')
	
    fd.close()
    fo.close()


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)
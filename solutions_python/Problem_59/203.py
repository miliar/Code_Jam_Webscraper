import sys, itertools
from pprint import pprint

output_line = "Case #{X:d}: {num_mkdir:d}"

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            N, M = map(int, inhandle.readline().split())

            total_mkdir = 0
            filesystem = {"/":{}}
            def add_dir(path, total_mkdir, count=True):
                #print(total_mkdir)
                dirs = path.strip()[1:].split("/")
                #pprint(dirs)
                curdir = filesystem["/"]
                for dir in dirs:
                    if not dir in curdir.keys(): #mkdir
                        if count:
                            #print("mkdir", dir)
                            total_mkdir += 1
                        curdir[dir] = {}
                    curdir = curdir[dir]
                return total_mkdir

            for n in range(N):
                total_mkdir = add_dir(inhandle.readline(), total_mkdir, count=False)

            for m in range(M):
                total_mkdir = add_dir(inhandle.readline(), total_mkdir, count=True)



            print(output_line.format(X=t + 1, num_mkdir=total_mkdir), file=outhandle)

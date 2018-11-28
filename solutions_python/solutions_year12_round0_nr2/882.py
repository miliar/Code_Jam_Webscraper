import sys
import math

def Dancing(inFile="B.in", outFile="B.out"):
    """GCJ 2012 Qualify Round Problem B"""
    fileIn = open(inFile, "r")
    fileOut = open(outFile, "w")
                    
    T = int(fileIn.readline())
    for ca in range(1, T+1):
        nums = fileIn.readline().split(" ")

        N = int(nums[0])
        S = int(nums[1])
        p = int(nums[2])

        normal = 0
        suprise = 0
        for i in range(1, N+1):
            ti = int(nums[2+i])
            low = ti // 3
            up = ti - low*2
            twoUp = False
            if up-low > 1:
                up -= 1
                twoUp = True
            elif up == low and low > 0:
                twoUp = True
            #print(repr(ti) + " " + repr(low) + " " + repr(up) + " " + repr(twoUp))

            if up >= p:
                normal += 1
            elif up+1 == p and twoUp:
                suprise += 1

        result = normal + min(S, suprise)
        fileOut.write("Case #" + repr(ca) + ": " + repr(result) + "\n")

    fileIn.close()
    fileOut.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python Dancing.py <inFIleName> <outFileName>")
        exit(1)
    Dancing(sys.argv[1], sys.argv[2])

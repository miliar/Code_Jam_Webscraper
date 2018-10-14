from sys import stdin

def main():
    inp = stdin
    cases = int(inp.readline())
    for s in range(cases):
        resp1 = int(inp.readline())
        mat = [[x for x in inp.readline().split()] for y in range(4)]
        resp2 = int(inp.readline())
        resp_mat1 = set(mat[resp1-1])
        mat2 = [[x for x in inp.readline().split()] for y in range(4)]
        resp_mat2 = set(mat2[resp2-1])
        resp_mat2 = set(resp_mat2)
        res = list((resp_mat1 & resp_mat2))
        if len(res) > 1:
            res = "Bad magician!"
        elif len(res) == 0:
            res = "Volunteer cheated!"
        else:
            res = res[0]
        print("Case #"+str(s+1)+":",res)        
main()
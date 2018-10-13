def solve():
    a = int(input())
    for x in range(1,a+1):
        row_g = int(input())
        matrix = []
        for i in range(4):
            matrix.append(input().split())
        ans_in = matrix[row_g-1]
        row_ng = int(input())
        new_mat = []
        for j in range(4):
            new_mat.append(input().split())
        count = 0
        ans = ''
        for char in ans_in:
            if char in new_mat[row_ng-1]:
                count += 1
                ans = char
        if count == 1:
            print("Case #{}: {}".format(x,ans))
        elif count > 1:
            print("Case #{}: Bad magician!".format(x))
        elif count < 1:
            print ("Case #{}: Volunteer cheated!".format(x))

if __name__ == '__main__':
    solve()


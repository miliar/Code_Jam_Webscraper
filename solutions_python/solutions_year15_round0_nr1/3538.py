__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''


def test(s):
    arr = []
    for c in s:
        arr.append(int(c))
    #print(arr)

    total = 0
    need = 0
    for i in range(len(arr)):
        if i == 0:
            total += arr[i]
        else:
            if arr[i] != 0:
                if total >= i: #enough
                    total += arr[i]
                else:
                    need += i - total
                    total += need
                    total += arr[i]
    return str(need)

file = open("sample.txt")

for i in range(int(file.readline())):
    print("Case #"+str(i+1)+": "+test(file.readline().strip().split(" ")[1]))
'''
print(test("7000000001"))
print("Expect: 3")
test("11111")
print("Expect: 0")
test("09")
print("Expect: 1")
test("110011")
print("Expect: 2")
test("1")
print("Expect: 0")
'''
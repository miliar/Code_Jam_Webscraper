def is_tidy(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True

def answer(n):
    for i in range(n, -1, -1):
        if is_tidy(i):
            return i

if __name__ == "__main__":
    for i in range(int(input())):
        print("Case #" + str(i + 1) + ":", answer(int(input())))

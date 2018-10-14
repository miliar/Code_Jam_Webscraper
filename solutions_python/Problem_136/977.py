import fileinput

__author__ = 'psmit'


def collecting_time(num_farms, F, X):
    return X / (2.0 + (F*num_farms))


def gain_farms_time(num_farms, F, C, memo={}):
    if((num_farms,F,C) in memo):
        return memo[(num_farms,F,C)]

    if num_farms == 0: return 0

    memo[(num_farms,F,C)] = gain_farms_time(num_farms - 1, F, C) + C / (2.0 + (F*(num_farms-1)))
    return memo[(num_farms,F,C)]


def main():
    inp = fileinput.input()

    T = int(inp.readline())

    for t in range(1,T+1):
        C,F,X = (float(x) for x in inp.readline().split())

        num_farms = 0
        min_time = collecting_time(num_farms, F, X)

        while True:
            num_farms += 1
            ti = collecting_time(num_farms, F, X) + gain_farms_time(num_farms, F, C)
            if ti < min_time:
                min_time = ti
            else:
                break

        print("Case #{}: {:.7f}".format(t, min_time))



main()
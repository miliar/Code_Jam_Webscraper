import fileinput

I, J, K = 2, 4, 8
translate = {"1": 1, "i" : I, "j" : J, "k" : K}
translate_result = {I: "i", J: "j", K: "k", 1: "1"}
op = {1 : {
          1 : 1,
          I : I,
          J : J,
          K : K},
      I : {
          1 : I,
          I : -1,
          J : K,
          K : -J},
      J : {
          1 : J,
          I : -K,
          J : -1,
          K : I},
      K : {
          1 : K,
          I : J,
          J : -I,
          K : -1}}


def val(qstring):
    result = 1
    for elem in qstring:
        sign = 1 if result > 0 else -1
        result = sign * op[abs(result)][translate[elem]]
    return result


def search_for_i(qstring):
    result = 1
    for idx, elem in enumerate(qstring):
        sign = 1 if result > 0 else -1
        result = sign * op[abs(result)][translate[elem]]
        if(abs(result) == I):
            return idx + 1, (1 if result > 0 else -1)
    return None, None


def search_for_k_backwards(qstring):
    result = 1
    for idx, elem in enumerate(reversed(qstring)):
        sign = 1 if result > 0 else -1
        result = sign * op[translate[elem]][abs(result)]
        if(abs(result) == K):
            return -(idx + 1), (1 if result > 0 else -1)
    return None, None


def tostr(val):
    return ("-{}" if val < 0 else "{}").format(translate_result[abs(val)])

def solve(num_and_mul, possible_ijk):
    num, fullmul = map(int, num_and_mul.split())
    #print("fullmul:", fullmul)
    if fullmul > 4:
        mul = 4 + (fullmul % 4)
    else:
        mul = fullmul
    #print(mul)

    possible_ijk = possible_ijk[:-1]
    # if(mul < 10):
    fullstring = possible_ijk * mul
    i_fin, sign1 = search_for_i(fullstring)
    if i_fin is None:
        #print("i_fin is none")
        return False
    k_start, sign2 = search_for_k_backwards(fullstring)
    if k_start is None:
        #print("k_start is none")
        return False
    if val(fullstring[i_fin:k_start]) * sign1 * sign2 == J:
        return True
    return False


def main():
    fin = list(fileinput.input())[1:]
    for i in range(len(fin) / 2):
        result = solve(fin[2 * i], fin[2 * i + 1])
        print("Case #{}: {}".format(i + 1, "YES" if result else "NO"))

if __name__ == '__main__':
    main()
    # print(tostr(val("ijk")))
    # print(search_for_i("ijk"))
    # print(search_for_k_backwards("ijk"))
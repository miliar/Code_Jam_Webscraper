def number_is_tidy(number: int) -> bool:
    if number < 10:
        return True
    number = str(number)
    for i in range(0, len(number) - 1):
        if number[i] > number[i + 1]:
            return False
    return True


def previous_tidy_number(number: int) -> int:
    if number_is_tidy(number):
        return number

    aux = str(number)
    for i in range(0, len(aux) - 1):
        if aux[i] > aux[i + 1]:
            if aux[i] != '1':

                result = aux[0:i] + str(int(aux[i]) - 1) + '9' * (len(aux) - i - 1)
                return previous_tidy_number(int(result))
            else:
                return previous_tidy_number(int('9' * (len(aux) - 1)))


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, previous_tidy_number(n)))

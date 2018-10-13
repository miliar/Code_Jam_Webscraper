#!/usr/bin/python3

def clean_up(number):
    text_rep = str(number)
    tidy = True

    # every 1-digit number is tidy
    if len(text_rep) == 1:
        return int(text_rep)

    # last control if number is tidy
    for i in range(len(text_rep)-1):
        if int(text_rep[i]) > int(text_rep[i+1]):
            tidy = False

    if tidy:
        return int(text_rep)

    # number was not tidy so clean up
    for i in range(len(text_rep)-1):
        if text_rep[i] > text_rep[i+1]:
            text_rep = str(int(text_rep[0:i+1])-1) + "9"*(len(text_rep)-(i+1))
            break

    text_rep = clean_up(int(text_rep))

    return int(text_rep)


T = int(input())

for i in range(T):
    last_number = int(input())

    tidy_number = clean_up(last_number)

    print("Case #" + str(i+1) + ": " + str(tidy_number))
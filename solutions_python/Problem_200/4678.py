def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

file = open("A.in", "r")
out = open("out.txt", "w")
p=0
for line in file:
    a_str=line.replace("\n", "")
    a_integer = int(a_str)
    p=p+1
    while is_sorted(list(a_str))==False and len(list(a_str))>1:
        a_integer = a_integer-1
        a_str=str(a_integer)
    out.write("Case #" + str(p) + ": " + str(a_str) + "\n")
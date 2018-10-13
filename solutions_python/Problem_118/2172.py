from math import sqrt

def isPalen(value):
    isPalendrome = False
    if len(str(value)) == 1:
        isPalendrome = True
    elif len(str(value)) == 2 or len(str(value)) == 3:
        if str(value)[0] == str(value)[-1]:
            isPalendrome = True
    else:
        isPalendrome = False

    return isPalendrome

def main(start, stop):
    found = 0

    for i in xrange(0,stop+1):
        if isPalen(i):
            if isPalen(i**2) and i**2 <= stop and i**2 >= start:
                found += 1

    return found


main(100,1000)

x = 0
in_file = open('C:\Users\Zane\SkyDrive\CodeJam\input.in', 'r')
data = in_file.readlines()
new_data = []
for item in data[1:-1]: #Note that we are indexing after the first item to avoid the first line. We also skip the last item due to losing the last digit because the new line character isn't there.
    new_data.append(item[:-1].split())
new_data.append(data[-1].split()) #This is to add the last item on the end
in_file.close()

output = open('C:\Users\Zane\SkyDrive\CodeJam\output.out', 'w')
event = 1
for item in new_data:
    x = main(int(item[0]),int(item[1]))
    output.write("Case #" + str(event) + ": " + str(x) + '\n')
    event += 1

output.close()
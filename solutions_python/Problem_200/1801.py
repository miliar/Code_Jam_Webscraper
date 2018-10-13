f = open ('B-large.in', 'r');

cases = int(f.readline());
case = 0;
output = "";
while case < cases:
    case += 1;
    data = list(f.readline())[:-1];
    data = list(map(int, data));
    counter = 0;
    prev = data[-1];

    for i in range(len(data)-2, -1, -1):
        if data[i] > prev:
            data[i] -= 1;
            data[i+1:] = [9]*(len(data)-i-1);
        prev = data[i]

    if data[0] == 0:
        data.pop(0);

    result = ''.join(map(str, data));
    
    output += "Case #" + str(case) + ": " + str(result) + "\n"

with open('B-large.out', 'w') as o:
    o.write(output)

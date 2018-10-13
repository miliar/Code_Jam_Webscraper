def googlers_dancers(s):
    numbers=[int(x) for x in s.split()];
    N=numbers[0];
    S=numbers[1];
    p=numbers[2];
    R=[numbers[n+3] for n in range(0,N)];
    R=sorted(R, reverse=True);

    winners=0;

    MAX=[];
    for x in R:
        if x==0:
            MAX.append(0);
        elif x==30:
            MAX.append(10);
        elif x==29:
            MAX.append(10);
        elif x%3==0:
            if S>0 and x/3 < p:
                MAX.append(x/3+1);
                S=S-1;
            else:
                MAX.append(x/3);
        elif x%3==1:
            MAX.append(x/3+1);
        elif x%3==2:
            if S>0 and x/3+1 < p:
                MAX.append(x/3+2);
                S=S-1;
            else:
                MAX.append(x/3+1);

    for n in MAX:
        if n >= p:
            winners = winners + 1;
    return str(winners)
    

input = open('B-large.in', 'r');
output = open('B-large.out', 'w');

n=int(input.readline());

for x in range(1,n+1):
    output.write("Case #" + str(x) + ": " + googlers_dancers(input.readline()) + "\n");

input.close();
output.close();

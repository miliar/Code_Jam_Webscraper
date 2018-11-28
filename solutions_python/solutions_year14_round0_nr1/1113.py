a=open('A-small-attempt0.in');
b=open('file.out','w');

cases=int(a.readline());

for case in range(cases):
    row1=int(a.readline());
    #go to the important row
    for i in range(row1-1):
	a.readline();
    
    posible_numbers=map(int, a.readline().split());
    #go to next
    for i in range(4-row1):
	a.readline();

    row2=int(a.readline());

    for i in range(row2-1):
	a.readline();

    other_numbers = map(int, a.readline().split());
    #obtain right numbers
    rnumbers=list()
    for n in other_numbers:
	if posible_numbers.count(n)>0:
	    rnumbers.append(n);
    #answer
    if len(rnumbers)==1:
	answer=str(rnumbers[0])
    elif len(rnumbers)>=2:
	answer='Bad magician!'
    else:
	answer='Volunteer cheated!'

    b.write("Case #"+str(case+1)+": "+answer+'\n');
    for i in range(4-row2):
	a.readline();
b.close()

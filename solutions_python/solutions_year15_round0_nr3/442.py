import csv


def findTarget(minus, remainder, inputString, x0, target):
    result = '1';
    for i, char in enumerate(remainder):
        (minus, result) = quaternionMultiply(minus, result, char);
        if result == target:
            #print('(result, x0, remainder) = (({},{}), {}, {})'.format(minus, result, x0, remainder))
            return(minus, True, remainder[i+1:], x0)
    for j in range(x0):
        for i, char in enumerate(inputString):
            (minus, result) = quaternionMultiply(minus, result, char);
            if result == target:
                #print('(result, x0, remainder) = (({},{}), {}, {})'.format(minus, result, x0-j-1, inputString[i+1:]))
                return(minus, True, inputString[i+1:], x0-j-1)
    #print('nothing found fail')
    return(0, False, '', 0)

def reduceRemainder(minus, inputString):
    result = '1';
    for char in inputString:
        (minus, result) = quaternionMultiply(minus, result, char);
    return (minus, result);

def quaternionMultiply(minus, l, r):
    result = {
       '11': '1',
       '1i': 'i',
       '1j': 'j',
       '1k': 'k',
       'i1': 'i',
       'ii': '-1',
       'ij': 'k',
       'ik': '-j',
       'j1': 'j',
       'ji': '-k',
       'jj': '-1',
       'jk': 'i',
       'k1': 'k',
       'ki': 'j',
       'kj': '-i',
       'kk': '-1',
    }[l+r];
    if result[0] == '-':
        return(minus*-1, result[1:]);
    else:
        return(minus, result); 



fin = open('input.in','r');
fout = open('output.out','w');

data = csv.reader(fin, delimiter=' ')
T = int(next(data)[0]);


for k in range(T):
    (L, X) = next(data);
    string=next(data)[0];
    #L = int(L);

    #print('(string, X) = ({}, {})'.format(string, X))
    #print('cut i')
    (minus, correct, remainder, x0) = findTarget(1, '', string, int(X), 'i');     
    if correct:
        #print('cut j')
        (minus, correct, remainder, x0) = findTarget(minus, remainder, string, x0, 'j');
        if correct:
            #print('cut k')
            (minus, correct, remainder, x0) = findTarget(minus, remainder, string, x0, 'k');
            if correct:
                #Reduce the multple repitions of strings here
                (Rminus, Rresult) = reduceRemainder(minus, remainder);
                (minus, result)  = (1, '1');
                x0 = x0%4;
                #print('(Rminus, Rremainder) = ({}, {})'.format(Rminus, Rresult));
                if x0 != 0:
                    (Bminus, Bresult) = reduceRemainder(1, string);
                    #print('x0, (Bminus, Bresult) = {}, ({}, {})'.format(x0, Bminus, Bresult));
                for i in range(x0):
                    (minus, result) = quaternionMultiply(minus*Bminus, Bresult, result);
                (minus, result) = quaternionMultiply(minus*Rminus, Rresult, result);
                #print('(minus, result) = ({}, {})'.format(minus, result));

    if correct and minus == 1 and result == '1':
        answer='YES';
    else:
        answer='NO';
    fout.write('Case #{}: {}'.format(k+1, answer))
    if k+1<T:
        fout.write('\n');

fin.close();
fout.close();


    

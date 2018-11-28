#include <iostream>
#include <cmath>

using namespace std;

void answer();
int main() {
    int numCases;
    cin >> numCases;
    for(int count = 1; count <= numCases; count++) {
        cout << "Case #" << count << ": ";
        answer();
    }
    return 0;
}

void answer() {
    long stalls, people, layer = 0, position;
    cin >> stalls >> people;

    while(people > pow(2, layer + 1) - 1) {
        ++layer;
    }
    cerr << '\n' << layer << endl;

    position = people - (pow(2, layer) - 1);

    long value1 = stalls, value2 = -1;
    long value1Amount = 1, value2Amount = 0;

    for(int count = 0; count < layer; count++) {
        if(value2 == -1) { // only one type of number
            // If value1 is odd
            if(value1 % 2 == 1) {
                value1Amount *= 2;
                value1 = (long)ceil((double)value1 / 2) - 1;
            }
            else { // If value1 is even.
                value1Amount = value1Amount;
                value2Amount = value1Amount;

                long tmp1, tmp2;
                tmp1 = ceil((double)(value1 - 1) / 2);
                tmp2 = floor((double)(value1 - 1) / 2);
                // cerr << value1 << endl;
                // cerr << tmp1 << '\n' << tmp2 << endl;
                if(tmp1 % 2 == 1) {
                    value1 = tmp1;
                    value2 = tmp2;
                }
                else {
                    value1 = tmp2;
                    value2 = tmp1;
                }
            }
        }
        else {
            // Consider value1 and value2, with value1 always odd coming in
            // and value2 always even coming in. 
            value1Amount *= 2;
            cerr << "PRE VALUES" << endl;
            cerr << value1 << endl;
            cerr << value2 << endl;
            value1 = (long)ceil((double)value1 / 2) - 1;


            long tmp1, tmp2;
            tmp1 = ceil(((double)value2 - 1) / 2);
            tmp2 = floor(((double)value2 - 1) / 2);

            if(tmp1 == value1) {
                value1Amount += value2Amount;
                value2 = tmp2;
                value2Amount = value2Amount;
            }
            else if(tmp2 == value1) {
                value1Amount += value2Amount;
                value2 = tmp1;
                value2Amount = value2Amount;
            }
            else {

                cerr << value1 << endl;
                cerr << tmp1 << '\n' << tmp2 << endl;
                cerr << "Can't reach here!" << endl;
                exit(1);
            }

            if(value1 % 2 == 0) {
                long hold;
                hold = value1;
                value1 = value2;
                value2 = hold;

                hold = value1Amount;
                value1Amount = value2Amount;
                value2Amount = hold;
            }
        }
    }

    long max, min, maxCount, minCount;
    if(value1 > value2) {
        max = value1;
        maxCount = value1Amount;
        min = value2;
        minCount = value2Amount;
    }
    else if(value2 > value1) {
        max = value2;
        maxCount = value2Amount;
        min = value1;
        minCount = value1Amount;
    }
    else {
        cerr << "Can't reach here! (2)" << endl;
        exit(1);
    }

    long spaces;
    if(position <= maxCount) {
        spaces = max;
    }
    else {
        spaces = min;
    }

    cout << ceil(((double)spaces - 1) / 2) << ' ' 
         << floor(((double)spaces - 1) / 2) << endl;

}
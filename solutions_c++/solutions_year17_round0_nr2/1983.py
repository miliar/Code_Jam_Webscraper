#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int tests;
    int it, jt;
    string number;

    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cin >> number;


        for (it = 0; it < number.size() - 1; ++it) {
            if (number[it] > number[it + 1]) {
                --number[it];
                for (jt = it + 1; jt < number.size(); ++jt) {
                    number[jt] = '9';
                }
                for (jt = it - 1; 0 <= jt; --jt) {
                    if (number[jt] > number[jt + 1]) {
                        --number[jt];
                        number[jt + 1] = '9';
                    }
                }
                break;
            }
        }


        cout << "Case #" << test << ": ";
        for (it = 0; it < number.size(); ++it) {
            if ('0' != number[it])
                cout << number[it];
        }
        cout << endl;
    }


    return 0;
}

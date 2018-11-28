#include <iostream>
#include <string>
using namespace std;
int main() {
    int t, k;
    string input;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> input >> k;
        // flip string
        int flipNum = 0;
        int stringLen = input.length();
        for (int j = 0; j < stringLen -k ; j++ ) {
            if(input[j]=='-') {
                for(int m = 0; m < k; m++) {
                    if(input[j+m]=='-') {
                        input[j+m]='+';
                    } else {
                        input[j+m]='-';
                    }
                }
                flipNum++;
            }
        }
        // detect the last answer
        int checkNum = 0;
        int checkPlus = 0;
        for(int j = stringLen-k; j < stringLen; j++) {
            // cout << input[j] << endl;
            if(input[j]=='-') {
                checkNum++;
            }
            if(input[j]=='+') {
                checkPlus++;
            }
        }

        // success
        if (checkNum == k) {
            cout << "Case #" << i << ": " << flipNum+1 << endl;
        } else if (checkPlus == k) {
            cout << "Case #" << i << ": " << flipNum << endl;
        } else {
            // impossible
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

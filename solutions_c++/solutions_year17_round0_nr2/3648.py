#include <iostream>
using namespace std;
int main() {
    int t, k;
    string input;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> input;
        int inputLen = input.length();
        if(inputLen==1) {
            cout << "Case #" << i << ": " << input << endl;
        } else {
            // search by last 2 number
            for(int j = inputLen - 1; j > 0; j--) {
                // _ _ input[j-1] input[j]
                if(input[j-1] > input[j]) {
                    // cout << "change" << endl;
                    input[j-1]--;
                    for(int k = j; k < inputLen; k++) {
                        input[k] = '9';
                    }
                }
            }
            if(input[0]=='0') {
                input = input.substr(1);
            }
            cout << "Case #" << i << ": " << input << endl;
        }
    }
    return 0;
}

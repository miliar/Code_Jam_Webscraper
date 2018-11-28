#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        string S;
        cin >> S;

        int K;
        cin >> K;

        int acc = 0;
        for(int j = 0; j <= S.length() - K; ++j) {
            if(S[j] == '-') {
                for (int k = 0; k < K; ++k) {
                    if (S[j + k] == '-')
                        S[j + k] = '+';
                    else
                        S[j + k] = '-';
                }
                ++acc;
            }
        }

        bool flag = true;
        for(int j = 0; j < S.length(); ++j) {
            if(S[j] == '-') {
                flag = false;
                break;
            }
        }

        cout << "Case #" << i << ": ";
        if(flag)
             cout << acc << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
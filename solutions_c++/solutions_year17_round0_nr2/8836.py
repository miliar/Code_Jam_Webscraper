#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
for(int kase = 1; kase <= T; ++kase) {
    long long int N;
    cin >> N;
    string S(to_string(N));
    if(S.size() == 1) {
        cout << "Case #" << kase << ": " << S << endl;
    } else {
        string SS;
        SS += S[0];
        for(int i = 1; i < (int)S.size(); ++i) {
            if((S[i] - '0') < (S[i-1] - '0')) {
                break;
            }
            SS += S[i];
        }
        if(SS.size() != S.size()) {
            char a = SS[SS.size() -1];
            int idx = 0;
            for(int i = 0; i < SS.size(); ++i, ++idx) {
                if(SS[i] == a) {
                    SS[i] = to_string((SS[i] - '0')-1)[0];
                    break;
                }
            }
            ++idx;
            while(idx < SS.size()) {
                SS[idx] = '9';
                ++idx;
            }
            while(SS.size() < S.size()) {
                SS += "9";
            }
        }
        cout << "Case #" << kase << ": " << stoll(SS) << endl;
    }
}
    return 0;
}

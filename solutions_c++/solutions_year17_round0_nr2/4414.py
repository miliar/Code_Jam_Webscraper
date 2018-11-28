#include <iostream>

using namespace std;

inline void dec(string& N, size_t i) {
    if (N[i] == '0') N[i] = '9';
    else N[i] = N[i] - 1;
}

int main(int argn, char* argv[]) {
    freopen("/Users/jorgemoag/Downloads/B-large.in.txt", "r", stdin);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        string N; cin >> N;
        bool carry = false;
        for (size_t i = N.length()-1; i > 0; i--) {
            if (carry) {
                dec(N, i);
            }
            carry = N[i] < N[i-1];
            if (carry) {
                N[i] = '9';
                for (size_t j = i; j < N.length(); ++j) {
                    N[j] = '9';
                }
            }
        }
        if (carry) {
            dec(N, 0);
        }
        while(N[0] == '0') N = N.substr(1);
        cout << "Case #" << t << ": " << N << endl;
    }
}

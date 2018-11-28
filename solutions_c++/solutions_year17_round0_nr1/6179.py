#include <bits/stdc++.h>

using namespace std;

bool same(string S) {
    for (int i = 0; i < S.length(); ++i) {
        if (S[i] == '-') return false;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string S;
        cin >> S;
        int K;
        cin >> K;
        int i = 0;
        while (S[i++] == '+');
        --i;
        int total = 0;
        for (; i + K - 1 < S.length(); ++i) {
            if (S[i] == '-') {
                S[i] = '+';
                for (int j = 1; j < K; ++j) {
                    S[i + j] = S[i + j] == '-' ? '+' : '-';
                }
                ++total;
            }
        }
        if (same(S)) {
            cout << "Case #" << t + 1 << ": " << total << endl;
        }
        else {
            cout << "Case #" << t + 1 << ": Impossible" << endl;
        }
    }
    return 0;
}
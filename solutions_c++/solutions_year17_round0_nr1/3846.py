#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        int K;
        cin >> S >> K;
        int len = S.size();
        bool a[len];
        for (int i = 0; i < len; i++) a[i] = S[i] != '+';
        int res = 0;
        bool possible = true;
        for (int i = 0; i < len && possible; i++) {
            if (a[i]) {
                if (i + K <= len) {
                    res++;
                    for (int j = i; j < i + K; j++) a[j] ^= 1;
                }
                else {
                    possible = false;
                }
            }
        }
        cout << "Case #" << t << ": ";
        if (possible) cout << res << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}

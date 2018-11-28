#include <bits/stdc++.h>

using namespace std;

string S;
int N, K, T;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> S;
        N = S.length();
        cin >> K;
        int cnt = 0;
        for (int i = 0; i < N - K + 1; i++) {
            if (S[i] == '-') {
                cnt++;
                for (int j = i; j < i + K; j++) {
                    S[j] = (S[j] == '+' ? '-' : '+');
                }
            }
        }
        bool isGood = true;
        for (int i = 0; i < N; i++) {
            if (S[i] == '-') {
                isGood = false;
                break;
            }
        }
        cout << "Case #" << t + 1 << ": ";
        if (isGood) {
            cout << cnt << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
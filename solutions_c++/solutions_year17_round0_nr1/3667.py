#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {
        string S;
        int K;
        int ans = 0;
        cin >> S >> K;
        for (int i = 0; i < S.size() + 1 - K; i++) {
            if (S[i] == '-') {
                for (int j = 0; j < K; j++) {
                    S[i + j] = (S[i + j] == '-') ? '+' : '-';
                }
                ans++;
            }
            //cout << S << endl;
        }
        for (int i = 0; i < S.size(); i++) {
            if (S[i] == '-') {
                ans = -1;
            }
        }
        printf("Case #%d: ", cas);
        if (ans == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }

    }



}

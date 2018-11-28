#include <bits/stdc++.h>
using namespace std;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {
        string S, ans;
        cin >> S;
        printf("Case #%d: ", cas);
        int pos = -1;
        for (int i = 1; i < S.size(); i++) {
            if (S[i] < S[i - 1]) {
                pos = i;
                break;
            }
        }
        if (pos == -1) {
            cout << S << endl;
            continue;
        }

        int p = -1;

        for (int i = pos - 1; i >= 0; i--) {
            if (i == 0 || S[i] > S[i - 1]) {
                S[i]--;
                p = i;
                break;
            }
        }
        if (S[0] > '0') cout << S[0];
        for (int i = 1; i <= p; i++) {
            cout << S[i];
        }
        for (int i = p + 1; i < S.size(); i++) {
            cout << '9';
        }
        cout << endl;
    }



}

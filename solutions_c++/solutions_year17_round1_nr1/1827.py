#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int k = t;
    while (t--) {
        cout << "Case #" << k - t << ":\n";
        int r, c;
        cin >> r >> c;
        string s, p = "";
        int flagt = 0;
        for (int i = 0; i < r; i++) {
            cin >> s;
            int flag = -1;
            for (int j = 0; j < c; j++) {
                if (s[j] == '?') {
                    if (flag != -1) s[j] = s[flag];
                } else {
                    if (flag == -1) {
                        for (int l = 0; l < j; l++) s[l] = s[j];
                    }
                    flag = j;
                }
            }
            if (flag != -1 && flagt == 0) {
                for (int j = 0; j < i; j++) cout << s << endl;
                flagt = 1;
                p = s;
            }
            if (flag == -1 && flagt) {
                flag = 1;
                s = p;
            }
            if (flag != -1) {
                cout << s << endl;
                p = s;
            }
        }
    }
}


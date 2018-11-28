#include <bits/stdc++.h>
#include <cstring>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int caseCnt;
    cin >> caseCnt;
    int caseNow = 0;
    while (caseNow < caseCnt) {
        ++caseNow;
        string str = "";
        int k;
        cin >> str >> k;
        int len = str.length();
        int ans = 0;
        for (int i = 0; i <= len - k; ++i) {
            if (str[i] == '-') {
                ans++;
                for (int j = 0; j < k; ++j) {
                    if (str[i + j] == '+') {
                        str[i + j] = '-';
                    } else {
                        str[i + j] = '+';
                    }
                }
            }
        }
        for (int i = len - k + 1; i < len; ++i) {
            if (str[i] == '-') {
                ans = -1;
            }
        }
        cout << "Case #" << caseNow <<": ";
        if (ans >= 0) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

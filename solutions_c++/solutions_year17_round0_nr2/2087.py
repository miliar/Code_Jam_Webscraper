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
        cin >> str;
        string ans = str;
        int len = str.length();
        char lastDigit = '0';
        int firstReversePos = -1;
        for (int i = 1; i < len; ++i) {
            if (str[i] < str[i - 1]) {
                firstReversePos = i;
                break;
            }
        }
        if (firstReversePos > 0) {
            int pos = firstReversePos - 1;
            while (pos > 0 && ans[pos] == ans[pos - 1]) {
                pos--;
            }
            for (int i = pos + 1; i < len; ++i) {
                ans[i] = '9';
            }
            ans[pos]--;
            while (ans.length() > 1 && ans[0] == '0') {
                ans = ans.erase(0, 1);
            }
        }
        cout << "Case #" << caseNow <<": " << ans << endl;
    }
    return 0;
}

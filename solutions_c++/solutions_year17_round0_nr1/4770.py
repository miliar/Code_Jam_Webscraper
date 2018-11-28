#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string str;
        int k;
        cin >> str >> k;
        int ans = 0;
        for (int i = 0; i <= str.length() - k; i++) {
            if (str[i] == '-') {
                for (int j = i; j < i+k; j++) {
                    str[j] = str[j] == '-' ? '+' : '-';
                }
                ans++;
            }
        }
        string res = to_string(ans);
        for (char ch : str) {
            if (ch == '-') {
                res = "IMPOSSIBLE";
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }
}

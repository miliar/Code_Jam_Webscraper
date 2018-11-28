#include <bits/stdc++.h>

using namespace std;


void solve(int x) {
    cout << "Case #" << x << ':' << ' ';
    string s;
    cin >> s;
    string ans = "";
    for (int i = 0; i < s.size(); i++) {
        ans += '0';
    }
    for (int i = 0; i < s.size(); i++) {
        for (int j = 9; j >= 0; j--) {
            for (int k = i; k < s.size(); k++) {
                ans[k] = '0' + j;
            }
            bool flag = true;
            for (int k = 0; k < s.size(); k++) {
                if (ans[k] != s[k]) {
                    flag = (ans[k] < s[k]);
                    break;
                }
            }
            if (flag) {
                if (i || j) cout << j;
                break;
            }
        }
    }
    cout << '\n';
}
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}

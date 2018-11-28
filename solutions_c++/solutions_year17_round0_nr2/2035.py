#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

string stretch(string s, int sz) {
    while(s.size() < sz)
        s += s.back();
    return s;
}

int solve() {
    string s;
    cin >> s;
    string ans;
    for (int i = 0; i < s.size(); i++) {
        for (char d = '0'; d <= '9'; d++) {
            string temp = ans + d;
            if (stretch(temp, s.size()) > s) {
                ans += char(d - 1);
                break;
            }
        }
        if (ans.size() < i + 1)
            ans += '9';
    }
    while (ans[0] == '0')
        ans = ans.substr(1);
    cout << ans << endl;
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}

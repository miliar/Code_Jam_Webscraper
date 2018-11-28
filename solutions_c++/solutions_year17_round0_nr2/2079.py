#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        string s;
        cin >> s;
        s = "0" + s;
        int last_inc = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i - 1] < s[i]) {
                last_inc = i;
            } else if (s[i - 1] > s[i]) {
                s[last_inc]--;
                for (int j = last_inc + 1; j < s.size(); j++) {
                    s[j] = '9';
                }
            }

        }
        stringstream buf;
        buf << s;
        long long ans;
        buf >> ans;
        cout << ans << endl;
    }
    return 0;
}
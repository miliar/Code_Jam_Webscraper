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
        int k;
        cin >> s >> k;
        vector<int> a(s.size());
        vector<int> pref_xor(a.size() + k);
        for (int i = 0; i < s.size(); i++) {
            a[i] = (s[i] == '-');
        }
        int sum = 0;
        int ans = 0;
        for (int i = 0; i < s.size(); i++) {
            sum ^= pref_xor[i];
            a[i] ^= sum;
            if (i <= (int)s.size() - k && a[i] == 1) {
                ans++;
                sum ^= 1;
                a[i] ^= 1;
                pref_xor[i + k] ^= 1;
            }
        }
        if (a == vector<int>(s.size())) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
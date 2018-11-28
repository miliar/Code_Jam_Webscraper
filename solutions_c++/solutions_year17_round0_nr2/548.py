#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct Solution {
    void run() {
        ll n;
        cin >> n;
        vector<ll> pw(19, 1);
        for (int i = 1; i < pw.size(); i++)
            pw[i] = pw[i - 1] * 10;
        vector<ll> s(19, 1);
        for (int i = 1; i < s.size(); i++)
            s[i] = s[i - 1] + pw[i];
        int pos = 0;
        while (pos < 19 && s[pos] <= n)
            pos++;
        pos--;
        ll res = s[pos];
        for (int j = pos; j >= 0; j--) {
            while (res + s[j] <= n && res / pw[j] % 10 < 9)
                res += s[j];
        }
        cout << res << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(10);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        cout << "Case #" << t << ": ";
        Solution sol;
        sol.run();
    }
}

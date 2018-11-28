#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, c = 0; cin >> t;
    while(t--) {
        string s; int k; cin >> s >> k;
        bool b[s.length()]; int p = 0, n = 0;
        for (int i = 0; i < s.length(); i++) {
            b[i] = s[i]=='+';
            if (b[i]) p++;
            else n++;
        }
        cout << "Case #" << ++c << ": ";
        if (n == 0) cout << 0 << endl;
        else if (p == 0 && s.length() == k) cout << 1 << endl;
        //else if (n < k) cout << "IMPOSSIBLE" << endl;
        // else if (p < k && n < k) cout << "IMPOSSIBLE" << endl;
        // else if ()
        else {
            int f = 0;
            for (int i = 0; i <= s.length()-k; i++) {
                if (!b[i]) {
                    f++;
                    for (int l = i; l < i+k; l++) b[l] = !b[l];
                }
            }
            bool chk = true;
            for (int i = 0; i < s.length(); i++) chk &= b[i];
            if (f == 0 || !chk) cout << "IMPOSSIBLE" << endl;
            else cout << f << endl;
        }
    }
}
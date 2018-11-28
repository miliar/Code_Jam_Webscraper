#include <bits/stdc++.h>

#define F first
#define S second
#define x1 privet1
#define x2 privet2
#define y1 privet3
#define y2 privet4
#define left privet6

using namespace std;
typedef long long ll;

const long long max_n = 100011, log_n = 32, max_m = 111, mod = 1000000007, inf = 1011111111111111111LL, p = 1009, p2 = 997;

int z, k, n;
string s;

char rev(char c) {
    if (c == '-') return '+';
    return '-';
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> z;
    int zz = z;
    while (z--) {
        cin >> s >> k;
        cout << "Case #" << zz - z << ": ";
        n = s.length();
        bool fl = false;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '-') {
                ans++;
                if (i + k > n) {
                    fl = 1;
                    break;
                }
                for (int q = 0; q < k; ++q) {
                    s[i + q] = rev(s[i + q]);
                }
            }
        }
        if (!fl) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}

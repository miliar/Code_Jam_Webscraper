#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

ll d;
int n;
ll k[10000];
ll s[10000];
ld m_tm;
ld c;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cout << "Case #" << T + 1 << ": ";
        cin >> d >> n;
        m_tm = -1;
        for (int i = 0; i < n; ++i) {
            cin >> k[i] >> s[i];
            c = static_cast<ld>(d - k[i]) / s[i];
            if (c > m_tm) {
                m_tm = c;
            }
        }
        cout << fixed << setprecision(10) << d / m_tm << "\n";
    }

    return 0;
}

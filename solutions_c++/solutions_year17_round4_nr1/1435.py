#include <bits/stdc++.h>

using namespace std;


void solve() {
    int n, p;
    cin >> n >> p;
    static int m[4];
    m[0] = 0;
    m[1] = 0;
    m[2] = 0;
    m[3] = 0;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        m[a%p]++;
    }
//    cout << m[0] << m[1] << m[2] << endl;
    if (p == 2) {
        cout << (m[0] + (m[1] + 1) / 2) << endl;
    } else if (p == 3) {
        int x = min(m[1], m[2]);
        m[1] -= x;
        m[2] -= x;
        cout << (m[0] + x + (m[1] + m[2] + 2) / 3) << endl;    
    } else if (p == 4) {
        int ans = m[0];
        ans += m[2] / 2;
        int x = min(m[1], m[3]);
        ans += x;
        m[1] -= x;
        m[3] -= x;
        int sm = m[1] + m[3];
        if (m[2] % 2 == 1) {
            ans += 1;
            m[2] = 0;
            sm = max(0, sm - 2);            
        }
        ans += (sm + 3) / 4;
        // 4x3, 4x1, 2x(1|3)+2, 2x2, 1+3
        cout << ans << endl;
    } else {
        assert(false);        
    }
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
}
#include<bits/stdc++.h>
using namespace std;

int a[5];

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int n, p;
        int s = 0;
        cin >> n >> p;
        memset(a, 0, sizeof(a));
        int ans = 0;
        for (int j = 0; j < n; j++) {
            int t;
            cin >> t;
            s += t%p;
            a[t%p] += 1;
        }
        if (s % p != 0) a[(p-s%p) % p]++;
        ans = a[0];
        if (p == 2) {
            ans += a[1] / 2;
        } else if (p == 3) {
            int t, v;
            t = min(a[1], a[2]);
            ans += t;
            v = max(a[1], a[2]) - t;
            ans += v / 3;
        } else {
            int t, v;
            t = min(a[1], a[3]);
            ans += t;
            v = max(a[1], a[3]) - t;
            ans += v / 4;
            ans += a[2] / 2 + a[2] % 2;
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}

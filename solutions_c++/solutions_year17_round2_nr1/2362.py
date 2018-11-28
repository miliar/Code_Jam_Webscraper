#ifdef _CONSOLE
#include "bits/stdc++.h"
#else
#include <bits/stdc++.h>
#endif
using namespace std;

typedef long long ll;
typedef long double ld;

#define rep(i,a,b) for(int i = (a); i < (b); i++)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define inf 1000000007

int t, n;
ld d, k[1001], s[1001];
ld ans;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _CONSOLE
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#endif
    // your code goes here
    cin >> t;
    rep(ti, 1, t + 1) {
        ans = 0;
        cin >> d >> n;
        rep(i, 1, n + 1) {
            cin >> k[i] >> s[i];
            if (ans < (d - k[i]) / s[i])
                ans = (d - k[i]) / s[i];
        }
        printf("Case #%d: %Lf\n", ti, d/ans);
    }
    return 0;
}
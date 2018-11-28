#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

const int MAXN = 1000;
int k[MAXN + 1], s[MAXN + 1];

int main() {
    //ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int n, d;
        scanf("%d%d", &d, &n);
        long double mx = 0;
        for(int i = 0; i < n; i++) {
            scanf("%d%d", &k[i], &s[i]);
            mx = max(mx, (d - k[i] + 0.0) / (long double)s[i]);
        }
        cout << "Case " << "#" << t << ": " << fixed << setprecision(15) << d / mx << "\n";
    }
    return 0;
}
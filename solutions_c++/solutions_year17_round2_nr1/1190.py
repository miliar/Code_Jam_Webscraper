#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1001, inf = 1000111222;

int n, d, k, s;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        ld maxfint = -1;
        cin >> d >> n;
        for(int i = 0; i < n; ++i) {
            cin >> k >> s;
            ld fint = 1.0 * (d - k) / s;
            maxfint = max(maxfint, fint);
        }
        ld ans = 1.0 * d / maxfint;
        cout << "Case #" << I << ": " << fixed << setprecision(9) << ans << endl;
    }
    return 0;
}



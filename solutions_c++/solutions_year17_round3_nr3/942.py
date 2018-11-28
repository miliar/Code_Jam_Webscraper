#include <bits/stdc++.h>
#include <math.h>
#define INF 100000000000005
#define MAXN 2005
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()
#define pi 3.14159265358979323846

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;


double a[100];

int main() {
    freopen("C-small-1-attempt0 (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, k;
    cin >> t;
    double u;
    for(int z = 0; z < t; ++z) {
        cin >> n >> k;

        cin >> u; for(int i = 0; i < n; ++i) cin >> a[i];

        sort(a, a + n);
        double xt = a[0]; int len = 1, index_last = -1, finish = 0;
        for(int i = 1; i < n; ++i) {
            if( a[i] == xt ) {
                len += 1;
                continue;
            }
            else {
                double st = a[i] - xt;
                double need = st * len;
                st = min(u, need);
                u -= st;
                st /= (double) len;
                xt += st;
                if(u == 0) {
                    finish = 1;
                    index_last = i;
                    break;
                }
                len += 1;
            }
        }
        if(finish == 1) {
            double ans = 1.;
            xt += u / (double) len;
            xt = min(1., xt);
            for(int i = 0; i < index_last; ++i) {
                ans *= xt;
            }
            for(int i = index_last; i < n; ++i) ans *= a[i];

            cout << "Case #" << z + 1 << ": " << fixed << setprecision(6) << ans << endl;
        }
        else {
            xt += u / (double) len;
            xt = min(1., xt);
            double ans = 1.;
            for(int i = 0; i < n; ++i) {
                ans *= xt;
            }
            cout << "Case #" << z + 1 << ": " << fixed << setprecision(6) << ans << endl;
        }

       // cout << "Case #" << z + 1 << ": " << fixed << setprecision(6) << ans << endl;


    }
}

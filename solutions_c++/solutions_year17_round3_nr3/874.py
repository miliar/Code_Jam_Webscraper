#include <bits/stdc++.h>
using namespace std;

double p[55];

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas=1; cas<=t; cas++) {
        int n,k; cin >> n >> k;

        double u; cin >> u;
        for (int i=0; i<n; i++) cin >> p[i];

        sort(p,p+n);

        double ans = 0.0;

        double s = 0.0, e = 1.0 , mid;
        double eps = 1e-9;
        while ( fabs(e-s) > eps ) {
            mid = (s+e)/2;

            double tot = 0.0;
            for (int i=0; i<n; i++) {
                if ( p[i] < mid ) tot += mid-p[i];
            }

            if ( tot > u ) {
                e = mid;
            } else {
                s = mid;
                double mp = 1.0;
                for (int i=0; i<n; i++) {
                    if ( p[i] < mid ) mp*=mid;
                    else mp*=p[i];
                }
                ans = max( ans , mp );
            }
        }

        printf("Case #%d: %.8f\n", cas, ans);
    }
}

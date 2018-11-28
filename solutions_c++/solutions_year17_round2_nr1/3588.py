#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back
#define oo INT_MAX
#define loo LLONG_MAX

using namespace std;

typedef pair<double, double> ii;

int main() {
    int t, cas = 0;
    cin >> t;
    while (t--) {
        int n;
        double a, b, d;
        cin >> d >> n;
        vector<ii> v;

        while (n--) {
            scanf("%lf %lf", &a, &b);
            v.pb(ii(a, b));
        }

        double aux = 0, ans = 0;
        fr(i, 0, v.size()) {
            aux = max(aux, (d - v[i].first) / v[i].second);
        }
        ans = d / aux;

        printf("Case #%d: %.6lf\n", ++cas, ans);
    }
    return 0;
}
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 100000

int main(void)
{
    freopen("A-large (1).in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    ll t, ti, d, n, i;
    cin >> t;
    for (ti = 1; ti <= t; ti++) {
        cin >> d >> n;
        vector< pair< int, int > > v(n);
        for (i = 0; i < n; i++) cin >> v[i].first >> v[i].second;
        sort(v.begin(), v.end());
        double smn, kmn , hr = 0, tm;
        hr = (double) (d-v[n-1].first)/v[n-1].second;
        //mn = v[n-1].second;
        //kmn = v[n-1].first;
        for (i = n-2; i >= 0; i--) {
            //kmn = v[i].first;
            //smn = v[i].second;
            hr = max(hr, (double) (d-v[i].first)/v[i].second);
        }
        printf("Case #%lld: %.8lf\n", ti, d/hr);
    }




    return 0;
}


#include <bits/stdc++.h>
using namespace std;

pair<long long,long long> x[1005];

double pi = 3.14159265359;

bool cmp (pair<long long,long long> a, pair<long long,long long> b) {
    if ( a.first != b.first ) return a.first > b.first;
    return a.second > b.second;
}

long long toparea (long long r) {
    return r*r;
}

long long sidesarea (long long r, long long h) {
    return h*r*2;
}

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas = 1; cas<=t; cas++) {

        int n,k; cin >> n >> k;

        for (int i=0; i<n; i++) {
            cin >> x[i].first >> x[i].second;
        }

        sort(x,x+n, cmp);

        //cout << endl; for (int i=0; i<n; i++) cout << x[i].first << " " << x[i].second << endl; cout << endl << endl;

        long long ma = 0;
        for (int i=0; i<n; i++) {
            long long ret = toparea(x[i].first) + sidesarea( x[i].first , x[i].second );
            vector< long long > y;
            for (int j=i+1; j<n; j++) y.push_back( sidesarea( x[j].first , x[j].second ) );
            if ( y.size() < k-1 ) continue;
            sort( y.begin() , y.end() );
            reverse( y.begin() , y.end() );
            for (int j=0; j<k-1; j++) ret += y[j];
            ma = max( ma, ret );
        }

        double ans = (double)(ma) * pi;
        printf("Case #%d: %.9f\n", cas , ans);
    }
}

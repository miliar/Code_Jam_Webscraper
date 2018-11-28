#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

ll n,d;

double ries(vector< pair<ll, ll> > &v) {
    double last_time = 0.0;
    for (int i = n-1; i>=0; --i) {
        double time = (d-v[i].first+0.0)/v[i].second;
        if (time > last_time) {
            last_time = time;
        }
    }
    return d/last_time;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t<=T; ++t) {
        printf("Case #%d: ", t);
        scanf("%lld %lld", &d, &n);
        vector< pair<ll, ll> > v;
        For(i,n) {
            ll k, s;
            scanf("%lld %lld", &k, &s);
            v.push_back({k, s});
        }
        sort(v.begin(), v.end());
        printf("%0.7f\n", ries(v));
    }
    return 0;
}

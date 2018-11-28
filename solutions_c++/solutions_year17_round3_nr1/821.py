#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define pb push_back
#define fst first
#define snd second
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t<=T; ++t) {
        int n, k;
        scanf("%d %d", &n, &k);
        vector< pll > v;
        For(i,n) {
            ll r,h;
            scanf("%lld %lld", &r, &h);
            v.pb({r*h,r});
        }
        sort(v.begin(), v.end(), greater<pll>());
        ll suc = 0;
        For(i,k-1) suc += 2*v[i].fst;
        ll best = 0;
        ll maxi = 0;
        For(i, k-1) {
            if (v[maxi].snd < v[i].snd) maxi = i;
        }
        best = 0;
        for(int i = k-1; i<n; ++i) {
            ll m = max(v[maxi].snd, v[i].snd);
            best = max(best, m*m + 2*v[i].fst);
        }
        best += suc;
        printf("Case #%d: %.9Lf\n", t, best*(long double)M_PI);
    }
    return 0;
}

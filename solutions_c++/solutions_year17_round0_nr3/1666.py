#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 20;


void solve() {
    ll n,k;
    cin >> n >> k;

    map<ll,ll> segs;
    segs[n] = 1;
    for(;;) {
        ll mx = segs.rbegin()->fi;
        if (segs[mx] < k) {
            k -= segs[mx];
            ll a = mx / 2;
            ll b = (mx-1) / 2;
            segs[a] += segs[mx];
            segs[b] += segs[mx];
            segs.erase(mx);
        }
        else {
            ll a = mx / 2;
            ll b = (mx-1) / 2;
            cout << a << " " << b;
            return;
        }
    }
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}
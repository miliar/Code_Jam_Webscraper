#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <sstream>

using namespace std;

#define ll long long
#define N (ll)(1<<21)
#define INF (ll)(1e18+1)
#define EPS (1e-8)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pdd pair<ld,ld>
#define fi first
#define se second
#define rep(i,a,n) for (ll i = a; i<n; i++)
#define per(i,a,n) for (ll i = n-1; i>=a; i--)
#define pb push_back

ll n, c, m;
ll p[1005],b[1005];
ll cnt[1005],cntp[1005];
ll v[1005];

bool mycomp(ll a, ll b) {
    return p[a] < p[b];
}

void solve() {
    cin >> n >> c >> m;
    memset(cnt,0,sizeof(cnt));
    memset(cntp,0,sizeof(cntp));
    rep(i,0,m) {
        cin >> p[i] >> b[i];
        b[i]--;
        v[i] = i;
        cnt[b[i]]++;
        cntp[p[i]]++;
    }

    sort(&v[0],&v[m],mycomp);

    ll cars = 0;
    rep(i,0,c)
        cars = max(cars, cnt[i]);

    rep(i,0,m) {
        ll need = ((i+1)+p[v[i]]-1)/p[v[i]];
        cars = max(need, cars);
    }

    ll mv = 0;
    rep(i,1,n+1) {
        mv += max(0LL,(cntp[i]-cars));
    }

    cout << cars << " " << mv << endl;

}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
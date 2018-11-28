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

ll g[105];
ll c[5];

void solve() {
    ll n, p;
    cin >> n >> p;

    memset(c,0,sizeof(c));

    rep(i,0,n) {
        cin >> g[i];
        g[i] %= p;
        c[g[i]]++;
    }

    ll ans = c[0];
    if (p == 2) {
        ans += (c[1]+1)/2;
    }
    else if (p == 3) {
        ll num = min(c[1],c[2]);
        ans += num;
        c[1] -= num, c[2] -= num;
        ans += (c[1]+2)/3;
        ans += (c[2]+2)/3;
    }
    else if (p == 4) {
        ll num = min(c[1],c[3]);
        ans += num;
        c[1] -= num, c[3] -= num;
        ans += c[2]/2;
        c[2] %= 2;

        if (c[1] == 0)
            swap(c[1],c[3]);
        ll cc = c[2];
        rep(i,0,cc) {
            if (c[1] >= 2) {
                ans++;
                c[1]-=2;
                c[2]--;
            }
        }

        ans += c[1]/4;
        c[1] %= 4;

        if (c[1] || c[2])
            ans++;
    }

    cout << ans << endl;
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
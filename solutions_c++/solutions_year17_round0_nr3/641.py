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

using namespace std;

#define ll long long
#define N (ll)(2e6+3)
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

map<ll, ll> mm, mm2;

void solve() {
    ll n, k;
    cin >> n >> k;
    k -= 1;
    mm.clear();
    mm[n] = 1;
    
    while (k > 0) {
        ll mx = mm.rbegin()->first;
        ll amt = mm.rbegin()->second;

        if (amt > k)
            mm[mx] = 1;
        else
            mm.erase(mm.find(mx));
        
        ll c1 = mx/2;
        ll c2 = (mx-1)/2;
        mm[c1] += amt;
        mm[c2] += amt;
        k -= amt;
    }
    
    ll res = mm.rbegin()->first;
    
    ll resmx = res/2;
    ll resmn = (res-1)/2;
    cout << resmx << " " << resmn << endl;
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
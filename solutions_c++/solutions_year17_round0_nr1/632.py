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

void solve() {
    string s;
    ll k;
    cin >> s >> k;
    
    ll cnt = 0;
    for (ll i = 0; i+k <= s.size(); i++) {
        if (s[i] == '-') {
            for(ll j = i; j < i+k; j++) {
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
            cnt++;
        }
    }
    bool imp = false;
    for (ll i = 0; i < s.size(); i++) {
        if (s[i] == '-')
            imp = true;
    }
    if (imp)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << cnt << endl;
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
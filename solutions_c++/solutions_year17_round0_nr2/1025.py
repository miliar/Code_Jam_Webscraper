#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


ll dp[25][10][2];
int a[25], tot;
ll n;

ll calc(int cur, int pre, bool limit) {
    if(cur == -1) return 1;
    ll &ret = dp[cur][pre][limit];
    if(~ret) return ret;
    ret = 0;
    int up = limit ? a[cur] : 9;
    for(int i = pre; i <= up; i++) {
        ret += calc(cur - 1, i, limit && i == up);
    }
    return ret;
}


ll solve(ll x) { 
    tot = 0;
    mst(dp, -1);
    do{
        a[tot++] = x % 10;
        x /= 10;
    }while(x);
    return calc(tot - 1, 0, 1);
}

ll check(ll l, ll r, ll val) {
    ll ret = 1;
    while(l <= r) {
        ll mid = (l + r) >> 1;
        if(solve(mid) >= val) {
            ret = mid;
            r = mid - 1;
        }
        else l = mid + 1;
    }
    return ret;
}
int main() {
    int T;

    freopen("out.txt", "w", stdout);
    cin >> T;
    For(cas, T) {
        cin >> n;
        cout << "Case #" << cas + 1 << ": " << check(1, n, solve(n)) << "\n";
        ll val = solve(n);
    }
	return 0;
}

// author: ash.code

#include <bits/stdc++.h>

#define ull unsigned long long
#define FOR(i, a, b) for(ll i = a; i <= b; i++)
#define ROF(i, a, b) for(ll i = a; i >= b; i--)
#define REP(i, n) for(ll i = 0; i < n; i++)
#define FILL(X, A) memset(X, A, sizeof(X))
#define fast ios_base::sync_with_stdio(false)
#define MOD 1000000007
typedef long long ll;

using namespace std;

int main() {
    // #ifndef ONLINE_JUDGE
    // 	freopen("ip.txt", "r", stdin);
    // 	freopen("op.txt", "w", stdout);
    // #endif
	
	fast;
    ll t, n, k;
    cin >> t;
    REP(tt, t) {
        cin >> n >> k;
        priority_queue<ll> pq;
        pq.push(n);
        REP(i, k-1) {
            ll k=pq.top();
            pq.pop();
            if(k&1) {
                pq.push(k/2);
                pq.push(k/2);
            }
            else {
                pq.push(k/2);
                pq.push(k/2-1);
            }
        }
        ll x=pq.top();
        // cout << x << endl;
        ll y=x/2, z=x-y-1;
        if(z<0) z=0;
    	cout << "Case #" << tt+1 << ": " << max(y,z) << " " << min(y,z) << endl;
    }
    
    return 0;
}


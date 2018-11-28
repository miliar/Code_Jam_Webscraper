#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

map <ll,ll> F;
ll n, k;

pair<ll,ll> get(ll n) {
    return pair<ll,ll>(n/2,(n-1)/2);
}

void solve(ll n, ll m, ll num1, ll num2) {
    if (n > m) {
        swap(n,m);
        swap(num1,num2);
    }
    //
    if (k <= num2) {
        pair<ll,ll> u = get(m);
        cout << u.first << " " << u.second << endl;
        return;
    }
    if (num1+num2 >= k) {
        pair<ll,ll> u = get(n);
        cout << u.first << " " << u.second << endl;
        return;
    }
    k -= num1 + num2;
    --n; --m;
    F[n/2] += num1;
    F[n-n/2] += num1;
    F[m/2] += num2;
    F[m-m/2] += num2;
    ll u = min(n/2,n-n/2);
    solve(u,u+1,F[u],F[u+1]);
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t; cin >> t; int te = t;
    while (t--) {
        F.clear();
        cin >> n >> k;
        cout << "Case #" << te-t << ": ";
        solve(n,n+1,1,0);
    }
	return 0;
}

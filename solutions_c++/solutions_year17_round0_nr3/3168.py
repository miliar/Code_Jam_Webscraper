#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair

pair <ll, ll> check(ll n, ll k);

pair <ll, ll> ee(ll n, ll k) {
    return check(n/2, k/2);
}

pair <ll, ll> eo(ll n, ll k) {
    if (k == 1) return mp(n/2 - 1, n/2);
    return check((n-1)/2, (k-1)/2);
}

pair <ll, ll> oe(ll n, ll k) {
    return check((n-1)/2, (k-1)/2 + 1);
}

pair <ll, ll> oo(ll n, ll k) {
    if (k == 1) return mp(n/2, n/2);
    return check((n-1)/2, (k-1)/2);
}

pair <ll, ll> check(ll n, ll k) {
    if (n%2 == 0 && k%2 == 0) return ee(n, k);
    if (n%2 == 0) return eo(n, k);
    if (k%2 == 0) return oe(n, k);
    return oo(n, k);
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        ll n,k;
        cin >> n >> k;
        pair <ll, ll> ans = check(n, k);
        cout << "Case #" << r+1 << ": " << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << '\n';
    }
    return 0;
}

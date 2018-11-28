#include<iostream>
#include<cstdio>

using namespace std;

typedef long long ll;

pair<ll, ll> breakn(ll n) {
	ll a = (n-1)/2;
	return pair<ll,ll>(a, n-1-a);
}

pair<ll, ll> ncr(ll n, ll r) {
	pair<ll, ll> t = breakn(n);
	if (r==1) return t;
	r--;

	if (r%2 == 1) return ncr(t.second, r/2 + 1);
	else return ncr(t.first, r/2);
}

void solve() {
	ll n,k;
	cin >> n >> k;
	pair<ll, ll> v = ncr(n,k);
	cout << v.second << " " << v.first;
}

int main() {
	//freopen("0Q/in.txt", "r", stdin);
	//freopen("0Q/C-small-1-attempt0.in", "r", stdin);
	//freopen("0Q/C-small-2-attempt0.in", "r", stdin);
	freopen("0Q/C-large.in", "r", stdin);
	freopen("0Q/out.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}

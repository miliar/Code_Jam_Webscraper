#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define mp make_pair
#define f first
#define s second
#define ld long double
#define pb push_back

inline ll sto(string s) {
	ll a = 0;
	for (char c: s) {
		a *= 10;
		a += c - '0';
	}
	return a;
}

inline int check(string s, int k) {
	ll r = sto(s);
	if (k != 0) {
		ll t = pow(10LL, k);
		r -= r % t + 1;
	}
	ll pr = r;
	int prev = 10;
	while (r != 0) {
		int v = r % 10;
		if (v > prev) return 0;
		prev = v;
		r /= 10;
	}
	cout << pr;
	return 1;
}

inline void solve() {
	string s;
	cin >> s;
	int n = s.size();
	for (int i = 0; i < n; ++i) {
		int v = check(s, i);
		if (v) {
			break;
		}
	}
}

int main(){
    freopen("gcj.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
}

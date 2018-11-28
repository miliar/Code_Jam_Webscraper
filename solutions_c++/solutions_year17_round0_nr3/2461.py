#include <bits/stdc++.h>
using namespace std;

using Int = long long;
#define rep(i, n) for (Int i = 0; i < Int(n); ++i)
#define rep1(i, n) for (Int i = 1; i <= Int(n); ++i)

void solve() {
	Int n, k; cin >> n >> k;
	Int lg = __lg(k), done = (1LL << lg) - 1;
	Int plus_one = (n - done) & done;
	n = (n - done) >> lg;
	k -= done;
	if (k > plus_one) --n;
	cout << (n+1)/2 << " " << n/2 << endl;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(nullptr);
	Int T; cin >> T;
	rep1(t, T) {
		cout << "Case #" << t << ": ";
		solve();
	}
}


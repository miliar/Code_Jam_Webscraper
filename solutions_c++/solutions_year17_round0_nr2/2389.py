#include <bits/stdc++.h>
using namespace std;

using Int = long long;
#define rep(i, n) for (Int i = 0; i < Int(n); ++i)
#define rep1(i, n) for (Int i = 1; i <= Int(n); ++i)

bool is_tidy(Int n) {
	Int prev = 9;
	while (n) {
		if (prev < (n % 10)) return false;
		prev = n % 10;
		n /= 10;
	}
	return true;
}

Int solve(Int n) {
	Int ans = 0, p = 0;
	while (!is_tidy(n)) {
		n -= (n % 10) + 1;
		n /= 10;
		ans = 10 * ans + 9;
		++p;
	}
	while (p--) n *= 10;
	ans += n;
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(nullptr);
	Int T; cin >> T;
	rep1(t, T) {
		Int n; cin >> n;
		cout << "Case #" << t << ": " << solve(n) << endl;
	}
}


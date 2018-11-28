#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

void solve() {
	int64_t n, k;
	cin >> n >> k;
	// rules are simpler in (n + 1) base: i breaks into i/2 and i-i/2
	++n;
	// sizeCount[i + 1] = count of empty intervals of length i
	map<int64_t, int64_t> sizeCount;
	sizeCount[n] = 1;
	int64_t y = 0, z = 0;
	while (k > 0) {
		assert(!sizeCount.empty());
		auto it = prev(sizeCount.end());
		int64_t d = min(k, it->second);
		k -= d;
		z = it->first / 2;
		y = it->first - z;
		it->second -= d;
		if (!it->second)
			sizeCount.erase(it);
		if (y != 1)
			sizeCount[y] += d;
		if (z != 1)
			sizeCount[z] += d;
	}
	cout << (y - 1) << ' ' << (z - 1) << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}

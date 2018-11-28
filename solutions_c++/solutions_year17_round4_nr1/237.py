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
	int n, p;
	cin >> n >> p;
	vector<int> cnt(p);
	for (int i = 0; i < n; ++i) {
		int q;
		cin >> q;
		++cnt[q % p];
	}
	int ans = cnt[0];
	if (p == 2) {
		ans += (cnt[1] + 1) / 2;
	} else if (p == 3) {
		int m = min(cnt[1], cnt[2]);
		int d = max(cnt[1], cnt[2]) - m;
		ans += m;
		ans += (d + 2) / 3;
	} else if (p == 4) {
		int m = min(cnt[1], cnt[3]);
		int d = max(cnt[1], cnt[3]) - m;
		ans += (cnt[2]) / 2;
		ans += m;
		ans += d / 4;
		if (cnt[2] % 2 == 0 && d % 4 == 0) {
		} else if (cnt[2] % 2 != 0 && d % 4 == 3) {
			ans += 2;
		} else {
			ans += 1;
		}
	}
	cout << ans << '\n';
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

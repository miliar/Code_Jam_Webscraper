#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K; cin >> N >> K;
		ld units; cin >> units;
		vector<ld> p(N);
		for (int i = 0; i < N; i++) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		while (units > 1e-9) {
//			cout << units << endl;
			int small = 0;
			ld cur = p[0];
			for (; small < p.size(); small++) {
				if (abs(cur - p[small]) > 1e-9) {
					break;
				}
			}
			if (small == p.size()) {
				ld add = units / small;
				for (int i = 0; i < p.size(); i++)
					p[i] += add;
				break;
			}
			ld next = p[small];
			if (units >= small * (next - cur)) {
				units -= small * (next - cur);
				for (int i = 0; i < small; i++)
					p[i] = next;
			} else {
				ld add = units / small;
				for (int i = 0; i < small; i++) {
					p[i] += add;
				}
				break;
			}
		}
		ld ans = 1;
		for (ld l : p)
			ans *= l;
		ans = min((ld) 1, ans);
		cout << fixed << setprecision(10) << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
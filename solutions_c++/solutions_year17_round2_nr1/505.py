// IOI 2018
#include <bits/stdc++.h>
using namespace std;
const int MAX = 1010;

int K[MAX], S[MAX], D, N;
int nc;

void solve() {
	cin >> D >> N;
	for (int i = 1; i <= N; ++i) cin >> K[i] >> S[i];

	double ans = 1e18;
	for (int i = 1; i <= N; ++i) {
		double x = (double)(D - K[i]) / S[i];
		ans = min(ans, (double)K[i] / x + S[i]);
	}

	cout << "Case #" << ++nc << ": " << setprecision(6) << fixed << ans << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--) solve();
}
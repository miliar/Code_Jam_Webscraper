#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double lf;

ll TC, N;
lf D;
pair<lf, lf> A[1005];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;

	for (ll tc = 1; tc <= TC; tc++) {
		cin >> D >> N;
		for (ll i = 0; i < N; i++) {
			cin >> A[i].first >> A[i].second;
		}
		lf lo = 0, hi = 1000000000000000LL, mid, c = 0;
		while (lo < hi && c < 100) {
			mid = (lo + hi) / 2;

			bool ok = true;
			for (ll i = 0; i < N; i++) {
				if (mid <= A[i].second) continue;
				lf mt = A[i].first / (mid - A[i].second);

				if (mt * mid < D) {
					ok = false;
					break;
				}
			}
			if (ok) {
				lo = mid;
			}
			else {
				hi = mid;
			}
			c++;
		}
	
		cout << "Case #" << tc << ": " << fixed << setprecision(9) << lo << "\n";
	}

	return 0;
}

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	freopen("out.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int d, k, a, b;
		double t = 0;
		cin >> d >> k;
		for (int i = 0; i < k; i++) {
			cin >> a >> b;
			t = max(t, 1.0 * (d - a) / b);
		}
		cout << fixed << setprecision(6) << "Case #" << tt << ": " << d / t
				<< "\n";
	}
	return 0;
}

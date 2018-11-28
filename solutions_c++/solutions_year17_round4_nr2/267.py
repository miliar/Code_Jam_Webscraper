#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <algorithm>
#include <map>
#include <iomanip>
#include <cstring>

using namespace std;

void Solve() {
	int n, m, c;
	cin >> n >> c >> m;

	vector<int> dega(n+1), degb(c+1);

	for (int i = 1; i <= m; ++i) {
		int a, b;
		cin >> a >> b;
		dega[a]++;
		degb[b]++;
	}

	int maxdega = 0;
	int sum = 0;
	for (int i = 1; i <= n; ++i) {
		sum += dega[i];
		maxdega = max(maxdega, sum / i + (sum % i ? 1 : 0));
	}

	int maxdegb = 0;
	for (int i = 1; i <= c; ++i) {
		maxdegb = max(maxdegb, degb[i]);
	}

	int ans1 = max(maxdega, maxdegb);

	int ans2 = 0;
	for (int i = 1; i <= n; ++i) {
		if (dega[i] > ans1) {
			ans2 += dega[i] - ans1;
		}
	}

	cout << ans1 << " " << ans2;
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		cout << "Case #" << k << ": ";
		Solve();
		cout << "\n";
	}
}
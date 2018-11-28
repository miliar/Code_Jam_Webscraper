#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <time.h>
#include <algorithm>
#include <list>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const int SZ = 1e3 + 10;
const int INF = 1e9;

ld p[SZ], u;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cout.precision(10);

	int t;
	cin >> t;
	for (int testno = 1; testno <= t; testno++) {
		int n, k;
		cin >> n >> k >> u;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		p[n++] = 1;

		sort(p, p + n);
		for (int i = 1; i < n; i++) {
			ld able = u / i, diff = p[i] - p[i - 1];
			u -= min(diff, able) * i;
			for (int j = 0; j < i; j++)
				p[j] += min(diff, able);
		}

		ld ans = 1;
		for (int i = 0; i < n; i++)
			ans *= p[i];

		cout << "Case #" << testno << ": ";
		cout << fixed << ans;
		cout << "\n";
	}

	return 0;
}
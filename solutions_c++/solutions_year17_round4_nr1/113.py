#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <algorithm>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const int SZ = 1e5 + 10;
const int INF = 1e9;

int g[SZ];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int testno = 1; testno <= t; testno++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> g[i];

		if (k == 2) {
			int x = 0;
			for (int i = 0; i < n; i++)
				if (g[i] % 2)
					x++;
			cout << "Case #" << testno << ": " << n - int(x / 2) << "\n";
			continue;
		}
		if (k == 3) {
			int d[3] = { 0, 0, 0 };
			for (int i = 0; i < n; i++)
				d[g[i] % 3]++;

			int mn = min(d[1], d[2]);
			d[1] -= mn;
			d[2] -= mn;
			mn += d[1] - ceil(double(d[1]) / double(3));
			mn += d[2] - ceil(double(d[2]) / double(3));
			cout << "Case #" << testno << ": " << n - mn << "\n";
		}
	}

	return 0;
}
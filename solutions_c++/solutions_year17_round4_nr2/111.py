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

int p[SZ], b[SZ], cl[SZ], rides[SZ];
int n, c, m, prom = 0;

bool succ(int r) {
	int lft = 0;
	prom = 0;
	for (int i = n - 1; i >= 0; i--)
		if (cl[i] < r)
			lft -= min(lft, r - cl[i]);
		else {
			lft += cl[i] - r;
			prom += cl[i] - r;
		}
	return bool(lft == 0);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	
	for (int testno = 1; testno <= t; testno++) {
		cin >> n >> c >> m;
		for (int i = 0; i < m; i++)
			cin >> p[i] >> b[i];

		for (int i = 0; i < c; i++)
			rides[i] = 0;
		for (int i = 0; i < m; i++)
			rides[b[i] - 1]++;
		int mx = 0;
		for (int i = 0; i < c; i++)
			mx = max(mx, rides[i]);

		for (int i = 0; i < n; i++)
			cl[i] = 0;
		for (int i = 0; i < m; i++) 
			cl[p[i] - 1]++;

		int l = mx, r = 2000, it = 2;
		while (it--) {
			int m = (l + r) / 2;
			if (succ(m))
				r = m;
			else
				l = m + 1;
		}
		l = max(mx, l - 2);
		while (!succ(l))
			l++;

		cout << "Case #" << testno << ": " << l << " " << prom << "\n";
	}

	return 0;
}

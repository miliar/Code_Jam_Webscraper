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

vector<pair<pair<int, int>, int> > x;
vector<int> bas, bbs;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int testno = 1; testno <= t; testno++) {
		int n, m;
		cin >> n >> m;
		x.clear();
		for (int i = 0; i < n; i++) {
			int a, b;
			cin >> a >> b;
			x.push_back(make_pair(make_pair(a, b), 0));
		}
		for (int i = 0; i < m; i++) {
			int a, b;
			cin >> a >> b;
			x.push_back(make_pair(make_pair(a, b), 1));
		}

		sort(x.begin(), x.end());
		bas.clear();
		bbs.clear();
		int atime = 0, btime = 0, ans = 0;
		for (int i = 0; i < x.size(); i++) {
			if (x[i].second == 0)
				atime += x[i].first.second - x[i].first.first;
			else if (x[i].second == 1)
				btime += x[i].first.second - x[i].first.first;

			if (x[(i + 1) % x.size()].second != x[i].second)
				ans++;
			else if (x[i].second == 0)
				bas.push_back(x[(i + 1) % x.size()].first.first - x[i].first.second);
			else
				bbs.push_back(x[(i + 1) % x.size()].first.first - x[i].first.second);
		}

		for (int &i : bas)
			if (i < 0)
				i += 1440;
		for (int &i : bbs)
			if (i < 0)
				i += 1440;

		sort(bas.begin(), bas.end());
		sort(bbs.begin(), bbs.end());
		for (int i : bas)
			atime += i;
		for (int i : bbs)
			btime += i;

		while (atime > 720) {
			atime -= bas.back();
			bas.pop_back();
			ans += 2;
		}
		while (btime > 720) {
			btime -= bbs.back();
			bbs.pop_back();
			ans += 2;
		}

		cout << "Case #" << testno << ": " << ans << "\n";
	}

	return 0;
}
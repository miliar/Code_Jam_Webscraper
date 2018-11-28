#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;
typedef unsigned long long ull;
typedef pair<int, int> pii;

void solve() {
	int n,k;
	cin >> n >> k;
	pii pans[1010];
	for (int i=0; i<n; ++i) {
		cin >> pans[i].first >> pans[i].second;
	}
	double best = 0;
	sort(pans, pans+n, greater<pii >());
	for (int i=0; i<=n-k; ++i) {
		long long rad = pans[i].first;
		double h = 2.0*pans[i].first*M_PI*pans[i].second;
		vector<double> heights;
		for (int j=i+1; j<n; ++j)
			heights.push_back(2.0*pans[j].second*M_PI*pans[j].first);
		sort(heights.begin(), heights.end(), greater<double>());
		for (int j=0; j<k-1; ++j) h += heights[j];
		double ans = rad*(rad*M_PI) + h;
		best = max(best, ans);
	}
	cout << setprecision(18) << best << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

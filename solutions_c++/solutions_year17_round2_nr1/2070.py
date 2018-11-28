#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

void solve()
{
	int n, d;
	cin >> d >> n;

	vector<pair<int, int> > v(n);
	for (int i = 0; i < n; i++) {
		int k, s;
		cin >> k >> s;
		v[i] = make_pair(k, s);
	}

	double t = 0;

	for (int i = 0; i < n; i++) {
		int need = d - v[i].first;
		double time = (double) need / v[i].second;
		t = max(t, time);
	}

	double ans = (double) d / t;
	printf("%.9f", ans);

}


int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}

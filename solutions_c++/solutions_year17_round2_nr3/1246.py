#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>

using namespace std;

void solve()
{
	int n,q;
	vector<vector<int> > d(n, vector<int>(n));
	cin >> n >> q;
	vector<int> e(n), s(n);
	for (int i = 0; i < n; i++) {
		cin >> e[i] >> s[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++){
			cin >> d[i][j];
		}
	}
	int u, v;
	cin >> u >> v;

	// just small data

	vector<double> ans(n, 1e30);
	ans[n-1] = 0;
	for (int i = n-2; i >= 0; i--) {
		double dis = 0;
		for (int j=i+1; j < n; j++) {
			dis += d[j-1][j];
			if (dis > e[i]) break;
			double t = dis / (double)s[i] + ans[j];
			ans[i] = min(ans[i], t);
		}
	}

	cout << setprecision(9) << fixed <<  ans[0];
}

int main()
{
	ios::sync_with_stdio(false);
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		cout <<"Case #" << i <<": ";
		solve();
		cout << endl;
	}
    return 0;
}

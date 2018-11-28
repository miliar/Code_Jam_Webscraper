#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>

using namespace std;


void solve()
{
	double d;
	int n;
	cin >> d >> n;
	double ans = 1e20;
	vector<int> k(n),s(n);
	for (int i = 0; i < n; i++) {
		cin >> k[i] >> s[i];
	}

	for (int i = 0; i < n; i++) {
		double t = double(d - k[i]) / s[i];
		double speed = (double)d / t;
		ans = min(ans, speed);
	}

	cout << setprecision(6) << fixed << ans;
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

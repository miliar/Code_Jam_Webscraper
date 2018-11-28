#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;

typedef long long ll;

struct horse
{
	long double d;
	long double s;
	long double t;
};

bool operator<(const horse& a, const horse& b)
{
	return a.d > b.d;
}

horse a[1005];

void solve()
{
	int  n;
	long double d;
	cin >> d >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i].d >> a[i].s;

	sort(a + 1, a + 1 + n);

	a[1].t = (d - a[1].d) / a[1].s;
	for (int i = 2; i <= n; i++)
	{
		a[i].t = max((d - a[i].d) / a[i].s, a[i - 1].t);
	}

	cout << fixed << setprecision(7) << d / a[n].t << endl;

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ll TC;
	cin >> TC;
	for (ll i = 1; i <= TC; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
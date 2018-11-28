#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <iomanip>
#include <string>

using namespace std;

typedef long long ll;

#define pi 3.14159265359

bool flag = 0;

struct layer
{
	double h;
	double r;
	double area;
	double areaH;
	bool used;
};

bool operator<(const layer& a, const layer& b)
{
	if (flag == 0)
	{
		if (a.used == 1) return false;
		return a.areaH > b.areaH;
	}

	if(flag == 1)
	return a.area > b.area;

	if (flag == 2)
		return a.r > b.r;
}

double a[1005];

void solve()
{
	ll n, m;
	cin >> n >> m;
	double u;
	cin >> u;
	double s = 0;
	for (ll i = 1; i <= n; i++) {
		cin >> a[i];
		s += a[i];
	}
	s += u;
	s /= n;

	double q = 0;
	int  k = 0;
	for (int i = 1; i <= n; i++) {
		if (a[i] < s) {
			q += a[i];
			k++;
		}
	}
	q += u;
	q /= k;

	double ans = 1;
	for (int i = 1; i <= n; i++)
	{
		if (a[i] < s)
			a[i] = q;
		ans *= a[i];
	}

	cout << fixed << setprecision(7) << ans << endl;
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
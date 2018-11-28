#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>
#include <iomanip>

using namespace std;

#define mp(a, b) make_pair(a,b)

long double EPS = 1e-9;
void f()
{
	long double d;
	int n;
	cin >> d >> n;
	vector<pair<long double, long double> > a;
	for (int i = 0;i < n;i++)
	{
		long double x,y;
		cin >> x >> y;
		a.push_back(mp(x, y));
	}
	long double l=0, r=2e15;
	for (int z = 0;z < 1000 ;z++)
	{
		double c = l + (r - l) / 2;

		long double min_t = 1e18;
		for (int i = 0;i < n;i++)
		{
			long double t = a[i].first/(c - a[i].second) ;
			if (t < 0)
				continue;
			min_t = min(min_t, t);
		}
		if (min_t*c - EPS >= d)
		{
			l = c;
		}
		else
			r = c;
	}
	cout << setprecision(7) << fixed << l;
}


int main() {
	int n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> n;
	for (int i = 0;i < n;i++)
	{
		if (i == 85)
			int z = 0;
		cout << "Case #" << i + 1 << ": ";
		f();
		cout << endl;
	}

	return 0;
}
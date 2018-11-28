#ifdef LOCAL
#include "locallibs.h"
#else
#include <bits/stdc++.h>
#endif

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
double solve(int n,double d, vector < pair < double, double> > &a)
{
	double l = 0;
	double r = 1e19;
	double eps = 1e-8;
	for(int i = 0; i<200;i++)
	{
		auto mid = (l + r) / 2;
		double dist, ans = 1e36;
		for (auto it:a)
		{
			dist = it.first + it.second * mid;
			ans = min(ans, dist);
		}
		if(ans > d)
		{
			r = mid;
		}else
		{
			l = mid;
		}
	}
	return l;
}

int main() {
#ifdef LOCAL
	// freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		double d;
		int n;
		cin >> d >> n;
		vector < pair < double, double> > a(n);
		for(int i =0; i<n;i++)
		{
			cin >> a[i].first >> a[i].second;
		}
		setprecision(20);
		cout << fixed << setprecision(8);
		auto ans = solve(n, d, a);
		cout << "Case #" << i << ": " << d/ans << endl;
	}
}
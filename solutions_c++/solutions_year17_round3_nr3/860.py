#define _USE_MATH_DEFINES
#ifdef LOCAL
#include "locallibs.h"
#else
#include <bits/stdc++.h>
#endif
using namespace std;
typedef long long ll;
const ll mod7 = 1e9 + 7;
struct Cake
{
	double r, h;
	double getScore()
	{
		return 2 * M_PI * r * h;
	}
};
bool cmpSide(Cake a, Cake b)
{
	return a.getScore() > b.getScore();
}
bool cmpSq(Cake a, Cake b)
{
	return a.r > b.r;
}
int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++)
	{
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> a(n);
		for(int i = 0; i<n;i++)
		{
			cin >> a[i];
		}
		int all = int(round(u * 10000) + 0.000001);
		double eps = 1e-4;
		int mni = 0;
		while(all --> 0)
		{
			double mn = 1e9;
			for(int i = 0; i<n;i++)
			{
				if(a[i] < mn)
				{
					mn = a[i];
					mni = i;
				}
			}
			a[mni] += eps;
		}
		double ans = 1;
		for(int i=0;i<n;i++)
		{
			ans *= a[i];
		}
		cout << setprecision(10) << fixed;
		cout << "Case #" << i << ": " << ans << endl;
	}
}
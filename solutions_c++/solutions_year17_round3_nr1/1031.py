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
		double ans = 0;
		int n, k;
		cin >> n >> k;
		vector<Cake> a(n);
		for (int i = 0; i < n; i++)
		{
			cin >> a[i].r >> a[i].h;
		}
		while(a.size() >= k)
		{
			sort(a.begin(), a.end(), cmpSq);
			double res = a[0].r * a[0].r * M_PI;
			res += a[0].getScore();
			a.erase(a.begin());
			sort(a.begin(), a.end(), cmpSide);
			for (int i = 0; i < k-1; i++)
			{
				res += a[i].getScore();
			}
			sort(a.begin(), a.end(), cmpSq);
			
			ans = max(ans, res);
		}
		cout << setprecision(10) << fixed;
		cout << "Case #" << i << ": " << ans << endl;
	}
}
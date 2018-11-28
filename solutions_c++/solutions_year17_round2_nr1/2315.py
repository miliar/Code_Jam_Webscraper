#include <bits/stdc++.h>
#define ll long long
#define rep(i,to) for(int i=0;i<(to);i++)
#define rep1(i,to) for(int i=1;i<=(to);i++)
#define ms(x, v) memset(x, v, sizeof(x))
using namespace std;
const int N = 1005;
int k[N], s[N], d, n;
bool check(double mid)
{
	double tm = d / mid;
	rep1(i, n)
	{
		if (tm * s[i] < d - k[i]) return 0;
	}
	return 1;
}
int main()
{
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int T;
	cin >> T;
	rep1(cas, T)
	{
		cin >> d >> n;
		rep1(i, n) cin >> k[i] >> s[i];
		double l = 0, r = 1e20, mid;
		int TM = 500;
		while (TM--)
		{
			mid = (l + r) / 2;
			if (check(mid)) l = mid;
			else r = mid;
		}
		printf("Case #%d: %.10f\n", cas, l);
	}
	return 0;
}
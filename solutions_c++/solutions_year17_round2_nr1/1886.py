#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long ll;
const int MAXN = 100500;
const double INF = 1e9;

double sol()
{
	double d;
	int n;
	cin >> d >> n;
	double ans = 1e18;


	for (int i = 0; i < n; i++)
	{
		double x, v;
		cin >> x >> v;
		ans = min(ans, d * v / (d - x));
	}

	return ans;
}

int main()
{                                                     
	
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: %.8lf\n", i, sol());
	}

	return 0;
}


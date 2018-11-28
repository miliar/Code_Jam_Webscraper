#include <bits/stdc++.h>

using namespace std;

#define INF 2000000000
#define MOD 1000000007
typedef long long ll;
typedef pair<int, int> P;


int main()
{
	int t;
	cin >> t;

	for (int ii = 1; ii <= t; ii++) {
		double d;
		ll n;
		cin >> d >> n;
		double t = 0;
		for (int i = 0; i < n; i++) {
			double dist;
			double v;
			cin >> dist >> v;
			double tmp = (d-dist)/v;
			t = max(tmp, t);
		}
		double ret = d/t;

		cout << "Case #" << ii << ": ";
		printf("%lf\n", ret);
	}
}

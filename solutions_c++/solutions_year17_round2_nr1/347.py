#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const int N = 1e3 + 7;

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	cout << setprecision(12) << fixed;
	for (int T = 0; T < t; T++)
	{
		int n, d;
		cin >> d >> n;
		ld ans = 0;
		for (int i=0; i<n; i++)
		{
			int x, s;
			cin >> x >> s;
			if (i == 0 || ans > d / ((ld)(d - x) / s))
				ans = d / ((ld)(d - x) / s);
		}
		cout << "Case #" << T+1 << ": " << ans << "\n";
	}
	

	return 0;
}

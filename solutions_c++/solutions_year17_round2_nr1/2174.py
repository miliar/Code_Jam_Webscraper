#include <bits/stdc++.h>
using namespace std;

void solve()
{
    long double d; int n; cin >> d >> n;
    long double smax = 10000000000000000;
    for(int i = 0; i < n; ++i)
    {
        long double k, s; cin >> k >> s;
        smax = min(smax, d*s / (d - k));
    }
    printf("%.7Lf", smax);
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
        solve();
		cout << endl;
	}
	return 0;
}

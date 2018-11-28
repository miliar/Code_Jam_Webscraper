#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t = 1; t <= tt; t++)
	{
        int n;
        double d;
        cin >> d >> n;
        double tmax = 0;
        while(n--)
		{
			double k, s;
			cin >> k >> s;
			tmax = max(tmax, (d-k)/s);
		}
		double ans = d/tmax;
		cout.setf(ios::floatfield, ios::fixed);
		cout.precision(8);
		cout << "Case #" << t << ": " << ans << "\n";
	}
	return 0;
}

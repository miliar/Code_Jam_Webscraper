#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, tst = 1;
	cin >> t;
	while(t--)
	{
		int d, n;
		cin >> d >> n;
		double mini = 0.0;
		for(int i = 0; i<n; i++)
		{
			int di, vi;
			cin >> di >> vi;
			double dist = (d - di);
			mini = max(mini, 1.0 * dist/(1.0*vi));
		}
		printf("Case #%d: ", tst++);
		cout << fixed << setprecision(10) << (1.0*d)/mini << endl;;
	}
	return 0;
}

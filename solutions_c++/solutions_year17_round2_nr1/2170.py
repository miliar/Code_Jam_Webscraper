#include <bits/stdc++.h>

using namespace std;

int main()
{
	long long t,tt;
	cin >> t;
	long double d,s,time;
	long long i,n;
	pair<long double, long double> k[1005];
	for(tt=1;tt<=t;tt++)
	{
		cin >> d >> n;
		for(i=0;i<n;i++)
		{
			cin >> k[i].first >> k[i].second;
		}
		//sort(k,k[n]);
		time = (d-k[n-1].first)/(k[n-1].second);
		for(i=n-2;i>=0;i--)
		{
			time = max(time, (d-k[i].first)/k[i].second);
		}
		cout << "Case #" << tt << ": ";
		//setprecision(10);
		//cout << std::setprecision(6) <<  d/time << endl;
		printf("%.6Lf\n",d/time);
	}
	return 0;
}
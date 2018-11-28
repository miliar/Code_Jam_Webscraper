#include <bits/stdc++.h>
using namespace std;
int main()
{
		freopen("input1A.txt", "r", stdin);
 	 freopen("output1A.txt", "w", stdout);

	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		long long d,n;
		cin >> d >> n;
		double min = -1;
		for(int j=1;j<=n;j++)
		{
			long long s,k;
			cin >> s >> k;
			double p = (double)(d-s)/k;
			if(p>min)
				min=p;
		}
		double ans = (double)d/min;
		printf("Case #%d: %.6lf\n",i,ans);
	}
}

#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main()
{
	ios::sync_with_stdio(false);
	ll t,d,n,k,s;
	double v;
	cin>>t;
	for(int j = 1; j<=t;++j)
	{
		cin>>d>>n;
		double min = -1;
		for(int i =0; i< n; ++i)
		{
			cin>>k>>s;
			v = (d-k)/(double)s;
			if(v>min)
			{
				min = v;
			}
		}
		// cout<<min;
		double temp = d/min;
		printf("Case #%d: %.6lf\n", j, temp);
	}
	return 0;
}
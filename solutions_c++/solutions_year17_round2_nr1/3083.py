#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
	ios_base::sync_with_stdio(false);
	
	int t;
	cin>>t;
	for(int it=1; it<=t; it++)
	{
		int d, n;
		cin>>d>>n;
		double time=-1;
		while(n--)
		{
			double k, s;
			cin>>k>>s;
			double ti=(d-k)/s;
			if(ti>time)
				time=ti;
		}
		double ans=d/time;
		printf("Case #%d: %.7lf\n",it,ans);
	}
	
	return 0;
}

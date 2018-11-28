#include "bits/stdc++.h"
using namespace std;
typedef long long ll;

int main()
{
	int t;
	cin>>t;
	for(int case1=1;case1<=t;case1++)
	{
		int d,n;
		cin>>d>>n;
		int a[n][2];
		for(int i=0;i<n;i++)cin>>a[i][0]>>a[i][1];
		for(int i=0;i<n;i++)
		{
			a[i][0]=d-a[i][0];
		}
		double dist=-1;
		for(int i=0;i<n;i++)
		{
			dist=max(dist,double(a[i][0])/double(a[i][1]));
		}
		dist=double(d)/dist;
		printf("Case #%d: %lf\n",case1,dist);
	}

	return 0;
}

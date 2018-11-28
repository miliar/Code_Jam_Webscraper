#include <bits/stdc++.h>
using namespace std;
#define f(i,n)	for(int i=0;i<n;i++)
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	f(ii,t)
	{
		long double d;
		int n;
		cin>>d>>n;
		long double a[n];
		long double p[n],s[n];
		f(i,n)
		{
			cin>>p[i]>>s[i];
		}
		for(int i=n-1;i>=0;i--)
		{
			a[i]=(d-p[i])/s[i];
			if(i!=n-1)
			{
				a[i]=max(a[i],a[i+1]);
			}
		}
		printf("Case #%d: %.7lf\n",ii+1,double(d/a[0]));

	}

	return 0;
}

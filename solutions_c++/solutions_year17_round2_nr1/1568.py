#include<bits/stdc++.h>
using namespace std;
#define int long long
#define s second
#define f first
ofstream out("output.txt");
void solve(int now)
{
	int d,n;
	cin>>d>>n;
	vector<pair<int,int> >a(n);
	for (int i=0;i<n;i++)
	{
		cin>>a[i].f>>a[i].s;
	}
	sort(a.begin(),a.end());
	long double l=0,r=1e18;
	while (l<r-0.000001)
	{
		long double mid=(l+r)/2;
		long double time=d/mid;
		bool was=1;
		for (int i=n-1;i>=0;i--)
		{
			if (a[i].s*time+a[i].f<d)
			{
				was=0;
			}
		}
		if (was==0)
		{
			r=mid;
		}
		else 
		{
			l=mid;
		}
	}
	out<<"Case #"<<now<<": "<<setprecision(13)<<l<<"\n";
}
signed main()
{
	int t,now=1;
	cin>>t;
	while (t--)
	{
		solve(now);
		now++;
	}
	return 0;
}

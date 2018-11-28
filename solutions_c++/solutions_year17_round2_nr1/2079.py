#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fast cin.sync_with_stdio(0);cin.tie(0)
pair<double ,double>p[100010];
inline bool comp(pair<double,double>p1,pair<double,double>p2)
{
	return p1.first<p2.first;
}
int main()
{
	int viv=0;
	int t;
	cin>>t;
	while(t--)
	{
		double d;
		int n,i;
		viv++;
		cout<<"Case #"<<viv<<": ";
		cin>>d>>n;
		for(i=1;i<=n;i++)
		{
			cin>>p[i].first;
			cin>>p[i].second;
		}
		sort(p+1,p+n+1,comp);
		double low=0;
		double high=999999999999999999;
		double ans=0;
		ll cnt=250;
		while(cnt--)
		{
			bool ok=true;
			double mid=(low+high)/2;
			if(mid==0)break;
			double time_taken=(double)d/mid;
			for(i=n;i>=1;i--)
			{
				double diss=(p[i].second*mid)+p[i].first;
				double timee=(d-p[i].first)/p[i].second;
				if(timee>=time_taken)
				{
					ok=false;
				}
			}
			if(ok)
			{
				ans=mid+0.0000001;
				low=mid+0.0000001;
			}
			else
			{
				high=mid+0.0000001;
			}
		}
		double bb=ans;
		printf("%.06lf\n",bb);

	}
}	
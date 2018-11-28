#include<bits/stdc++.h>
using namespace std;
#define pi 3.14159265358979323846
double r[1005],h[1005];
int main()
{
	int t;
	scanf("%d",&t);
	int y=1;
	while(t--)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		vector< pair<double,int> >v;
		for(int i=1;i<=n;i++)
		{
			scanf("%lf %lf",&r[i],&h[i]);
			v.push_back(make_pair(r[i]*h[i],i));
		}
		sort(v.begin(),v.end());
		reverse(v.begin(),v.end());
		double maxi=0;
		for(int i=1;i<=n;i++)
		{
			double ans=r[i]*r[i]+2*r[i]*h[i];
			int cnt=1;
			for(int j=0;j<v.size();j++)
			{
				if(cnt==k)
					break;
				if(v[j].second==i)
					continue;
				if(r[v[j].second]>r[i])
					continue;
				cnt++;
				ans=ans+2*v[j].first;
			}
			maxi=max(maxi,ans*pi);
		}
		printf("Case #%d: %0.10lf\n",y++,maxi );
		
	}
	return 0;
}
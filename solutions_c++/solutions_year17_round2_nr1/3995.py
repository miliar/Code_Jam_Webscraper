#include<bits/stdc++.h>
using namespace std;
int  main()
{
	int t;
	scanf("%d",&t);
	int y=1;
	while(t--)
	{
		 int n,d;
		scanf("%d %d",&d,&n);
		vector< pair<int,int> >v;
		for(int i=0;i<n;i++){
			int k,s;
			scanf("%d %d",&k,&s);
			v.push_back(make_pair(k,s));
		}
		v.push_back(make_pair(d,0));
		sort(v.begin(),v.end());
		double val[1005],mini=1e13;
		for(int i=0;i<n;i++)
		{
			if(v[i].second>v[i+1].first)
			{
				double t=((double)v[i+1].first-(double)v[i].first)/((double)v[i].second-(double)v[i+1].second);
				val[i]=v[i].first/t;
				val[i]=val[i]+v[i].second;
			}
			else
			{
				double t=(d-(double)v[i].first)/v[i].second;
				val[i]=v[i].first/t;
				val[i]=val[i]+v[i].second;
			}
			mini=min(mini,val[i]);
		}
		printf("Case #%d: %0.10lf\n",y++,mini );
	}
	return 0;
}
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int t,z;
	freopen("A-large.in","r",stdin);
	freopen("A-largeout.txt","w",stdout);
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int n,k;
		cout<<"Case #"<<z<<":"<<" ";
		cin>>n>>k;
		int i;
		pair<double,double> v[n];
		double a,b;
		for(i=0;i<n;i++)
		{
			cin>>a>>b;
			v[i]=(make_pair(2*a*b,a));	
		}
		sort(v,v+n);
		reverse(v,v+n);
		int j;
		double area=0;
		double rtmp=0;
		int flg=0;
		for(i=0;i<k-1;i++)
		{
			area+=v[i].first;
			if(v[i].second>rtmp)
			{
				rtmp=v[i].second;
			}
		}
		double tmp=v[i].first;
		if(v[i].second>rtmp)
		{
			tmp=tmp+v[i].second*v[i].second;
			flg=1;
		}
		double tmp1;
		for(i++;i<n;i++)
		{
			tmp1=v[i].second;
			if(flg==0)
			{
				if(v[i].first+tmp1*tmp1>tmp+rtmp*rtmp)
				{
					tmp=v[i].first+tmp1*tmp1;
					rtmp=v[i].second;
					flg=1;
				}
			}
			else
			{
				if(v[i].first+tmp1*tmp1>tmp)
				{
					tmp=v[i].first+tmp1*tmp1;
					rtmp=v[i].second;
					flg=1;
				}
			}
		}
		if(flg==0)
			area+=rtmp*rtmp;
		printf("%0.9lf\n",3.141592653589793*(area+tmp));
	}
}

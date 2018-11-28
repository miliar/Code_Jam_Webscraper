#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;
double PI=3.1415926535897932384626433;
main()
{
	int t;cin>>t;
	for(int count=1;count<=t;count++)
	{
		int n,k;cin>>n>>k;
		vector<pair<double,double> >a;
		for(int i=0;i<n;i++)
		{
			double r,h;
			cin>>r>>h;
			a.push_back(make_pair(PI*r*r,2*PI*r*h));
		}
		double ans=0;
		sort(a.begin(),a.end(),greater<pair<double,double> >());
		for(int i=0;i<=n-k;i++)
		{
			double sum=a[i].first+a[i].second;
			vector<double>b;
			for(int j=i+1;j<n;j++)b.push_back(a[j].second);
			sort(b.begin(),b.end(),greater<double>());
			for(int j=0;j<k-1;j++)sum+=b[j];
			ans=max(ans,sum);
		}
		cout<<"Case #"<<count<<": "<<fixed<<setprecision(9)<<ans<<endl;
	}
}

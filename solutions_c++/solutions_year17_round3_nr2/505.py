#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
main()
{
	int t;cin>>t;
	for(int count=1;count<=t;count++)
	{
		int C[3]={};cin>>C[1]>>C[2];
		int c[3][100][2];
		int sum[3]={};
		vector<pair<pair<int,int>,int> >a;
		for(int i=0;i<C[1];i++)
		{
			cin>>c[1][i][0]>>c[1][i][1];
			sum[1]+=c[1][i][1]-c[1][i][0];
			a.push_back(make_pair(make_pair(c[1][i][0],c[1][i][1]),1));
		}
		for(int i=0;i<C[2];i++)
		{
			cin>>c[2][i][0]>>c[2][i][1];
			sum[2]+=c[2][i][1]-c[2][i][0];
			a.push_back(make_pair(make_pair(c[2][i][0],c[2][i][1]),2));
		}
		sort(a.begin(),a.end());
		a.push_back(make_pair(make_pair(a[0].first.first+1440,a[0].first.second+1440),a[0].second));
		sum[1]=720-sum[1];
		sum[2]=720-sum[2];
		vector<pair<int,int> >b;
		int ans=0;
		for(int i=0;i<int(a.size())-1;i++)
		{
			if(a[i].second!=a[i+1].second)ans++;
			else if(a[i].first.second<a[i+1].first.first)
				b.push_back(make_pair(a[i+1].first.first-a[i].first.second,a[i].second));
		}
		ans+=a[0].second!=a[int(a.size())-1].second;
		sort(b.begin(),b.end());
		for(int i=0;i<b.size();i++)
		{
			int pos=b[i].second;
			if(sum[pos]-b[i].first<0)ans+=2;
			else sum[pos]-=b[i].first;
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,m=1;
	cin>>t;
	while(t--)
	{
		int n,k,i,j;
		cin>>n>>k;
		vector<pair<long long int,long long int> >v;
		double ans=0;
		for(i=0;i<n;i++)
		{
			long long int a,b;
			cin>>a>>b;
			//r h
			v.push_back(make_pair(-a,2*a*b));
		}
		sort(v.begin(),v.end());
		for(i=0;i<=n-k;i++)
		{
			double r=-v[i].first,h=v[i].second;
			vector<long long int>temp;
			for(j=i+1;j<n;j++)
			temp.push_back(-v[j].second);
			sort(temp.begin(),temp.end());
			for(j=0;j<k-1;j++)
			h-=temp[j];
		//	cout<<r<<" "<<h<<endl;
			ans=max(ans,r*r+h);
		}
		ans=ans*atan(1)*4;
		printf("Case #%d: %.10lf\n",m,ans);
		m++;
	}
	return 0;
}

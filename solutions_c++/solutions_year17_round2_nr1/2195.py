#include<bits/stdc++.h>
using namespace std;
pair<long long,long long> info[1010];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;

	long long d;

	int n;

	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<": ";
		cin>>d;
		cin>>n;

		for(int i=1;i<=n;i++)
		{
			cin>>info[i].first>>info[i].second;
		}
		sort(info+1,info+n+1);


		//start with last horse

		long double tm = (1.0*(d-info[n].first))/info[n].second;

		for(int i=n-1;i>=1;i--)
		{
			if((1.0*(d-info[i].first))>=info[i].second*tm)
			{
				tm = (1.0*(d-info[i].first))/info[i].second;
			}
		}

		long double ans = (1.0*d)/tm;

		cout<<fixed<<setprecision(10)<<ans<<endl;

	}
}

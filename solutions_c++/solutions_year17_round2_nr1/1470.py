#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define pll pair<ll,ll>
int main()
{
	ll test;
	cin>>test;
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(6);
	for(ll cases=1;cases<=test;cases++)
	{
		ll n,d;
		cin>>d>>n;
		vector<pair<double,double> > v;
		for(int i=0;i<n;i++)
		{
			double k,s;
			cin>>k>>s;
			v.push_back({k,s});
		}
		cout<<"Case #"<<cases<<": ";
		sort(v.begin(),v.end());
		//reverse(v.begin(),c.end());
		double dist[n];
		dist[n-1]=d;
		for(int i=n-2;i>=0;i--)
		{
			for(int j=i+1;j<n;j++)
			{
				double dist1=v[i].first-v[j].first;
				double speed=v[i].second-v[j].second;
				double time=((double)dist1)/(double)(-1*speed);
				//cout<<time<<"\n";
				if(time<0||time>((double)(dist[i]-v[i].first))/v[i].second)
				{
					continue;
				}
				else
				{
					//cout<<time<<"c\n";
					dist[i]=v[i].first+time*v[i].second;
					break;
				}
			}
			if(dist[i]<=0.00000001)
				dist[i]=d;
			//cout<<v[i].first<<"\n";
			//cout<<dist[i]<<"\n";
		}
		double speed=1e200;
		for(int i=0;i<n;i++)
		{
			speed=min(speed,dist[i]/((dist[i]-v[i].first)/v[i].second));
		}

		cout<<speed<<"\n";
	}
}
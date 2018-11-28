#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
#define pb push_back
long double p[55];
map<long double,int> m;
map<long double,int> ::iterator it,jt,kt;
void print()
{
	for(kt=m.begin();kt!=m.end();kt++)
	{
		cout<<kt->first<<" "<<kt->second<<endl;
	}
	cout<<endl;
}
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	ll n,k;
	long double u;
	while(t--)
	{
		z++;
		cin>>n>>k;
		cin>>u;
		for(int i=0;i<n;i++)
		{
			cin>>p[i];
			m[p[i]]++;
		}
		if(m.find(1.000)==m.end())
		{
			m.insert({1.0000,0});
		}
		cout<<"Case #"<<z<<": ";
		long double lar=1.00000;
		long double smal;
		long long cnt;
		int lll=0;
		bool b;
		while(u>0.000000 && !m.empty())
		{
			b=false;
			it=m.begin();
			jt=m.begin();
			cnt=it->second;
			smal=it->first;
			lar=1.0000;
			jt++;
			if(jt!=m.end())
			{
				b=true;
				lar=min(lar,jt->first);
			}
			// cout<<smal<<" "<<lar<<" "<<u<<endl;
			// print();
			if(u>=((lar-it->first)*it->second))
			{
				u=u-((lar-it->first)*it->second);
				m.erase(m.begin());
				smal=lar;
				if(b==true)
				{
					// cout<<"Increasing to "<<m.begin()->first<<endl;
					m.begin()->second+=cnt;
				}
				else
				{
					m[1.00000]+=cnt;	
				}
				
				// cout<<m[smal]<<endl;
			}
			else
			{
				smal=smal+(u/cnt);
				u=0.0000000;m.erase(it);
				m[smal]+=cnt;

				break;
				

			}
			if(m.size()==1)
				break;
		}
		long double ans=1.0000;
		for(it=m.begin();it!=m.end();it++)
		{
			for(int i=0;i<it->second;i++)
			{
				ans=ans*it->first;
			}
		}
		m.clear();
		
		cout<<fixed<<setprecision(7)<<ans<<endl;
	}
}
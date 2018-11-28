#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
#define pb push_back
vector <pair<ll,ll> > a,b;
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	ll n,m;
	ll s,e;
	while(t--)
	{
		z++;
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			cin>>s>>e;
			a.push_back({s,e});
		}
		for(int i=0;i<m;i++)
		{
			cin>>s>>e;
			b.push_back({s,e});
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		cout<<"Case #"<<z<<": ";
		if(n+m==1)
		{
			if(n==1)
			{
				if(a[0].first>=720 || a[0].second<720)
				{
					cout<<2<<endl;
				}
				else
				{
					cout<<2<<endl;
				}
			}	
			else
			{
				if(b[0].first>=720 || b[0].second<720)
				{
					cout<<2<<endl;
				}
				else
				{
					cout<<2<<endl;
				}
			}
		}
		else
		{
			if(n==2)
			{
				if(a[0].first>=720 || max(a[0].second,a[1].second)<720)
				{
					cout<<2<<endl;
				}
				else if(a[0].second<a[1].first && abs(a[1].first-a[0].second)>=720)
				{
					cout<<2<<endl;
				}
				else if(abs(a[1].second-a[0].first)<=720)
				{
					cout<<2<<endl;
				}
				else
				{
					ll a1=a[0].first;
					ll b1=abs(a[1].first-a[0].second);
					ll c1=1440-a[1].second;
					if(a1+b1>=720 || b1+c1>=720)
					{
						cout<<4<<endl;
					}
					else
					{
						cout<<4<<endl;
					}
				}
			}
			else if(m==2)
			{
				if(b[0].first>=720 || max(b[0].second,b[1].second)<720)
				{
					cout<<2<<endl;
				}
				else if(b[0].second<b[1].first && abs(b[1].first-b[0].second)>=720)
				{
					cout<<2<<endl;
				}
				else if((abs(b[1].second-b[0].first))<=720)
				{
					cout<<2<<endl;
				}
				else
				{
					ll a1=b[0].first;
					ll b1=abs(b[1].first-b[0].second);
					ll c1=1440-b[1].second;
					if(a1+b1>=720 || b1+c1>=720)
					{
						cout<<4<<endl;
					}
					else
					{
						cout<<4<<endl;
					}
				}
			}
			else
			{
				if((a[0].second<=720&& b[0].first>=720) || (b[0].second<=720&& a[0].first>=720))
				{
					cout<<2<<endl;
				}
				else
				{
					cout<<2<<endl;
				}
			}
		}
		a.clear();
		b.clear();
	}
}
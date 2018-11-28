#include"bits/stdc++.h"
using namespace std;
#define ll long long int
#define mod 1000000007
#define pb push_back

int main()
{
	ll tt,u=1;
	cin>>tt;
	while(tt--)
	{
		ll n,i,j;
		cin>>n;
		vector<ll> vv;
		for(i=n;i!=0;i/=10)
		{
			vv.pb(i%10);
		}
		ll l=vv.size();
		ll b[vv.size()];
		for(i=0;i<vv.size();i++)
		{
			b[i]=vv[vv.size()-1-i];
		}
		ll loc=-1;
		ll p=b[0];
		for(i=0;i<l-1;i++)
		{
			if(b[i+1]>=b[i])
			{
				continue;
			}
			else
			{
				loc=i;
				break;
			}
		}
		cout<<"Case #"<<u<<": ";
		u++;
		if(loc==-1)
		{
			cout<<n<<endl;
			continue;
		}
		for(i=loc;i>=0;i--)
		{
			if(i==loc)
			{
				b[i]--;
			}
			else
			{
				if(b[i+1]<b[i])
				{
					b[i]--;
				}
			}
		}
		if(b[0]==p-1)
		{
			for(i=1;i<l;i++) b[i]=9;
		}
		if(b[0]==0)
		{
			for(i=0;i<l-1;i++)
			{
				b[i]=9;
				cout<<b[i];
			}
			cout<<endl;
		}
		else
		{
			for(i=0;i<=loc;i++)
			{
				cout<<b[i];
			}
			for(i==loc+1;i<l;i++)
			cout<<9;
			cout<<endl;
		}
	}
}

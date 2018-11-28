#include <bits/stdc++.h>
#define ll long long int
#define ld long double 
#define MOD 1000000007 
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define ff first
#define ss second 
#define ios ios_base::sync_with_stdio(false);

using namespace std;

ll a[1010];

int main()
{
	ll t,k;
	string s;
	cin>>t;
	for(ll i=1; i<=t; i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>s; 
		cin>>k;
		mem(a);
		ll ans=0;
		for(ll i=0; i<s.length(); i++)
		{
			if(s[i]=='+')
				a[i]=1;
			else
				a[i]=0;
		} 
		for(ll i=0; i<=s.length()-k; i++)
		{
			if(a[i]!=1)
			{
				ans++; 
				for(ll j=i; j<i+k; j++)
				{
					a[j]^=1;
				}
			} 
		}
		
		for(ll i=0; i<s.length(); i++)
		{
			if(a[i]==0)
			{
				ans=-1;
				break;
			} 
		}
		if(ans!=-1)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define lb lower_bound
#define ub upper_bound
#define lim 100005
#define mk make_pair
#define pll pair<ll,ll> 
#define pb push_back
#define X first
#define Y second
#define MOD 1000000007
#define rep(a,b,c) for(a=b;a<c;a++)
#define mem(a,b) memset(a,b,sizeof(a))
#define ios ios_base::sync_with_stdio(0)

ll a,b,c,d;

void print(ll abc[],ll n)
{
	for(ll a=0;a<n;a++)
	cout<<abc[a]<<" ";
}
ll mark[lim];

ll cnt(string s,char x)
{
	ll a;
	ll ct=0;
	for(a=0;a<s.size();a++)
	{
		if(s[a]==x)
		ct++;
	}
	return ct;
}

string conv(string s,ll a,ll k)
{
	ll i,j;
	for(i=a;i<=a+k;i++)
	{
		if(s[i]=='+')
		s[i]='-';
		else
		s[i]='+';
	}
	return s;
}

int main(void)
{
	ios;
	ll n,k,e,m,t,q,f;
	ll a,b,c;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	string s;
	ll ans=0;
	for(ll i=1;i<=t;i++)
	{
		cin>>s>>k;
		ans=0;
		for(a=0;a<=s.size()-k;a++)
			{
				if(s[a]=='-')
				{
					s=conv(s,a,k-1),ans++;
					//cout<<s<<endl;
				}
				
			}
			if(cnt(s,'+')==s.size())
			cout<<"Case #"<<i<<": "<<ans<<endl;
			else
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
	}
	return 0;
}

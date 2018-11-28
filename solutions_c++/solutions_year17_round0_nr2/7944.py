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


bool chck(string s)
{
	for(a=0;a<s.size()-1;a++)
	{
		if(s[a]>s[a+1])
		return 0;
	}
	return 1;
}

string pr(string s)
{
	string r;
	ll i=0;
	while(s[i]=='0')
	{
		i++;
	}
	while(i<s.size())
	{
		r.pb(s[i]);
		i++;
	}
	return r;
}

int main(void)
{
	ios;
	ll n,k,e,m,t,q,f,tes;
	ll a,b,c;
	freopen("input2.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>t;
	string s;
	ll ans=0;
	for(ll i=1;i<=t;i++)
	{
		cin>>s;
		while(!chck(s))
		{
		for(a=0;a<s.size()-1;a++)
		{
			if(s[a]>s[a+1])
			{
				s[a]--;
				break;
			}
		}
		a++;
		while(a<s.size())
		s[a]='9',a++;
		s=pr(s);
		}
		cout<<"Case #"<<i<<": "<<s<<endl;	
	}
	return 0;
}

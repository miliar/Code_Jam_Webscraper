#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long 
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define graph std::vector<std::vector<ll> > 
#define sc(x) scanf("%lld",&x)
#define sp " "
using namespace std;

ll ison(ll x,ll i)
{
	return x&(1ll<<i);
}

const ll MOD=1e9+7;
const double PI =acos(-1.0);
const ll MAX=1e13;
const ll N=20;

char o[N];
string s;
ll n;
void rec(ll idx,ll state)
{
	if(state==0)
	{
		if(idx==n-1 || s[idx]<=s[idx+1]) 
		{
			o[idx]=s[idx];
			if(idx!=n-1) rec(idx+1,0);
		}
		else
		{
			if(idx==0 || s[idx-1]<=s[idx]-1)
			{
				o[idx]=s[idx]-1;
				if(idx!=n-1) rec(idx+1,1);
			}
			else
			{
				rec(idx-1,2);
			}
		}
	}
	else if(state==1)
	{
		o[idx]='9';
		if(idx!=n-1) rec(idx+1,1);
	}
	else
	{
		if(idx==0 || s[idx-1]<=s[idx]-1)
		{
			o[idx]=s[idx]-1;
			if(idx!=n-1) rec(idx+1,1);
		}
		else
		{
				rec(idx-1,2);
		}
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll t;
	cin>>t;
	for (int tc = 0; tc < t; ++tc)
	{
		cin>>s;
		n=s.length();
		rec(0,0);
		bool f=true;
		cout<<"Case #"<<tc+1<<": ";
		for (int i = 0; i < n; ++i)
		{
			if(o[i]<='0' && f)
			{
				continue;
			}
			else
			{
				cout<<o[i];
				f=false;
			}
		}
		cout<<"\n";
	}
	return 0;
}
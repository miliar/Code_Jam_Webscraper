#include <bits/stdc++.h>
#define mod 1000000007
#define INF 1000000000000000007LL
#define SZ 300009
#define ull unsigned long long
#define ll long long int
#define ld long double
#define fi first
#define se second
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
#define all(v) ((v).begin()), ((v).end())
#define ios ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define db(...) ZZ(#__VA_ARGS__, __VA_ARGS__)
#define dbvv(v) cout << "Printing "#v << " --> \n"; for(ll i=0;i<v.size();i++) {for(ll j=0;j<v[i].size();j++) cout << v[i][j] << " "; cout << "\n";}
#define dbv(st) cout << "Printing "#st << " --> \n"; for(auto i=st.begin();i!=st.end();i++) cout << *i << " "; cout << "\n";
#define dbvp(st) cout << "Printing "#st << " --> \n"; for(auto i=st.begin();i!=st.end();i++) cout << i->first << " " << i->second << "\n"; cout << "\n";
#define dbmp(mp) cout << "Printing "#mp << " --> \n"; for(auto i=mp.begin();i!=mp.end();i++) cout << #mp"[" << i->first << "]"<< " = " << i->second << "\n";
#define dbar(ar,st,en) cout << "Printing "#ar << " --> \n"; for(auto it=st;it!=en;it++) cout << *it << " "; cout << "\n";
#define dbmar(ar,rowz,colz) cout << "Printing "#ar << " --> \n"; for(auto i=0;i<rowz;i++) {for(auto j=0;j<colz;j++) cout << ar[i][j] << " "; cout << "\n";}
template <typename Arg1>void ZZ(const char* name, Arg1&& arg1){std::cout << name << " = " << arg1 << std::endl;}
template <typename Arg1, typename... Args>void ZZ(const char* names, Arg1&& arg1, Args&&... args)
{
    const char* comma = strchr(names + 1, ',');
    std::cout.write(names, comma - names) << " = " << arg1;
    ZZ(comma, args...);
}
using namespace std;

ll to_ll(string &s)
{
	ll i,ret=0,p=1;
	for(i=(ll)s.length()-1;i>=0;i--) ret+=(s[i]-'0')*p, p*=10LL;
	return ret;
}
ll gcd(ll x,ll y)
{
	if(y==0) return x;
	return gcd(y,x%y);
}
ll pwr(ll base,ll expo,ll m)
{
	if(base==0) return 0LL;
	if(expo==0) return (1LL%m);
	if((expo&1)==0) {ll temp=pwr(base,expo>>1,m); return (temp*temp)%m;}
	return ((base%m)*pwr(base,expo-1,m))%mod;
}
/*
-----------------------------------------------------------------------------------------------------------------------------------------
##########################
## Author: Viral Mehta  ##
## College: BITS Pilani ##
##########################
-----------------------------------------------------------------------------------------------------------------------------------------
*/
ll n,k;
int main()
{
	ios;
	ll t,tc;
	cin>>t;
	for(tc=1;tc<=t;tc++)
	{
		cin>>n>>k;
		map<ll,ll> mp;
		set<ll> st;
		st.insert(n); mp[n]=1;
		while(!st.empty())
		{
			ll val=*st.rbegin();
			if(val%2==0)
			{
				ll p1=(val-1)>>1;
				ll p2=val-p1-1;
				if(p1>0) {mp[p1]+=mp[val];st.insert(p1);}
				if(p2>0) {mp[p2]+=mp[val];st.insert(p2);}
			}
			else
			{
				ll p1=(val-1)>>1;
				ll p2=p1;
				if(p1>0) {mp[p1]+=mp[val];st.insert(p1);}
				if(p2>0) {mp[p2]+=mp[val];st.insert(p2);}
			}
			st.erase(val);
		}
		//dbmp(mp);
		ll cnt=0;
		for(auto it=mp.rbegin();it!=mp.rend();it++)
		{
			cnt+=(it->second);
			if(cnt>=k)
			{
				ll val=it->first;
				ll LS=(val-1)>>1;
				ll RS=val-LS-1;
				cout << "Case #" << tc << ": " << max(LS,RS) << " " << min(LS,RS) << "\n";
				break;
			}
		}
	}
	return 0;
}
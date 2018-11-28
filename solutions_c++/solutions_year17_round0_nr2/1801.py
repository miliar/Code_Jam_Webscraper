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
ll dp[11][20];
bool vis[11][20];
vector<ll> ar;
ll f(ll prev,ll n)
{
    if(n==0) 
    {
        if(prev>0) return 1;
        return 0;
    }
    if(vis[prev][n]==1) return dp[prev][n];
    vis[prev][n]=1;
    ll i,ret=0;
    for(i=prev;i<=9;i++)
    {
        ret+=f(i,n-1);
    }
    return dp[prev][n]=ret;
}
ll solve(string str)
{
    ll idx,n=str.length(); ar.clear(); ar.resize(n);
    for(idx=0;idx<n;idx++) ar[idx]=str[idx]-'0';ll ret=0;
    ll dig,prev;
    for(idx=0;idx<n;idx++)
    {
        //db(str);
        //db(idx);
        if(idx==0) prev=0;
        else prev=str[idx-1]-'0';
        if(idx>0&&str[idx]<str[idx-1]) break;
        //db(idx,"meow");
        for(dig=prev;dig<str[idx]-'0';dig++)
        {
            ll len=n-idx-1;
            ll val=f(dig,len);
            //db(idx,dig,len,val);
            ret+=val;
        }
    }
    return ret;
}
int main()
{
	ios;
	ll t,tc,i,j;
	cin>>t;
	ll N;
	for(tc=1;tc<=t;tc++)
	{
	    cin>>N;
	    N++;
	    ll ans;
	    string s=to_string(N);
	    ll val=solve(s);
	    //db(s,val);
	    ll x,lo=1; ll hi=N+20; ll mid;
	    while(hi-lo>1)
	    {
	        ll mid=lo+(hi-lo)/2;
	        ll dp[11][20];
	        bool vis[11][20];
	        for(i=0;i<11;i++)
	        {
	            for(j=0;j<20;j++)
	            {
	                dp[i][j]=0;
	                vis[i][j]=0;
	            }
	        }
	        x=solve(to_string(mid));
	        if(x==val) hi=mid;
	        else if(x<val) lo=mid+1;
	        else hi=mid;
	    }
	    for(i=0;i<11;i++)
	        {
	            for(j=0;j<20;j++)
	            {
	                dp[i][j]=0;
	                vis[i][j]=0;
	            }
	        }
	    if(solve(to_string(lo))==val) ans=--lo;
	    else ans=--hi;
	    cout << "Case #" << tc << ": " << ans << "\n";
	}
	return 0;
}

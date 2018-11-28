#define ll long long
#define mod 1000000007LL
#define F(a,b,c) for(a=b;a<c;a++)
#define Fr(a,b,c) for(a=b;a>=c;a--)
#define pf printf
#define sfd(a) scanf("%d",&a)
#define sfdd(a,b) scanf("%d%d",&a,&b)
#define sfl(a) scanf("%lld",&a)
#define sfll(a,b) scanf("%lld%lld",&a,&b)
#define pfd(a) printf("%d",a)
#define pfl(a) printf("%lld",a)
#define sf scanf
#define line printf("\n")
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define let(x,a) __typeof(a) x(a)
#define forall(it,v) for(it=v.begin();it!=v.end();it++)
ll ra[1003],he[1003],dp[1003][1003],inf=10000000000000000LL;
int n;
ll fun(int rem,int po){
	if(po>=n){
		if(rem)
			return -inf;
		return 0;
	}
	if(!rem)
		return 0;
	ll &x=dp[po][rem];
	if(x!=-1)
		return x;
	return x=max(fun(rem-1,po+1)+ra[po]*he[po],fun(rem,po+1));
}
int main(){
int t;
sfd(t);
int k=1;
while(k<=t){
	int kk,i,r,h;
	std::vector<pair<int,int> > v;
	memset(dp,-1,sizeof dp);
	pf("Case #%d: ",k);
	sfdd(n,kk);
	F(i,0,n)
		sfdd(r,h),v.pb(mp(r,h));
	sort(v.rbegin(),v.rend());
	F(i,0,n)
		ra[i]=v[i].first,he[i]=v[i].second;
	double an=0,pi=acos(-1);
	F(i,0,n)
		an=max(an,pi*ra[i]*ra[i]+2*pi*fun(kk-1,i+1)+2*pi*ra[i]*he[i]);
	pf("%.8lf\n",an);
	k++;
}
return 0;
}

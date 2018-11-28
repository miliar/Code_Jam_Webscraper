//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define ii pair<ll,ll>
#define dd pair<long double,ll>
#define ff first
#define ss second
#define ll long long

ll n,k;
ii cake[1005];
dd dp[1005][1005];

//ans, last index
dd f(ll idx, ll req){
	// printf("IN %lld %lld %lld %lld\n",idx,req,cake[idx].ff,cake[idx].ss);
	ll i,j;
	dd &ans = dp[idx][req];
	dd ans1, ans2;
	if(ans != dd(-1,-1)) return ans;
	if(req == 0) return ans = ii(0,-1);
	if(idx + 1 == req){
		ans.ff = (long double) M_PI * cake[idx].ff * cake[idx].ff;
		for(i=0;i<=idx;i++)
			ans.ff += (long double) M_PI * 2.0 * cake[i].ff * cake[i].ss;
		ans.ss = idx;
		// printf("OUT %lld %lld %lld %lld %.12Lf %lld\n",idx,req,cake[idx].ff,cake[idx].ss,ans.ff,ans.ss);
		return ans;
	}
	ans1 = f(idx - 1, req);
	ans2 = f(idx - 1, req - 1);
	if(ans2.ss > -1)
		ans2.ff -= (long double) M_PI * cake[ans2.ss].ff * cake[ans2.ss].ff;
	ans2.ff += (long double) M_PI * cake[idx].ff * cake[idx].ff;
	ans2.ff += (long double) M_PI * 2.0 * cake[idx].ff * cake[idx].ss;
	ans2.ss = idx;
	if(ans2.ff >= ans1.ff){
		ans.ff = ans2.ff;
		ans.ss = ans2.ss;
		// printf("OUT %lld %lld %lld %lld %.12Lf %lld\n",idx,req,cake[idx].ff,cake[idx].ss,ans.ff,ans.ss);
		return ans;
	}
	ans.ff = ans1.ff;
	ans.ss = ans1.ss;
		// printf("OUT %lld %lld %lld %lld %.12Lf %lld\n",idx,req,cake[idx].ff,cake[idx].ss,ans.ff,ans.ss);
	return ans;
}

int main(){
	freopen ("A-small-attempt6.in","r",stdin); 
	freopen ("A-small-attempt6.out","w",stdout); 
	ll i,j,test,t;
	scanf("%lld",&t);
	for(test = 1; test <= t; test++){
		scanf("%lld %lld",&n,&k);
		for(i=0;i<n;i++)
			scanf("%lld %lld",&cake[i].ff,&cake[i].ss);
		sort(cake,cake+n);
		for(i=0;i<=n;i++)
			for(j=0;j<=k;j++)
				dp[i][j] = dd(-1,-1);
		printf("Case #%lld: %0.12Lf\n",test,f(n-1,k).ff);

	}
    
    return 0;
}
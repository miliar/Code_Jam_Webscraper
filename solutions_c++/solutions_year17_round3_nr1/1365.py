//	Mohib Manva
#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
#define LOCAL 1
#define pb push_back
#define ll long long

ll po(ll a,ll b){
	ll x = 1,y=a;
	while(b>0){
		if(b%2){
			x = x*y;
			x %= mod;
		}
		y=y*y;
		y%=mod;
		b/=2;
	}
	return x;
}

static long double dp[2005][2005];
int n,k;
static pair<long double,long double> a[2005];

long double solve(int ind,int taken){
	if(taken==k){
		return 0.0;
	}
	if(ind==n){
		return -1e9;
	}
	if(dp[ind][taken]!=-1){
		return dp[ind][taken];
	}
	long double ans;
	ans = 2.0 * M_PI * a[ind].first * a[ind].second;
	ans += M_PI * a[ind].first * a[ind].first;
	if(taken!=k-1)
		ans += solve(ind+1,taken+1) - M_PI * a[ind].first * a[ind].first;
	else
		ans += solve(ind+1,taken+1);
	ans = max(ans,solve(ind+1,taken));
	dp[ind][taken] = ans;
	return ans;
}

int main(){
	if(LOCAL){
    	freopen("A-large.in","r",stdin);
    	freopen("output.txt","w+",stdout);
	}
	int T = 1;
	scanf("%d",&T);
	int t = 1;
	while(T--){
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%Lf %Lf",&a[i].first,&a[i].second);
		}
		sort(a,a+n);
		for(int i=0;i<2005;i++){
			for(int j=0;j<2005;j++){
				dp[i][j] = -1.0;
			}
		}
		printf("Case #%d: %.9Lf\n",t++,solve(0,0));
	}
	return 0;	
}
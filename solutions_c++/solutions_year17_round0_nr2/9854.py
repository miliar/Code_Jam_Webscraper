#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 40;
ll n;
int t;
ll dp[N][10][2];
ll cur[N];
ll pot[N];
ll ans;
int sz;
ll number;
const ll inf = 2e18+1;
/*
void solve(int i, ll prev, int k){
	if(i>=sz){
		ans = max(ans,number);
		return;
	}
	for(int j = prev; j  <= (k == 0? 9:cur[i]); j++){
		if(j == cur[i]){
			number = number*10+j;
			solve(i+1,j,1);
			number = number-j;
			number = number/10;
		}
		else{
			number = number*10+j;
			solve(i+1,j,0);
			number = number-j;
			number = number/10;
		}
	}
}*/

ll solve(int i, int j, int k){
	if(i>=sz){
		return 0LL;
	}
	ll &x = dp[i][j][k];
	if(x == -1){
		x = -inf;
		for(int ii = j; ii <= (k == 0?9:cur[i]); ii++){
			if(ii == cur[i])
				x = max(x,solve(i+1,ii,1)+ii*pot[i]); 
			else
				x = max(x,solve(i+1,ii,0)+ii*pot[i]);
		}
	}
	return x;
}

int main () {
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		scanf("%lld", &n);
		sz = 0;
		ll m = n;
		ans = 1;
		ll p = 1;
		memset(dp,-1,sizeof dp);
		while(m > 0){
			cur[sz] = m%10LL;
			pot[sz] = p;
			p*=10LL;
			m/=10LL;
			sz++;
		}
		reverse(cur,cur+sz);
		reverse(pot,pot+sz);
		ans = solve(0,0,1);
		printf("Case #%d: %lld\n",i+1,ans);
	}

	return 0;
} 
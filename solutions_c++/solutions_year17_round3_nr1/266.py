#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;

const int MOD = 1e9 + 7;

const ll oo = 1e15;

typedef long long ll;

int t,n,k,a[1100];

double dp[1100][1100][2];

pdd pan[1100];

double he(double h , double r){
	return 2 * acos(-1) * r * h;
}
double area(double r){
	return r * r* acos(-1);
}

double calc(int idx , int rem , bool take){
	if(rem < 0)
		return -2e18;
	if(idx == n){
		if(rem)
			return -2e18;
		return 0;
	}
	double &ret = dp[idx][rem][take];
	if(ret == ret)
		return ret;
	ret = calc(idx+1,rem,take);
	if(take){
		ret = max(ret,he(pan[idx].second,pan[idx].first)+calc(idx+1,rem-1,take));
	}else{
		ret = max(ret,he(pan[idx].second,pan[idx].first)+area(pan[idx].first)+calc(idx+1,rem-1,1));
	}
	return ret;
}
int main() {
 	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
 	scanf("%d",&t);
 	for(int it = 1; it <= t ; it++){
 		memset(dp,-1,sizeof dp);
 		scanf("%d%d",&n,&k);
 		for (int i = 0; i < n; ++i){
 			scanf("%lf%lf",&pan[i].first,&pan[i].second);
 		}
 		sort(pan,pan+n);
 		reverse(pan,pan+n);
 	/*	for (int i = 0; i < n; ++i){
 			printf("%lf %lf\n",pan[i].first,pan[i].second );
 		}*/
 		printf("Case #%d: %.9lf\n",it,calc(0,k,0));
 	}
	return 0;
}

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> PL;
PL dfs(ll N,ll K){
	if(K==1){
		if(N&1) return PL(N/2,N/2);
		return PL(N/2-1,N/2);
	}
	if((K-1)&1)
		return dfs(N/2,(K-1)/2+1);
	if(N&1)
		return dfs(N/2,(K-1)/2);
	return dfs(N/2-1,(K-1)/2);
}
int main(){
	int tcase,kase=0;
	ll N,K;
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%lld%lld",&N,&K);
		PL ans=dfs(N,K);
		printf("Case #%d: %lld %lld\n",++kase,ans.second,ans.first);
	}
	return 0;
}

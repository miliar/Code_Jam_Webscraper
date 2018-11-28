#include <bits/stdc++.h>
using namespace std;
#define ll long long

int mi(ll N, ll K){
	//cout << N << ' ' << K << endl;
	if(N==0)
		return 0;
	if(K==1){
		if(N&1)
			return N/2;
		return N/2-1;
	}
	if(K&1){
		if(N&1)
			return mi(N/2, K/2);
		return mi(N/2-1, K/2);
	}
	return mi(N/2, K/2);
}

int mx(ll N, ll K){
	//cout << N << ' ' << K << endl;
	if(N==0)
		return 0;
	if(K==1)
		return N/2;
	if(K&1){
		if(N&1)
			return mx(N/2, K/2);
		return mx(N/2-1, K/2);
	}
	return mx(N/2, K/2);
}

int main(){
	int t;
	cin >> t;
	int i;
	for(i=0;i<t;++i){
		ll n, k;
		cin >> n >> k;
		
		printf("Case #%d: ", i+1);
		//cout << solve(n, k) << endl;
		cout << mx(n, k) << ' ' << mi(n, k) << endl;
		/*if(r == -1)
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, r);*/
	}
	return 0;
}
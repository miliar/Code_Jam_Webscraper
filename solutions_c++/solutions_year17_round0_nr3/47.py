#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<queue>
#include<map>
using namespace std;
priority_queue<long long>Q;
map<long long,long long>M;
long long n,K;
void solve(){
	scanf("%lld%lld",&n,&K);
	M.clear();
	while (!Q.empty()) Q.pop();
	M[n]=1; Q.push(n);
	while (1){
		long long k=Q.top(); Q.pop();
		long long L=(k-1)/2,R=k/2;
		if (M[k]>=K){
			printf("%lld %lld\n",R,L); return;
		}
		K-=M[k];
		if (L&&M[L]==0) Q.push(L);
		if (R&&L!=R&&M[R]==0) Q.push(R);
		if (L) M[L]+=M[k]; if (R) M[R]+=M[k];
	}
}
int main(){
	freopen("Cl.in","r",stdin);
	freopen("Cl.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}
	

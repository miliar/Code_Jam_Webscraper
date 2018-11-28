#include<bits/stdc++.h>
using namespace std;
long long y,x;
void solve(long long n,long long k){
	if(k==1){
		y=n/2;
		x=(n-1)/2;
		return;
	}
	long long l=(n-1)/2,r=n/2;
	if(k%2)return solve(l,k/2);
	return solve(r,k/2);
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("outt.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		printf("Case #%d: ",T);
		long long n,k;
		scanf("%lld%lld",&n,&k);
		solve(n,k);
		printf("%lld %lld\n",y,x);
	}

}

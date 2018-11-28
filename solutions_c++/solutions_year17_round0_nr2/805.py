#include <bits/stdc++.h>
using namespace std;
long long base[20];
long long ans;
int dfs(int x,int y,long long rem){
	// printf("%d %d %lld\n", x,y,rem);
	if (rem<0) return 0;
	if (x<0) {ans = min(rem,ans);return 1;}
	int flag = 0;
	for (int i=9;i>=y;i--){
		if (base[x]*(long long)i<=rem){
			if (dfs(x-1,i,rem-base[x]*(long long)i)){
				flag =1;
				break;
			}
		}
	}
	return flag;
}
int main(){
	int T,ca=0;
	freopen("B.out","w",stdout);
	freopen("B.in","r",stdin);
	base[0]=1;
	for (int i=1;i<=17;i++)
		base[i] = base[i-1] *(long long) 10;
	scanf("%d",&T);
	while(T--){
		long long n;
		scanf("%lld",&n);
		ans = n;
		printf("Case #%d: ",++ca );
		dfs(17,0,n);
		printf("%lld\n",n-ans);
	}
	return 0;
}
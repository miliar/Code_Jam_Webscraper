#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
char ch[1100];
int pd[1100],n,K;
void solve(){
	scanf("%s",ch+1); n=strlen(ch+1); scanf("%d",&K); int ans=0;
	for (int i=1;i<=n;i++) if (ch[i]=='+') pd[i]=0; else pd[i]=1;
	for (int i=1;i<=n-K+1;i++)
		if (pd[i]){
			ans++;
			for (int j=1;j<=K;j++)
				pd[i+j-1]^=1;
		}
	for (int i=1;i<=n;i++)
		if (pd[i]==1){
			printf("IMPOSSIBLE\n"); return;
		}
	printf("%d\n",ans);
}
int main(){
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}

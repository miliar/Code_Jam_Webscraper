#include <cstdio>
#include <string.h>
#include <cstdlib>
using namespace std;
char x[1005];
int k,tag[1005];
void input(){
	scanf("%s %d",x,&k);
	for(int i = 0;i < 1005 ;i++) tag[i] = 0;
}
void solve(){
	int ans = 0;
	int len = strlen(x);
	int now = 0,i;
	for(i = 0 ;i < len-k+1 ;i ++){
		now -= tag[i];
		x[i] = x[i]=='-'?0:1;
		if(x[i]^(now%2)!=1){
			ans ++;
			now ++;
			tag[i+k]++;
		}
	}
	bool flag = false;
	for(;i < len ;i++){
		now -=tag[i];
		x[i] = x[i]=='-'?0:1;
		if(x[i]^(now%2)!=1){
			flag = true;
			break;
		}
	}
	if(flag)puts("IMPOSSIBLE");
	else printf("%d\n",ans);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1 ;i <= T ; i++){
		printf("Case #%d: ",i);
		input();
		solve();
	}
}

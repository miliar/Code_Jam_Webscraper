#include <cstdio>
#include <cstring>

void solve(){ 
	int l,k;
	char chrs[1024];
	int ans=0;
	scanf("%s",chrs);
	scanf("%d",&k);
	l=strlen(chrs);
	for(int i=0;i<l;i++){
		chrs[i]=chrs[i]=='+'?1:0;
	}
	for(int i=0;i<l-k+1;i++){
		if(chrs[i]==0){
			ans++;
			for(int xhk=0;xhk<k;xhk++){
				chrs[i+xhk]^=1;
			}
		}
	}
	for(int i=l-k+1;i<l;i++){
		if(chrs[i]==0){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n",ans);
}
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

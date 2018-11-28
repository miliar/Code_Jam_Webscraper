#include<bits/stdc++.h>
using namespace std;
int N,P,ans,cnt[4],a[110],maxd;
bool dfs(int dep,int mod){
	if(mod==0 && dep==maxd){
		ans++;
		return true;
	}
	if(dep==maxd) return false;
	for(int i=1;i<P;i++){
		if(cnt[i]>0){
			cnt[i]--;
			if(!dfs(dep+1,(mod+i)%P)){
				cnt[i]++;
			}else return true;
		}
	}
	return false;
}
int main(){
	int tcase,kase=0;
	scanf("%d",&tcase);
	while(tcase--){
		ans=0;
		scanf("%d%d",&N,&P);
		memset(cnt,0,sizeof cnt);
		for(int i=1;i<=N;i++){
			scanf("%d",a+i);
			a[i]%=P;
			if(a[i]==0) ans++;
			cnt[a[i]]++;
		}
		int pre=ans;
		for(maxd=2;;maxd++){
			while(dfs(0,0));
			if(ans==pre) break;
			pre=ans;
		}
		for(int i=1;i<P;i++)
			if(cnt[i]){
				ans++;
				break;
			}
		printf("Case #%d: %d\n",++kase,ans);
	}
	return 0;
}
/*
1
7 4
1 2 2 3 1 1 2
*/

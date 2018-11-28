#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char str[20];
int len;
ll ans;
void dfs(ll now,int idx,bool flag,char pre){
	if(idx>len){
		ans=max(ans,now);
	}else{
		if(flag){
			if(pre<=str[idx]){
				dfs(now*10LL+str[idx]-'0',idx+1,flag,str[idx]);
			}
			for(char ch=pre;ch<str[idx];ch++){
				dfs(now*10LL+ch-'0',idx+1,false,ch);
			}
		}else{
			for(int i=idx;i<=len;i++)
				now=now*10LL+9LL;
			dfs(now,len+1,false,'9');
		}
	}
}
int main(){
	int tcase,kase=0;
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%s",str+1);
		len=strlen(str+1);
		ans=0;
		dfs(0,1,true,'0');
		printf("Case #%d: %lld\n",++kase,ans);
	}
	return 0;
}

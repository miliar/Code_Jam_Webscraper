#include <cstdio>
#include <cstring>
using namespace std;
int T,len,ans,i,j,K,l,p,ca;char s[111];int a[111],b[111];
void dfs(int i,bool l,int w){
	if(i>len){
		if(w>ans){
			ans=w;memcpy(b,a,sizeof(a));
		}
		return;
	}
	if(l)a[i]=9,dfs(i+1,l,w+1);
	else{
		a[i]=s[i]-'0';if(a[i]>=a[i-1])dfs(i+1,l,w+(w>0||a[i]>0));
		if(s[i]>'0'){a[i]=s[i]-'0'-1;if(a[i]>=a[i-1])dfs(i+1,1,w+(w>0||a[i]>0));}
	}
}
int main(){
	int ca=0;
	for(scanf("%d",&T);T;T--){
		scanf("%s",s+1);len=strlen(s+1);
		ans=0;dfs(1,0,0);
		printf("Case #%d: ",++ca);
		int i=1;for(;b[i]==0;i++);
		for(int c=1;c<=ans;c++,i++)printf("%d",b[i]);printf("\n");
	}
}
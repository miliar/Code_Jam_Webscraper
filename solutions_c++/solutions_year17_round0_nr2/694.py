#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LF double
#define LL long long
#define ULL unsigned long long
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a>b)?a:b)
#define fo(i,j,k) for(int i=j;i<=k;i++)
#define fd(i,j,k) for(int i=j;i>=k;i--)
#define fr(i,j) for(int i=Begin[j];i;i=Next[i])
using namespace std;
int const ml=1000+9,Inf=1e9;
int t,n,a[ml];LL ans;
void dfs(int now,int tag,LL tmp,int pre){
	if(now>a[0]){
		ans=tmp;
		return;
	}
	int mx=9;if(!tag)mx=a[now];
	fd(i,mx,pre){
		dfs(now+1,tag||(i!=mx),tmp*10+i,i);
		if(ans!=-1)return;
	}
}
int main(){
	//freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	scanf("%d",&t);
	fo(cas,1,t){
		char ch=getchar();a[0]=0;
		while((ch<'0')||(ch>'9'))ch=getchar();
		while((ch>='0')&&(ch<='9'))a[++a[0]]=ch-'0',ch=getchar();
		ans=-1;dfs(1,0,0,0);
		printf("Case #%d: %lld\n",cas,ans);
	}
	return 0;
}

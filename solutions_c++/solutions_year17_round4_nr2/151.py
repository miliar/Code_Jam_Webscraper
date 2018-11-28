#include<bits/stdc++.h>
using namespace std;
int T,n,m,c,x,y,a[1010],b[1010],i,ans,ans1;
int main(){
	freopen("BB.in","r",stdin);
	freopen("BB.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		ans1=ans=0;
		scanf("%d%d%d",&n,&c,&m);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=1;i<=m;i++){
			scanf("%d%d",&x,&y);
			a[x]++;b[y]++;
			if(b[y]>ans)ans=b[y];
		}
		for(i=1;i<=n;i++){
			a[i]+=a[i-1];
			ans=max(ans,(a[i]+i-1)/i);
		}
		for(i=1;i<=n;i++)
			ans1+=max(0,a[i]-a[i-1]-ans);
		printf("Case #%d: ",_);
		printf("%d %d\n",ans,ans1);
	}
}

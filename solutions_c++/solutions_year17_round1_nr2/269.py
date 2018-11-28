#include<bits/stdc++.h> 
using namespace std;
int p[100010],cnt,S[110];
int T,ans,n,m,i,a[110],b[110][110],j,m1,m2,an,M,s,t,k,use[110][110],l[110][110],r[110][110];
int getmin(int x,int y){
	return (int)ceil(x/1.1/y);
}
int getmax(int x,int y){
	return (int)(x/0.9/y);
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		memset(use,0,sizeof(use));
		ans=M=cnt=0;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)scanf("%d",&a[i]);
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++)
				scanf("%d",&b[i][j]);
			sort(b[i]+1,b[i]+m+1);
			for(j=1;j<=m;j++)
				l[i][j]=getmin(b[i][j],a[i]),
				r[i][j]=getmax(b[i][j],a[i]),
				p[++cnt]=l[i][j];
		}
		sort(p+1,p+cnt+1);
		for(i=1;i<=cnt;i++){
			for(j=1;j<=n;j++){
				for(k=1;k<=m;k++)
					if(l[j][k]<=p[i]&&r[j][k]>=p[i]&&!use[j][k])break;
				if(k>m)break;
				S[j]=k;
			}
			if(j<=n)continue;
			ans++;
			for(j=1;j<=n;j++)use[j][S[j]]=1;
		}
		printf("Case #%d: %d\n",_,ans);
	}
}

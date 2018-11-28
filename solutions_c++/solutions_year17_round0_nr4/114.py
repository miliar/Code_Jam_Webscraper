#include <cstdio>
#include <cstring>
using namespace std;
int G1[205][205],G2[205][205];
int n;
int G[105][105],NG[105][105];
char st[105];
int Fa[205],Go[205];
bool dfs(int G[][205],int p,int n){
	for(int i = 1; i<=n;i++)
		if(G[p][i]&&!Go[i]){
			Go[i] = p;
			if(Fa[i]==0||dfs(G,Fa[i],n)){
				Fa[i] = p;
				return 1;
			}
		}
	return 0;
}
void Del1(int x,int y){
	for(int i=1;i<=n;i++)G1[x][i]=G1[i][y]=0;
}
void Del2(int x,int y){
	for(int i=0;i<=n+n;i++)G2[x-y+n][i]=G2[i][x+y]=0;
}
int main(){
	int T,tt=0,m,i,j,k,l,ans;
	scanf("%d",&T);
	while(T--){
		tt++;
		memset(G,0,sizeof(G));
		memset(NG,0,sizeof(NG));
		memset(G1,0,sizeof(G1));
		memset(G2,0,sizeof(G2));
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++){
				G1[i][j]=1;
				G2[i-j+n][i+j]=1;
			}
		for(i=1;i<=m;i++){
			int x,y;
			scanf("%s%d%d",st,&x,&y);
			if(st[0]=='+'){
				NG[x][y]=G[x][y]=1;
				Del2(x,y);
			}
			if(st[0]=='x'){
				NG[x][y]=G[x][y]=2;
				Del1(x,y);
			}
			if(st[0]=='o'){
				NG[x][y]=G[x][y]=3;
				Del1(x,y);
				Del2(x,y);
			}
		}
		for(i=1;i<=n;i++)Fa[i]=Go[i]=0;
		for(i=1;i<=n;i++){
			dfs(G1,i,n);
			memset(Go,0,sizeof(Go));
		}
		//printf("OK?%d\n",tt);
		for(i=1;i<=n;i++){
			if(Fa[i]!=0){
				NG[Fa[i]][i]|=2;
			}
		}
		for(i=1;i<=n+n;i++)Fa[i]=Go[i]=0;
		for(i=1;i<n+n;i++){
			dfs(G2,i,n+n);
			memset(Go,0,sizeof(Go));
		}
		//printf("OK?%d\n",tt);
		for(i=2;i<=n+n;i++){
			if(Fa[i]!=0){
		//		printf("%d %d\n",i,Fa[i]);
				NG[(Fa[i]+i-n)/2][(i-Fa[i]+n)/2]|=1;
			}
		}
		ans = 0;
		int cs = 0;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++){
				if(NG[i][j]==1||NG[i][j]==2)ans++;
				else if(NG[i][j]==3)ans+=2;
				if(NG[i][j]!=G[i][j])cs++;
			}
		printf("Case #%d: %d %d\n",tt,ans,cs);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(G[i][j]!=NG[i][j]){
					if(NG[i][j]==1)printf("+ ");
					if(NG[i][j]==2)printf("x ");
					if(NG[i][j]==3)printf("o ");
					printf("%d %d\n",i,j);
				}
	}
	return 0;
}

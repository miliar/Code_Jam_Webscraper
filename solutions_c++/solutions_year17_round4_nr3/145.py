#include<bits/stdc++.h>
using namespace std;
const int Tx[]={0,1,0,-1};
const int Ty[]={-1,0,1,0};
char s[60][60];
int q[100010],flag,t,B[10010],_;
int f[60][60],F[2][60][60],T,n,m,i,j,A[10010],v[20010],ne[20010],len[20010],cnt,head[10010],l,r;
void add(int x,int y,int z){
	v[++cnt]=y;ne[cnt]=head[x];head[x]=cnt;len[cnt]=z;
	v[++cnt]=x;ne[cnt]=head[y];head[y]=cnt;len[cnt]=z;
}
int find(int x,int y,int z){
	int X=x+Tx[z],Y=y+Ty[z];
	if(s[X][Y]=='.')return find(X,Y,z);
	if(s[X][Y]=='\\')return find(X,Y,3-z);
	if(s[X][Y]=='/')return find(X,Y,z^1);
	if(s[X][Y]=='#')return 1;
	if(s[X][Y]=='-')return 0;
}
void dfs(int x,int y,int z,int t){
	int X=x+Tx[z],Y=y+Ty[z];
	F[z&1][x][y]=t;
	if(s[X][Y]=='.')dfs(X,Y,z,t);
	if(s[X][Y]=='\\')dfs(X,Y,3-z,t);
	if(s[X][Y]=='/')dfs(X,Y,z^1,t);
	if(s[X][Y]=='#')return;
}
int bfs(){
	for(;l<=r;l++){
		for(int i=head[q[l]];i;i=ne[i]){
			int t=-1;
			if(len[i]==1)t=A[q[l]]^1;
			else if(A[q[l]]==0)t=1;
			if(t==-1)continue;
			if(A[v[i]]==-1)A[v[i]]=t,q[++r]=v[i];else
			if(A[v[i]]!=t)return 0;
		}
	}
	return 1;
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(_=1;_<=T;_++){
		cnt=0;
		memset(head,0,sizeof(head));
		memset(s,0,sizeof(s));
		memset(F,0,sizeof(F));
		memset(f,0,sizeof(f));
		memset(A,0,sizeof(A));
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			scanf("%s",s[i]+1);
			for(j=1;j<=m;j++)if(s[i][j]=='|')s[i][j]='-';
		}
		for(i=0;i<=n+1;i++)s[i][0]=s[i][m+1]='#';
		for(i=0;i<=m+1;i++)s[0][i]=s[n+1][i]='#';
		/*for(i=0;i<=n+1;i++)
			printf("%s\n",s[i]);*/
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)if(s[i][j]=='-'){
				f[i][j]=(i-1)*m+j;
				if(find(i,j,0)&&find(i,j,2))
					dfs(i,j,0,f[i][j]),dfs(i,j,2,f[i][j]);
				if(find(i,j,1)&&find(i,j,3))
					dfs(i,j,1,f[i][j]+n*m),dfs(i,j,3,f[i][j]+n*m);
				add(f[i][j],f[i][j]+n*m,1);
			}
		memset(A,-1,sizeof(A));
		/*for(i=1;i<=n;i++,puts(""))
			for(j=1;j<=m;j++)
				if(s[i][j]!='#')printf("%d,%d ",F[0][i][j],F[1][i][j]);*/
		printf("Case #%d: ",_);
		l=1;r=0;
		flag=1;
		for(i=1;i<=n&&flag;i++)
			for(j=1;j<=m&&flag;j++)if(s[i][j]!='#'){
				if(F[0][i][j]+F[1][i][j]==0)flag=0;
				if(F[0][i][j]==0)A[F[1][i][j]]=1,q[++r]=F[1][i][j];else
				if(F[1][i][j]==0)A[F[0][i][j]]=1,q[++r]=F[0][i][j];else
				add(F[0][i][j],F[1][i][j],0);
			}
		if(!flag){puts("IMPOSSIBLE");continue;} 
		if(!bfs()){puts("IMPOSSIBLE");continue;}
		for(i=1;i<=n&&flag;i++)
			for(j=1;j<=m&&flag;j++)
			if(s[i][j]!='#'&&A[f[i][j]]==-1){
				for(t=1;t<=n*m;t++)B[t]=A[t];
				A[f[i][j]]=1;
				q[l=r=1]=f[i][j];
				if(bfs())continue;
				for(t=1;t<=n*m;t++)A[t]=B[t];
				A[f[i][j]]=1;
				q[l=r=1]=f[i][j];
				if(!bfs())flag=0;
			}
		if(!flag){puts("IMPOSSIBLE");continue;}
		puts("POSSIBLE");
		for(i=1;i<=n;i++,puts(""))
			for(j=1;j<=m;j++){
				if(s[i][j]=='-')putchar(A[f[i][j]]==0?'|':'-');
				else putchar(s[i][j]);
			}
	}
}

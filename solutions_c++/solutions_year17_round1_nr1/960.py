#include <cstdio>
#include <cstring>
using namespace std;
int G[105][105];
int n,m;
int Check(int x,int y,int tx, int ty){
	int c=0;
	for(int i=x;i<=tx;i++)
		for(int j=y;j<=ty;j++)
			if(G[i][j]!=0){
				if(c!=0&&G[i][j]!=c)return 0;
				c=G[i][j];
			}
	return c;
}
int Check1(int x,int y,int tx, int ty){
	int c=0;
	for(int i=x;i<=tx;i++)
		for(int j=y;j<=ty;j++)
			if(G[i][j]!=0){
				c=G[i][j];
			}
	return c;
}
void Flood(int x,int y,int tx,int ty, int c){
	for(int i=x;i<=tx;i++)
		for(int j=y;j<=ty;j++)
			G[i][j]=c;
}
void Do(int x,int y,int rx,int ry){
	int i,j;
	j=Check(x,y,rx,ry);
	if(j){
		Flood(x,y,rx,ry,j);
		return ;
	}
	for(i=x;i<rx;i++){
		if(Check1(x,y,i,ry)&&Check1(i+1,y,rx,ry)){
			Do(x,y,i,ry);
			Do(i+1,y,rx,ry);
			return ;
		}
	}
	for(i=y;i<ry;i++){
		if(Check1(x,y,rx,i)&&Check1(x,i+1,rx,ry)){
			Do(x,y,rx,i);
			Do(x,i+1,rx,ry);
			return;
		}
	}
}

int main(){
	int T,i,j,k,l,tt=0;
	scanf("%d",&T);
	while(T--){
		tt++;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++){
				char ch =getchar();
				while(ch!='?'&&(ch<'A'||ch>'Z'))ch=getchar();
				if(ch=='?')G[i][j]=0;
				else G[i][j]=ch-'A'+1;
			}
		Do(1,1,n,m);
		printf("Case #%d:\n",tt);
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++)putchar(G[i][j]+'A'-1);
			putchar('\n');
		}		
	}
	return 0;
}

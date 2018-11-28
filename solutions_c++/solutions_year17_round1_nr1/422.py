#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int Maxn=25;

int R,C;
int cake[Maxn+5][Maxn+5];
bool vis[Maxn+5][Maxn+5];
int cnt[Maxn+5][Maxn+5];
int rec[Maxn+5][Maxn+5][4];

inline int read(){
	char x=getchar();
	while(!(x=='?' || ('A'<=x && x<='Z'))) x=getchar();
	if (x=='?') return 0;
	return (x-'A'+1);
}

int sum[Maxn+5][Maxn+5];
inline int lowbit(int x){
	return x&-x;
}

inline void add(int x,int y,int val){
	for (int i=x;i<=Maxn;i+=lowbit(i))
		for (int j=y;j<=Maxn;j+=lowbit(j))
			sum[i][j]+=val;
}

inline int get(int x,int y){
	int ret=0;
	for (int i=x;i;i-=lowbit(i))
		for (int j=y;j;j-=lowbit(j))
			ret+=sum[i][j];
	return ret;
}

inline int get(int x0,int y0,int x1,int y1){
	return get(x1,y1)+get(x0-1,y0-1)-get(x1,y0-1)-get(x0-1,y1);
}

void solve(int T){
	//Init
	memset(sum,0,sizeof(sum));
	memset(vis,false,sizeof(vis));
	//Input
	scanf("%d%d",&R,&C);
	for (int i=1;i<=R;i++) for (int j=1;j<=C;j++) cake[i][j]=read();
	for (int i=1;i<=R;i++) for (int j=1;j<=C;j++) add(i,j,cake[i][j]);	

	//Solve
	while(true){
		memset(cnt,0,sizeof(cnt));
		int tmpMax=0,tmpX,tmpY;
		for (int i=1;i<=R;i++)
		for (int j=1;j<=C;j++)
		if (!vis[i][j] && cake[i][j]){
			for (int rm=0;1<=i-rm;rm++)
			for (int rp=0;i+rp<=R;rp++)
			for (int cm=0;1<=j-cm;cm++)
			for (int cp=0;j+cp<=C;cp++){
				if (get(i-rm,j-cm,i+rp,j+cp)==cake[i][j]){
					cnt[i][j]=max(cnt[i][j],(rp+rm+1)*(cp+cm+1));
					if (cnt[i][j]==(rp+rm+1)*(cp+cm+1)){
						rec[i][j][0]=i-rm;
						rec[i][j][1]=j-cm;
						rec[i][j][2]=i+rp;
						rec[i][j][3]=j+cp;
					}
				}
			}
			if (cnt[i][j]>tmpMax){
				tmpMax=cnt[i][j];
				tmpX=i;
				tmpY=j;
			}
		}

		if (tmpMax<=1) break;
		for (int i=rec[tmpX][tmpY][0];i<=rec[tmpX][tmpY][2];i++)
			for (int j=rec[tmpX][tmpY][1];j<=rec[tmpX][tmpY][3];j++){
				if (cake[i][j]==0){
					cake[i][j]=cake[tmpX][tmpY];
					vis[i][j]=true;
					add(i,j,cake[i][j]);
				}else vis[i][j]=true;
			}
	}

	//Print
	printf("Case #%d:\n",T);
	for (int i=1;i<=R;i++){
		for (int j=1;j<=C;j++){
			printf("%c",(char)(cake[i][j]+'A'-1));
		}
		printf("\n");
	}
}

int main(){
	freopen("A-small-attempt0.in-2.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T=0;
	scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}
#include<cstdio>
#include<algorithm>
#include<cstring>
#define ll long long
using namespace std;
const int maxn=2e3;
int pp,wzd[4][10],ans[maxn];bool bz;
int N,R,O,Y,G,B,V,b,r,y,i,j,cnt,tot;
char ch;ll ww,p;
inline ll read(){
	ww=0,p=1;
	for(ch=getchar();(ch<'0'||ch>'9')&&ch!='-';ch=getchar());
	if (ch=='-') ch=getchar(),p=-1;
	for(;ch>='0'&&ch<='9';ch=getchar()) ww=ww*10+ch-48;
	return ww*p;
}
void make(){
	wzd[1][1]=R,wzd[1][2]=r,wzd[1][3]='R',wzd[1][4]='G';
	wzd[2][1]=B,wzd[2][2]=b,wzd[2][3]='B',wzd[2][4]='O';
	wzd[3][1]=Y,wzd[3][2]=y,wzd[3][3]='Y',wzd[3][4]='V';
}
void work(){
	for(int i=1;i<=cnt;i++){
		printf("%c",ans[i]);
		for(int j=1;j<=3;j++)if (ans[i]==wzd[j][3]){
			for(;wzd[j][2];){
				wzd[j][2]--;
				printf("%c%c",wzd[j][4],wzd[j][3]);
			}
		}
	}
}
void fa(){
	for(int i=1;wzd[1][1];i+=2,wzd[1][1]--) ans[i]=wzd[1][3];
	bz=0;
	for(int i=cnt;i>=cnt;i--)if (ans[i]==0){
		if (ans[i+1]!=wzd[2][3]&&wzd[2][1]){
			ans[i]=wzd[2][3];
			wzd[2][1]--;
		}else
		if (ans[i+1]!=wzd[3][3]&&wzd[3][1]){
			ans[i]=wzd[3][3];
			wzd[3][1]--;
		}else{bz=1;return;}
	}
}
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t=read();
	for(pp=1;pp<=t;pp++){
		N=read(),R=read(),O=read(),Y=read(),G=read(),B=read(),V=read();
		printf("Case #%d: ",pp);
		b=O,r=G,y=V;
		make();
		for(i=1;i<=3;i++)for(j=i+1;j<=3;j++)
		if (wzd[i][1]<wzd[j][1]) swap(wzd[i],wzd[j]);
		if (wzd[1][1]+wzd[1][2]==N){
		if (N%2==0&&wzd[1][1]==wzd[1][2]){
			for(int i=1;i<=N/2;i++) printf("%c%c",wzd[1][3],wzd[1][4]);
			printf("\n");
			continue;
		}
		printf("IMPOSSIBLE\n");
		continue;
		}
		bool re=0;
		for(int i=1;i<=3;i++)if (wzd[i][1]&&wzd[i][1]<=wzd[i][2]){
			printf("IMPOSSIBLE\n");re=1;
			break;		
		}else wzd[i][1]-=wzd[i][2];
		if (re) continue;
		tot=0,cnt=0;
		for(int i=1;i<=3;i++)for(int j=i+1;j<=3;j++)
		if (wzd[i][1]<wzd[j][1]) swap(wzd[i],wzd[j]);
		for(int i=1;i<=3;i++) cnt+=wzd[i][1];
		if (wzd[1][1]>cnt/2){printf("IMPOSSIBLE\n");continue;}
		for(int i=0;i<=maxn-1;i++) ans[i]=0;
		fa();
		if (bz){printf("IMPOSSIBLE\n");continue;}
		work();
		printf("\n");
	}
}














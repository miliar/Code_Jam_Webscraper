#include <cstring>
#include <cstdio>
#include <algorithm>
#define ll long long
#define fo(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=1e2+5;
ll d[maxn][maxn];
ll n,q,e[maxn],s[maxn],pp;
double f[maxn][maxn];
char ch;ll ww,p;
inline ll read(){
	ww=0,p=1;
	for(ch=getchar();(ch<'0'||ch>'9')&&ch!='-';ch=getchar());
	if (ch=='-') ch=getchar(),p=-1;
	for(;ch>='0'&&ch<='9';ch=getchar()) ww=ww*10+ch-48;
	return ww*p;
}
int main() {
	//freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);
	int t,i,j,k;
	t=read();
	fo(pp,1,t){
	printf("Case #%d:",pp);
	n=read(),q=read();
	fo(i,1,n) e[i]=read(),s[i]=read();
	fo(i,1,n) fo(j,1,n) d[i][j]=read();
	fo(k,1,n)
	fo(i,1,n)if (d[i][k]!=-1)
	fo(j,1,n)if (d[k][j]!=-1&&i!=j) {
		if ((d[i][j]==-1)||(d[i][j]>d[i][k]+d[k][j])) d[i][j]=d[i][k]+d[k][j];
	}
	fo(i,1,n) 
	fo(j,1,n)
	if (d[i][j]!=-1&&d[i][j]<=e[i]) f[i][j]=(double)d[i][j]/s[i];else f[i][j]=-1;
	fo(k,1,n)
	fo(i,1,n)
	if (f[i][k]!=-1)
	fo(j,1,n) if (f[k][j]!=-1&&i!=j) {
		if ((f[i][j]==-1)||(f[i][j]>f[i][k]+f[k][j])) f[i][j]=f[i][k]+f[k][j];
	}
	fo(i,1,q) {
		int x=read(),y=read();
		printf(" %.9lf",f[x][y]);
	}
	putchar('\n');
	}
}

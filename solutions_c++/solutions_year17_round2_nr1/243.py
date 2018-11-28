#include<cstring>
#include<cstdio>
#include<algorithm>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define ll long long
#define min(a,b) (a<b?a:b)
using namespace std;
char ch;int ww,p;
inline int read(){
	ww=0,p=1;
	for(ch=getchar();ch<'0'||ch>'9'&&ch!='-';ch=getchar());
	if (ch=='-') ch=getchar(),p=-1;
	for(;ch>='0'&&ch<='9';ch=getchar()) ww=ww*10+ch-48;
	return ww*p;
}
const int maxn=1000+5;
int i,j,k,s,w;double v;
int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int t=read();
	fo(j,1,t){
		int d=read(),n=read();
		v=1e18;
		fo(i,1,n) {
			w=read(),s=read();
			v=min(v,(double)s*d/(d-w));
		}
		printf("Case #%d: %lf\n",j,v);
	}
}

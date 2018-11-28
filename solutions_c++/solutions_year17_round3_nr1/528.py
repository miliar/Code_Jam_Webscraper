#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
#include<cstring>
#include<iostream>
#include<algorithm>
#define rep(i,a,b) for (int i=a; i<=b; i++)
#define per(i,a,b) for (int i=a; i>=b; i--)
#define debug(x) {cout<<(#x)<<" "<<x<<endl;}
using namespace std;
typedef long long LL;

inline int read() {
    int x=0,f=1; char ch=getchar();
    while (!(ch>='0'&&ch<='9')) {if (ch=='-')f=-1;ch=getchar();}
    while (ch>='0'&&ch<='9') {x=x*10+(ch-'0'); ch=getchar();}
    return x*f;
}

const int N = 1005;
const double Pi = 3.14159265358979;

int k,n;
struct cake{
	double r,h;
} c[N];
bool cmp(cake a,cake b) {
	if (a.r==b.r) return a.h>b.h;
	return a.r>b.r;
}
double dp[N][N];
double aux[N];

int main() {

	#ifndef ONLINE_JUDGE
		freopen("A-large (2).in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(cas,1,T) {
		n=read(),k=read(); 
		rep(i,1,n) c[i].r=read(),c[i].h=read();
		sort(c+1,c+n+1,cmp);
		rep(i,1,n) rep(j,1,k) dp[i][j]=0;
		rep(i,1,k) aux[i]=0;
		rep(i,1,n) {
			dp[i][1]=Pi*c[i].r*c[i].r+2*Pi*c[i].r*c[i].h;
			rep(j,2,k) dp[i][j]=aux[j-1]+2*Pi*c[i].r*c[i].h;
			rep(j,1,k) aux[j]=max(aux[j],dp[i][j]);
		}
		printf("Case #%d: %lf\n",cas,aux[k]);
	}

	return 0;
}


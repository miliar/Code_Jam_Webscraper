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

const int N = 51;
const double eps = 1e-10;
int n,k;
double U,P[N];

double calc(double q) {
	double ret=0;
	rep(i,1,n) {
		if (P[i]<q) ret+=q-P[i];
	}
	return ret;
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("C-small-1-attempt0 (1).in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(cas,1,T) {
		n=read(),k=read(); scanf("%lf",&U); rep(i,1,n) scanf("%lf",&P[i]);
		double l=0,r=1,best;
		while (r-l>eps) {
			double mid=(l+r)/2;
			if (calc(mid)<=U) l=best=mid;
			else r=mid;
		}
		double ans=1;
		rep(i,1,n) if (P[i]<best) ans*=best; else ans*=P[i];
		printf("Case #%d: %lf\n",cas,ans);
	}

	return 0;
}


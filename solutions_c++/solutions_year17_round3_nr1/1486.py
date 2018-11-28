#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)
typedef long long ll;

const int maxn=1200;
struct arr {
	ll r,h;
}a[maxn],b[maxn];
int choose[maxn];
int n,k;
double ans,tmp;

void work(int lim,int eid) {
	int m=0;
	rep(i,1,n)
		if (a[i].r<=lim && i!=eid)
			b[++m]=a[i];
	//if (m<k-1) return;
	sort(b+1,b+m+1,[](arr a,arr b){return a.r*a.h>b.r*b.h;});
	b[0]=a[eid];
	tmp=M_PI*b[0].r*b[0].r;
	rep(i,0,min(k-1,m))
		tmp+=2*M_PI*b[i].r*b[i].h;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d%d\n",&n,&k);
		rep(i,1,n) {
			int x,y;
			scanf("%d%d\n",&x,&y);
			a[i]=(arr){x,y};
		}
		//sort(a+1,a+n+1,[](arr a,arr b){return a.r*a.h>b.r*b.h;});
		ans=0;
		rep(i,1,n) {
			choose[i]=true;
			work(a[i].r,i);
			if (ans<tmp)
				ans=tmp;
		}
		printf("%.8f\n",ans);
	}
	return 0;
}

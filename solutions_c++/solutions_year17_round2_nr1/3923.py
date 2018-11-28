#ifdef unix
#define RE "%lld"
#else
#define RE "%I64d"
#endif
#define rep(i,a,b) for (int i=(a);i<=(b);++i)
#define dep(i,a,b) for (int i=(b);i>=(a);--i)
#include<bits/stdc++.h>
using namespace std;
typedef double dd;
dd d;
int n;
struct node {
		dd k, s;
		void read() { scanf("%lf%lf", &k, &s); }
}a[1005];
bool cmp(const node &a, const node &b) { return a.k < b.k; }
dd work() {
		scanf("%lf%d", &d, &n);
		rep(i,1,n) a[i].read();
		sort(a+1,a+1+n,cmp);
		a[n+1].k = d, a[n+1].s = 0;
	//	rep(i,1,n) printf("%lf %lf\n", a[i].k, a[i].s);
		dd sumt = 0;
		rep(j,1,n) {
			int x;
			dd mint = -1, nowt;
			rep(i,1,n) {
				if (a[i].s > a[i+1].s + 0.1) { //**
					nowt = (a[i+1].k - a[i].k) / (a[i].s - a[i+1].s);
					if (mint < 0 || nowt < mint) mint = nowt, x = i;
				}
			}
	//		printf("%d %lf\n", x, mint);
			sumt += mint;
			rep(i,1,n) 
					a[i].k += a[i].s * mint;
			a[x].s = a[x+1].s;
		}
		return d / sumt;
}
int main() {
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		int T;
		scanf("%d", &T);
		rep(i,1,T)
				printf("Case #%d: %.12f\n", i, work());
		return 0;
}


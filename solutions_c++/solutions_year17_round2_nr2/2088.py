#ifdef unix
#define RE "%lld"
#else
#define RE "%I64d"
#endif
#define rep(i,a,b) for (int i=(a);i<=(b);++i)
#define dep(i,a,b) for (int i=(b);i>=(a);--i)
#include<bits/stdc++.h>
using namespace std;
int n;
struct node {
		int c, x;
		void read(int cc) { c = cc; scanf("%d", &x); }

}a[10];
bool cmp(const node &a, const node&b) { return a.x > b.x; }
int ans[5005];
char pt(int c) {
			if (c == 0) return 'R';
			if (c == 2) return 'Y';
			if (c == 4) return 'B';
}
void work() {
		scanf("%d", &n);
		rep(i,0,5) a[i].read(i);
		sort(a,a+6,cmp);
		if (a[1].x + a[2].x < a[0].x) {
			printf("IMPOSSIBLE\n");
			return;
		}
		memset(ans, -1, sizeof ans);
//		printf("%d %d %d\n", a[0].c, a[1].c, a[2].c);
		rep(i,0,a[0].x-1) 
				ans[i*3] = a[0].c;
		rep(i,0,a[1].x-1) 
				ans[i*3+1] = a[1].c;
		rep(i,a[1].x,a[0].x-1)
				ans[i*3+1] = a[2].c;
		rep(i,0,(a[2].x-(a[0].x-a[1].x))-1)
				ans[i*3+2] = a[2].c;
		rep(i,0,a[0].x*3) 
				if (ans[i] != -1) putchar(pt(ans[i]));
		printf("\n");
}
int main() {
		freopen("b.in", "r", stdin);
		freopen("b.out", "w", stdout);
		int T;
		scanf("%d", &T);
		rep(i,1,T)  {
				printf("Case #%d: ", i);
				work();
		}
		return 0;
}


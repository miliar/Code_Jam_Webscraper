#define PROC "a"
#ifdef unix
#define RE "%lld"
#else
#define RE "%I64d"
#endif
#define rep(i,a,b) for (int i=(a);i<=(b);++i)
#define dep(i,a,b) for (int i=(b);i>=(a);--i)
#include<bits/stdc++.h>
using namespace std;
char s[1005];
void work() {
		scanf("%s", s + 1);
		int n = (int)strlen(s+1), k;
		scanf("%d", &k);
		int ans = 0;
		rep(i,1,n-k+1)
				if (s[i]=='-') {
					rep(j,i,i+k-1)
							s[j] = s[j]=='+'?'-':'+';
					ans ++;
				}
		//printf("ans %d\n", ans);
		bool f = 0;
		rep(i,n-k+2,n)
				if (s[i]=='-') f = 1;
		if (f) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
}
int main() {
		freopen(PROC"_large.in", "r", stdin);
		freopen(PROC".out", "w", stdout);
		int T;
		scanf("%d", &T);
		rep(i,1,T) {
				printf("Case #%d: ", i);
				work();
		}
		return 0;
}


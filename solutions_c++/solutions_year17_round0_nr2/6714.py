#define PROC "b"
#ifdef unix
#define RE "%lld"
#else
#define RE "%I64d"
#endif
#define rep(i,a,b) for (int i=(a);i<=(b);++i)
#define dep(i,b,a) for (int i=(b);i>=(a);--i)
#include<bits/stdc++.h>
using namespace std;
bool judge(int x) {
		int la = 10;
		while (x) {
				int cur = x % 10;
				x /= 10;
				if (la < cur) return 0;
				la = cur;
		}
		return 1;
}
int num[20], n;
int main() {
		freopen(PROC"_large.in", "r", stdin);
		freopen(PROC".out", "w", stdout);
		int T;
		scanf("%d", &T);
		rep(i,1,T) { 
				printf("Case #%d: ", i);
				long long x, xx;
				scanf(RE, &x);
				xx = x;
				n = 0;
				memset(num, 0, sizeof num);
				while (x) num[++ n] = x % 10, x /= 10;
				int f = -1;
				dep(j,n,2) 
					if (num[j] > num[j-1]) {
							f = j; break;
					}
				if (f == -1) cout<<xx<<endl;
				else {
					int t = f;
					while (t + 1 <= n && num[t+1]==num[t])
							++ t;
					num[t] --;
					dep(j,t-1,1) num[j] = 9;
					while (n && num[n] == 0) -- n;
					dep(j,n,1) printf("%d",num[j]);
					printf("\n");
				}
		}
		return 0;
}


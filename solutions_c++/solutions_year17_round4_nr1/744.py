#include <bits/stdc++.h>
using namespace std;
int n = 0,p = 0;
int g[200];
int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		scanf("%d%d",&n,&p);
		if(p == 2) {
			int cnt1 = 0,cnt2 = 0,x;
			for(int i = 1;i <= n;++ i) {
				scanf("%d",&x);
				if(!(x&1)) cnt2 ++;
				else cnt1 ++;
			}
			int ans = cnt2 + (cnt1+1)/2;
			printf("Case #%d: %d\n",t,ans);
		}
		if(p == 3) {
			int cnt0 = 0,cnt1 = 0,cnt2 = 0,x;
			for(int i = 1;i <= n;++ i) {
				scanf("%d",&x); x %= 3;
				if(x == 0) cnt0 ++;
				if(x == 1) cnt1 ++;
				if(x == 2) cnt2 ++;
			}
			int ans = cnt0;
			if(cnt1 >= cnt2) {
				ans += cnt2; cnt1 -= cnt2; 
				ans += (cnt1+2)/3;
			} else {
				ans += cnt1; cnt2 -= cnt1;
				ans += (cnt2+2)/3;
			}
			printf("Case #%d: %d\n",t,ans);
		}
	} 
	return 0;
} 

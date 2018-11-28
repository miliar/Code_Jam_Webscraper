#include <bits/stdc++.h>
using namespace std;
int N, C, M;
int cnt[1010], sum[1010];
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T = 0; scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		memset(cnt,0,sizeof(cnt));
		memset(sum,0,sizeof(sum));
		scanf("%d%d%d",&N,&C,&M);
		int p, b;
		for(int i = 1;i <= M;++ i) {
			scanf("%d%d",&p,&b);
			cnt[b] ++; sum[p] ++;
		}
		for(int i = 1;i <= N;++ i) sum[i] += sum[i-1];
		int ans1 = 0, ans2 = 0;
		for(int i = 1;i <= C;++ i) ans1 = max(ans1,cnt[i]);
		for(int i = 1;i <= N;++ i) ans1 = max(ans1,(sum[i]+i-1)/i);
		for(int i = 1;i <= N;++ i) ans2 += max(0,sum[i]-sum[i-1]-ans1);
		printf("Case #%d: %d %d\n",t,ans1,ans2);
	} 
	return 0;
} 

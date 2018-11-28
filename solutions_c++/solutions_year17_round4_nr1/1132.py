#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int testcase, kase = 0, cnt[7], t, ans, n, p, i;
	scanf("%d", &testcase);
	while(testcase --){
		memset(cnt, 0, sizeof(cnt));
		scanf("%d%d", &n, &p);
		for(i = 1; i <= n; ++ i){
			scanf("%d", &t);
			++ cnt[t % p];
		}
		printf("Case #%d: ", ++ kase);
		if(p == 2) printf("%d\n", cnt[0] + ((cnt[1] + 1) >> 1));
		else if(p == 3){
			if(cnt[1] > cnt[2]) swap(cnt[1], cnt[2]);
			printf("%d\n", cnt[0] + min(cnt[1], cnt[2]) + (max(cnt[1], cnt[2]) - min(cnt[1], cnt[1]) + 2) / 3);
		}else{
			t = min(cnt[1], cnt[3]);
			ans = cnt[0] + t + (cnt[2] >> 1);
			cnt[1] -= t, cnt[3] -= t, cnt[2] &= 1;
			if(t = max(cnt[1], cnt[3])){
				if(cnt[2] && t >= 2)
					ans += 1 + (t + 1) / 4;
				else ans += (t + 3) / 4;
			}else if(cnt[2]) ++ ans;
			printf("%d\n", ans);
		}
	} return 0;
}

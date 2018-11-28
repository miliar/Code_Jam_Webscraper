#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int cnt[5];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc){
		memset(cnt, 0, sizeof(cnt));
		int n, p;
		scanf("%d%d", &n, &p);
		for(int i = 0; i < n; ++i){
			int x;
			scanf("%d", &x);
			cnt[x % p]++;
		}
		int ans = 0;
		if(p == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}
		else if(p == 3) {
			ans = cnt[0] + min(cnt[1], cnt[2]);
			int x = max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]);
			ans += (x + 2) / 3;
		}
		else if(p == 4) {
			ans = cnt[0];
			int x = min(cnt[1], cnt[3]);
			ans += x;
			cnt[1] -= x;
			cnt[3] -= x;
			
			x = min(cnt[2], cnt[1] / 2);
			ans += x;
			cnt[2] -= x;
			cnt[1] -= 2 * x;

			x = min(cnt[2], cnt[3] / 2);
			ans += x;
			cnt[2] -= x;
			cnt[3] -= 2 * x;

			x = cnt[2] / 2;
			ans += x;
			cnt[2] -= 2 * x;

			x = cnt[1] / 4;
			ans += x;
			cnt[1] -= 4 * x;

			x = cnt[3] / 4;
			ans += x;
			cnt[3] -= 4 * x;
			assert(cnt[1] >= 0);
			assert(cnt[2] >= 0);
			assert(cnt[3] >= 0);
			if(cnt[1] || cnt[2] || cnt[3]) ans++;
		}
		printf("Case #%d: %d\r\n", cc, ans);
	}
	return 0;
}


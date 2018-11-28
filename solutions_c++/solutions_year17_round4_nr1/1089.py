#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
#define eprintf(...) fprintf(stderr,__VA_ARGS__)

int ans, p, cnt[4];

int main(){
	int T; scanf("%d", &T);
	for (int Case=1;Case<=T;Case++) {
		memset(cnt, 0, sizeof(cnt));
		int n; scanf("%d%d", &n, &p);
		int tot = 0;
		while(n--){
			int g; scanf("%d", &g);
			cnt[g%p]++;
			tot += g;
		}
		ans = 0;
		if(p==2){
			ans = cnt[1] / 2;
		}
		else
		if(p==3){
			for (int k = 0; k <= min(cnt[1], cnt[2]); k++)
				ans = max(ans, k + (cnt[1] - k) / 3 + (cnt[2] - k) / 3);
		}
		else
		if(p==4){
			for (int i = 0; i * 2 <= cnt[3]; i++)
				for(int j = 0; j * 2 <= cnt[1]; j++)
					for (int k = 0; k <= min(cnt[3] - i * 2, cnt[1] - j * 2); k++)
						ans = max(ans, (cnt[2] + i + j) / 2 + k + (cnt[3] - i * 2 - k) / 4 + (cnt[1] - j * 2 - k) / 4);
		}
		ans += cnt[0];
		if (tot % p != 0) ans++;
		printf("Case #%d: %d\n", Case, ans);
	}
}

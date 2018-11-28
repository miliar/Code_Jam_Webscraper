#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, n, p, a[5];
	scanf("%d", &T);
	for (int tt = 1; tt <= T;tt++){
		memset(a, 0, sizeof(a));
		printf("Case #%d: ", tt);
		scanf("%d%d", &n, &p);
		int ans = 0;
		for (int i = 1;i <= n;i++){
			int x;
			scanf("%d", &x);
			a[x % p]++;
		}
		ans += a[0];
		if (p == 2){
			ans += (a[1]+1) / 2;
		}else if (p == 3){
			int cur = min(a[1], a[2]);
			ans += cur;
			a[1] -= cur;
			a[2] -= cur;
			if (a[1]){
				ans += (a[1] + 2) / 3;
			}else{
				ans += (a[2] + 2) / 3;
			}
		}else if (p == 4){
			// 2 depart
			ans += a[2] / 2;
			a[2] %= 2;

			int cur = min(a[1], a[3]);
			ans += cur;
			a[1] -= cur;
			a[3] -= cur;

			int t = max(a[1], a[3]);
			if (t >= 2 && a[2] == 1){
				ans++;
				t -= 2;
			}
			ans += (t + 3) / 4;
		}
		printf("%d\n", ans);
	}
}
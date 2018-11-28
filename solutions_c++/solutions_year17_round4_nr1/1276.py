#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 101, P = 5;

int cnt[P];
//int a[MAXN];
int n, p;
double ans;

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		memset(cnt, 0, sizeof(cnt));
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; i ++){
			int a; scanf("%d", &a);
			cnt[a % p] ++;
		}
		int ans = cnt[0];
		if (p == 2){
			ans += (cnt[1] + 1) / 2;
		} else if (p == 3){
			int c1 = cnt[1];
			int c2 = cnt[2];
			if (c1 > c2){
				int t = c1; c1 = c2; c2 = t;
			}
			ans += c1;
			ans += (c2 - c1 + 2) / 3;
		} else {//P = 4
			ans += (cnt[2] + 1) / 2;
			int c1 = cnt[1], c3 = cnt[3];
			if (c1 > c3){
				int t = c1; c1 = c3; c3 = t;
			}
			ans += c1;
			c3 -= c1;
			if (cnt[2] & 1)
				c3 -= 2;
			if (c3 >= 0)
				ans += (c3 + 3) / 4;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

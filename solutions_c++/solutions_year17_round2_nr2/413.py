#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1000;
int T, n;
struct ARR {
	int cnt, pos;
}a[10];
int ans[MaxN + 5];

char Get(int x)
{
	if (x == 1) return 'R';
	if (x == 2) return 'O';
	if (x == 3) return 'Y';
	if (x == 4) return 'G';
	if (x == 5) return 'B';
	if (x == 6) return 'V';
}

bool cmp(ARR A, ARR B) {
	return A.cnt > B.cnt;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d", &n);
		for (int i = 1; i <= 6; i++) {
			scanf("%d", &a[i].cnt);
			a[i].pos = i;
		}
		sort(a + 1, a + 7, cmp);
		memset(ans, 0, sizeof(ans));
		if (a[2].cnt + a[3].cnt < a[1].cnt) printf("Case #%d: IMPOSSIBLE\n", cas);
		else {
			int tot = 0;
			int t = a[2].cnt + a[3].cnt - a[1].cnt;
			for (int i = 1; i <= t; i++) {
				ans[++tot] = a[1].pos; a[1].cnt--;
				ans[++tot] = a[2].pos; a[2].cnt--;
				ans[++tot] = a[3].pos; a[3].cnt--;
			}
			for (int i = 1; i <= a[2].cnt; i++) {
				ans[++tot] = a[1].pos;
				ans[++tot] = a[2].pos;
			}
			for (int i = 1; i <= a[3].cnt; i++) {
				ans[++tot] = a[1].pos; 
				ans[++tot] = a[3].pos; 
			}
			printf("Case #%d: ", cas);
			for (int i = 1; i <= tot; i++) printf("%c", Get(ans[i]));
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 1003;

char st[MAXN];
int n, K, ans;

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%s", st);
		n = strlen(st);
		scanf("%d", &K);
		
		ans = 0;
		for (int i = 0; i < n && ans != -1; i ++)
			if (st[i] == '-'){
				if (i+K-1 >= n) ans = -1;
					else {
						ans ++;
						for (int j = 0; j < K; j ++)
							if (st[i+j] == '-') st[i+j] = '+';
								else st[i+j] = '-';
					}
			}
		
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

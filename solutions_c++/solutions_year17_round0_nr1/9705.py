#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int maxn = 1 << 10;
const int INF = 0x3f3f3f3f;
char a[maxn];
int k;
inline void get(int &x)
{
	char ch = getchar();
	int f = 1;
	while (ch < '0' || ch > '9')
	{
		f = ch == '-' ? -1 : 1;
		ch = getchar();
	}
	x = ch - '0';
	while (ch = getchar(), ch >= '0' && ch <= '9') x = 10 * x + ch - '0';
	x *= f;
}
void run()
{
	int l = 0, ans = 0;
	while (a[l] = getchar(), a[l] == '+' || a[l] == '-') l++;
	scanf("%d", &k);
	for (int i = 0; i < l; i++)
	{
		if (a[i] == '+') continue;
		int j = 0;
		for (; j < k && i + j < l; j++) a[i + j] = '+' + '-' - a[i +j];
		if (j < k)
		{
			puts("IMPOSSIBLE");
			return ;
		}
		ans ++;
	}
	printf("%d\n", ans);
}
int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++)
	{
		getchar();
		printf ("Case #%d: ", cas);
		run();
	}
	return 0;
}


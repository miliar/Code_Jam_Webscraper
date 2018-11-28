#include <cstdio>
#include <cstring>
const int maxn = 1005;
int n, c, m, p[maxn], b[maxn], psum[maxn], bsum[maxn], maxp, maxb, psumsum[maxn];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d%d%d", &n, &c, &m);
		//printf("%d %d %d\n", n, c, m);
		memset(bsum, 0, sizeof(bsum));
		memset(psum, 0, sizeof(psum));
		for (int i = 1; i <= m; i++)
		{
			scanf("%d%d", &p[i], &b[i]);
			psum[p[i]]++;
			bsum[b[i]]++;
		}
		maxp = psum[1];
		for (int i = 2; i <= n; i++)
		{
			if (maxp < psum[i])
				maxp = psum[i];
		}
		maxb = bsum[1];
		for (int i = 2; i <= c; i++)
		{
			if (maxb < bsum[i])
				maxb = bsum[i];
		}
		if (maxb >= maxp)
		{
			printf("%d 0\n", maxb);
			continue;
		}
		psumsum[0] = 0;
		int pos = 0;
		for (int i = 1; i <= n; i++)
		{
			psumsum[i] = psum[i] + psumsum[i - 1];
			if (pos == 0 || psumsum[i] * pos > psumsum[pos] * i)
				pos = i;
		}
		int ans1, ans2 = 0;
		//printf("%d\n", pos);
		if (psumsum[pos] % pos == 0)
			ans1 = psumsum[pos] / pos;
		else
			ans1 = (psumsum[pos] / pos) + 1;
		if (ans1 < maxb)
			ans1 = maxb;
		for (int i = 1; i <= n; i++)
			if (psum[i] > ans1)
				ans2 += psum[i] - ans1;
		printf("%d %d\n", ans1, ans2);
	}
	return 0;
}

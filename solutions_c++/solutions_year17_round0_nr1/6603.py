#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
const int INF = 987654321;
int T, len, ans, N;
char in[1004];
bool b[1004];
void func(int id, int cnt)
{
	if (id == len + 1) 
	{
		ans = min(cnt, ans);
		return;
	}
	if (b[id])
	{
		func(id + 1, cnt);
	}
	else
	{
		if (id + N <= len + 1)
		{
			for (int i = 0; i < N; ++i)
				b[id + i] = !b[id + i];
			func(id + 1, cnt + 1);
			for (int i = 0; i < N; ++i)
				b[id + i] = !b[id + i];
		}
	}
}
int main()
{
	//freopen("A-large.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		scanf("%s", &in);
		scanf("%d", &N);
		len = 0;
		ans = INF;
		for (int i = 0; in[i]; ++i)
		{
			if (in[i] == '+') b[i + 1] = true;
			else b[i + 1] = false;
			len++;
		}
		ans = INF;
		func(1, 0);
		printf("Case #%d: ", tc);
		if (ans == INF)	printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
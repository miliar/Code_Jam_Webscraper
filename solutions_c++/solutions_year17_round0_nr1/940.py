#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MaxN = 1007;

int T, N, M, cnt, sum;
char str[MaxN];
bool chg[MaxN];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);
	for (int id = 1; id <= T; id++)
	{
		scanf("%s", str+1); N = strlen(str+1);
		scanf("%d", &M);
		for (int i=1; i<=N; i++) chg[i] = false;
		cnt = sum = 0;
		int i, j;
		for (i=1; i<=N; i++)
		{
			j = (str[i] == '-');
			j ^= (cnt & 1);
			//cout << j << ' ' ;
			if (j == 1)
			{
				if (i + M - 1 > N) break;
				chg[i] = true;
				cnt ++; sum ++;
			}
			if (i >= M)
			{
				cnt -= chg[i-M+1];
			}
		}
		printf("Case #%d: ", id);
		if (i <= N) printf("IMPOSSIBLE\n");
		else printf("%d\n", sum);
	}
	return 0;
}
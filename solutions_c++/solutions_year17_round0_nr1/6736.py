#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

int solve();

int main()
{
//	FILE* fp = fopen("output.txt","w");

	int T;	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		int ans = solve();
		printf("Case #%d: ", tc);
//		fprintf(fp,"Case #%d: ", tc);

		if (ans != -1)
		{
			printf("%d\n", ans);
//			fprintf(fp,"%d\n", ans);
		}
		else
		{
			printf("IMPOSSIBLE\n");
//			fprintf(fp,"IMPOSSIBLE\n");
		}
	}
}

int solve()
{
	char P[1001]; scanf("%s", P);
	int K;	scanf("%d", &K);

	int size = strlen(P);
	bool is_happy[1001];
	for (int i = 0; i < size; ++i)
	{
		if (P[i] == '-') is_happy[i] = false;
		else	is_happy[i] = true;
	}

	int cnt = 0;
	for (int i = 0; i < size - K + 1; ++i)
	{
		if (!is_happy[i])
		{
			++cnt;
			for (int j = 0; j < K; ++j)
				is_happy[i + j] ^= 1;
		}
	}

	for (int i = 0; i < size; ++i)
		if (!is_happy[i]) return -1;
	return cnt;
}
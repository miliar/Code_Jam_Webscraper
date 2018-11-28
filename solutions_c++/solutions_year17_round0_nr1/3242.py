#include <cstdio>
#include <cassert>
#include <queue>
#include <functional>
using namespace std;

#ifdef _MSC_VER
#pragma warning(disable: 4996) // Disable deprecation
#endif 

int gVisiteds[1200];
typedef pair<int, int> IPAIR;

int Solve(int st, int n, int k)
{
	const int mask = (1 << k) - 1;
	memset(gVisiteds, 0, sizeof(gVisiteds));
	queue<IPAIR> q;
	q.push( {st,0});
	while (!q.empty())
	{
		IPAIR state = q.front();
		q.pop();
		if (state.first == 0)
			return state.second;

		if (gVisiteds[state.first] == 0)
		{
			gVisiteds[state.first] = 1;
			for (int i = 0; i <= n-k; ++i)
			{
				int newSt = state.first ^ (mask << i);
				if (gVisiteds[newSt] == 0)
				{
					q.push({newSt, state.second+1});
				}
			}
		}
	}
	return -1;
}

int main()
{
//	freopen("a.in", "r", stdin);
	char buff[1024];
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int K;
		scanf("%s%d", buff, &K);
		int state = 0;
		char *s = buff;
		for(; *s; ++s)
		{
			state <<= 1;
			state |= (*s == '-') ? 1 : 0;
		}
		int ans = Solve(state, s-buff, K);
		printf("Case #%d: ", t);
		if (ans >= 0)
		{
			printf("%d\n", ans);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}

	fclose(stdout);
	return 0;
}

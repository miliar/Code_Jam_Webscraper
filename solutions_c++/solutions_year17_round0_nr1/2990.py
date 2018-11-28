#include <cstdio>
#include <cstring>
#define CODE "A-large"
#define MEM(x, y) memset((x), (y), sizeof(x))
const int MAXC = 1005;
char buff[MAXC]{ };
int cnt, K, N, T;

int main()
{
	freopen(CODE ".in", "r", stdin);
	freopen(CODE ".out", "w", stdout);
	scanf("%d", &T);
	for(int _ = 1; _ <= T; ++_)
	{
		scanf(" %s", buff);
		scanf("%d", &K);
		cnt = 0;
		N = strlen(buff);
		bool yes = true;
		for(int i = 0; i < N; ++i)
			if(buff[i] != '+')
			{
				if(i+K > N)
				{	// Cannot Flip
					yes = false;
					break;
				}
				int nxt = i+K;
				for(int j = 0; j < K; ++j) // Flip
				{
					if(buff[i+j] == '+')
					{
						if(nxt == i+K)
							nxt = i+j;
						buff[i+j] = '-';
					}
					else
						buff[i+j] = '+';
				}
				i = nxt-1; // Small Skipping
				++cnt;
			}
		if(yes)
			printf("Case #%d: %d\n", _, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", _);
	}
	return 0;
}
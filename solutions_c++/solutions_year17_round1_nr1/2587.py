#include <iostream>

const int maxn = 25 + 5;
char g[maxn][maxn];
bool visited[maxn][maxn];
int R, C;

static inline void spray(int x, int y, int val)
{
	//find the maximax rectangle
	int lm, rm; //left-most and right-most
	for (lm = y; lm > 0 && g[x][lm - 1] == '?'; --lm) {
		g[x][lm - 1] = val;
		visited[x][lm - 1] = true;
	}
	for (rm = y; rm < C - 1 && g[x][rm + 1] == '?'; ++rm) {
		g[x][rm + 1] = val;
		visited[x][rm + 1] = true;
	}

	//then scan from up to bottom
	bool flag = true;
	for (int n = x - 1; n >= 0 && flag; --n)
	{
		for (int t = lm; t <= rm && flag; ++t)
			if (g[n][t] != '?')
				flag = false;
		if (flag) {
			//memset(&g[n][lm], val, rm - lm + 1);
			for (int t = lm; t <= rm; ++t) {
				g[n][t] = val;
				visited[n][t] = true;
			}
		}
	}
	flag = true;
	for (int n = x + 1; n < R && flag; ++n)
	{
		for (int t = lm; t <= rm && flag; ++t)
			if (g[n][t] != '?')
				flag = false;
		if (flag) {
			//memset(&g[n][lm], val, rm - lm + 1);
			for (int t = lm; t <= rm; ++t) {
				g[n][t] = val;
				visited[n][t] = true;
			}
		}
	}
}

int main()
{
	FILE *debugStream;
	freopen_s(&debugStream, "A-large.in", "r", stdin);
	freopen_s(&debugStream, "A-large.out", "w", stdout);
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		memset(g, 0, sizeof(g));
		memset(visited, 0, sizeof(visited));
		std::cin >> R >> C;
		for (int j = 0; j < R; ++j)
			for (int k = 0; k < C; ++k)
				std::cin >> g[j][k];
		//then calculate every row and column
		for (int j = 0; j < R; ++j)
		{
			for (int k = 0; k < C; ++k)
			{
				if ('?' != g[j][k] && !visited[j][k])
				{
					spray(j, k, g[j][k]);
				}
			}
		}

		std::cout << "Case #" << i << ":\n";
		for (int j = 0; j < R; ++j)
			std::cout << g[j] << std::endl;
	}
	return 0;
}
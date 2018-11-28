#include <bits/stdc++.h>
using namespace std;
const int N = 210;
typedef long long ll;
int mod = 1000000007;
char s[N][N];
void run()
{
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", s[i]);
	int dir[2][2] = {0, 1, 0, -1};
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (s[i][j] != '?')
			{
				for (int k = 0; k < 2; k++)
				{
					int x = i, y = j;
					do
					{
						x += dir[k][0];
						y += dir[k][1];
						if (y < 0 || y >= m || s[x][y] != '?')
							break;
						s[x][y] = s[i][j];
					}while(true);
				}
			}
	for (int i = 0; i < n; i++)
	{
		if (s[i][0] == '?')
		{
			int x = i - 1;
			if (x < 0)
				x = 1;
			while (x < n)
				if (s[x][0] != '?')
					break;
				else
					x++;
			for (int j = 0; j < m; j++)
				s[i][j] = s[x][j];
		}
		puts(s[i]);
	}

}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	scanf("%d", &T);
	 
	while (T--)
	{ 
		printf("Case #%d:\n", cas++);
		run();
	}
    return 0;
}
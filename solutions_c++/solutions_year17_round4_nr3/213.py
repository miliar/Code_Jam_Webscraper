#include <bits/stdc++.h>
using namespace std;

const int maxn = 100000;

struct TwoSAT
{
	int n;
	vector <int> G[maxn * 2];
	bool mark[maxn * 2];
	int S[maxn * 2], c;
	
	bool dfs(int x)
	{
		if (mark[x ^ 1]) return false;
		if (mark[x]) return true;
		mark[x] = true;
		S[c ++] = x;
		for (int i = 0; i < (int)G[x].size(); ++ i)
			if (!dfs(G[x][i])) return false;
		return true;
	}
	
	void init(int n)
	{
		this -> n = n;
		for (int i = 0; i < 2 * n; ++ i) G[i].clear();
		memset(mark, 0, sizeof(mark));
	}
	
	void add_clause(int x, int xval, int y, int yval)
	{
		
//		printf("add %d %d %d %d\n", x, xval, y, yval);
		
		x = x * 2 + xval;
		y = y * 2 + yval;
		G[x ^ 1].push_back(y);
		G[y ^ 1].push_back(x);
		
//		printf("	%d %d\n", x ^ 1, y);
//		printf("	%d %d\n", y ^ 1, x); 
		
	}
	
	bool solve()
	{
		for (int i = 0; i < 2 * n; i += 2)
		{
			if (!mark[i] && !mark[i + 1])
			{
				c = 0;
				if (!dfs(i))
				{
					while (c > 0) mark[S[-- c]] = false;
					if (!dfs(i + 1)) return false;
				}
			}
		}
		return true;
	}
	
}A;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

int T, n, m, Cnt;
int on[1001][1001][2], id[1001][1001], Del[1001][1001], type[1001][1001][2];
char mp[1001][1001];

bool go(int x, int y, int t)
{
	if (x < 1 || x > n || y < 1 || y > m) return 1;
	if (mp[x][y] == '#') return 1;
	if (mp[x][y] == '|' || mp[x][y] == '-') return 0;
	if (mp[x][y] == '.') return go(x + dx[t], y + dy[t], t);
	if (mp[x][y] == '\\')
	{
		/*
			0 -> 1
			1 -> 0
			2 -> 3
			3 -> 2
		*/
		return go(x + dx[t ^1], y + dy[t ^ 1], t ^ 1);
	}
	if (mp[x][y] == '/')
	{
		/*
			0 -> 3
			3 -> 0
			1 -> 2
			2 -> 1
		*/
		return go(x + dx[3 - t], y + dy[3 - t], 3 - t);
	}
}

void cover(int x, int y, int t, int id, int tp)
{
	if (x < 1 || x > n || y < 1 || y > m) return;
	if (mp[x][y] == '#') return;
	
//	printf("cover %d %d %d\n", x, y, id);
	
	if (mp[x][y] == '.') 
	{
		if (on[x][y][0] == -1) on[x][y][0] = id, type[x][y][0] = tp;
		else if (on[x][y][0] != id) on[x][y][1] = id, type[x][y][1] = tp;
		cover(x + dx[t], y + dy[t], t, id, tp);
	}
	if (mp[x][y] == '\\')
	{
		/*
			0 -> 1
			1 -> 0
			2 -> 3
			3 -> 2
		*/
		cover(x + dx[t ^1], y + dy[t ^ 1], t ^ 1, id, tp);
	}
	if (mp[x][y] == '/')
	{
		/*
			0 -> 3
			3 -> 0
			1 -> 2
			2 -> 1
		*/
		cover(x + dx[3 - t], y + dy[3 - t], 3 - t, id, tp);
	}
}

void del(int x, int y, int t)
{
	if (x < 1 || x > n || y < 1 || y > m) return;
	if (mp[x][y] == '#') return;
	
//	printf("del %d %d\n", x, y);
	
	if (mp[x][y] == '.') 
	{
		Del[x][y] = 1;
		del(x + dx[t], y + dy[t], t);
	}
	if (mp[x][y] == '\\')
	{
		/*
			0 -> 1
			1 -> 0
			2 -> 3
			3 -> 2
		*/
		del(x + dx[t ^1], y + dy[t ^ 1], t ^ 1);
	}
	if (mp[x][y] == '/')
	{
		/*
			0 -> 3
			3 -> 0
			1 -> 2
			2 -> 1
		*/
		del(x + dx[3 - t], y + dy[3 - t], 3 - t);
	}
}

int main()
{
	
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++ i) scanf("%s", mp[i] + 1);
		Cnt = 0;
		for (int i = 1; i <= n; ++ i)
			for (int j = 1; j <= m; ++ j)
			{
				if (mp[i][j] == '.') on[i][j][0] = on[i][j][1] = -1, Del[i][j] = 0;
				else if (mp[i][j] == '|' || mp[i][j] == '-') id[i][j] = Cnt ++;
			}
		A.init(Cnt);
		int flag = 1;
		for (int i = 1; i <= n; ++ i)
		{
			for (int j = 1; j <= m; ++ j)
				if (mp[i][j] == '|' || mp[i][j] == '-')
				{
					int flag1, flag2;
					if (!go(i - 1, j, 3) || !go(i + 1, j, 1)) flag1 = 0;
					else flag1 = 1;
					if (!go(i, j + 1, 0) || !go(i, j - 1, 2)) flag2 = 0;
					else flag2 = 1;
					
//					printf("%d %d %d %d\n", i, j, flag1, flag2);
					
					if (flag1 && flag2) 
					{
						for (int t = 0; t < 4; ++ t) cover(i + dx[t], j + dy[t], t, id[i][j], t & 1);
					}
					if (!flag1 && !flag2)
					{
						flag = 0;
						break;
					}
					if (!flag1 && flag2)
					{
						A.mark[id[i][j] * 2] = 1;
						del(i + dx[0], j + dy[0], 0);
						del(i + dx[2], j + dy[2], 2);
					}
					if (flag1 && !flag2)
					{
						A.mark[id[i][j] * 2 + 1] = 1;
						del(i + dx[1], j + dy[1], 1);
						del(i + dx[3], j + dy[3], 3);
					}
				}
			if (!flag) break;
		}
		if (flag)
		{
			for (int i = 1; i <= n; ++ i)
			{
				for (int j = 1; j <= m; ++ j)
					if (mp[i][j] == '.' && !Del[i][j])
					{
						if (on[i][j][1] == -1)
						{
							if (on[i][j][0] == -1) 
							{
	//							printf("	gg\n");
								flag = 0;
								break;
							}
							if (A.mark[2 * on[i][j][0] + (type[i][j][0] ^ 1)])
							{
								flag = 0;
								break;
							}
							A.mark[2 * on[i][j][0] + type[i][j][0]] = true;
						} else {
							A.add_clause(on[i][j][0], type[i][j][0], on[i][j][1], type[i][j][1]);
	//						A.add_clause(2 * on[i][j][0], type[i][j][0], 2 * on[i][j][1], type[i][j][1] ^ 1);
						}
					}
				if (!flag) break;
			}
		} 
		if (flag)
		{
			for (int i = 0; i < Cnt * 2; ++ i)
			{
				if (A.mark[i])
				{
					A.mark[i] = 0; 
			//		printf("set %d\n", i);
					if (!A.dfs(i))
					{
						flag = 0;
						break;
					}
				}
			}
		}
		if (flag && A.solve())
		{
			printf("POSSIBLE\n");
			
//			for(int i = 0; i < 2 * Cnt; ++ i) printf("%d ",A.mark[i]);
//			printf("\n"); 
			
			for (int i = 1; i <= n; ++ i)
			{
				for (int j = 1; j <= m; ++ j)
				{
					if (mp[i][j] == '.' || mp[i][j] == '\\' || mp[i][j] == '/' || mp[i][j] == '#') putchar(mp[i][j]);
					else {
						if (A.mark[id[i][j] * 2]) putchar('-');
						else putchar('|');
					}
				}
				printf("\n");
			}
		} else printf("IMPOSSIBLE\n");
	}
	return 0;
}


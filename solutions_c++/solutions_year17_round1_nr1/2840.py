#include <cstdio>
#include <cstring>
#include <utility>
#define CODE "A-small-attempt0"
// "A-small-0"
#define MEM(x, y) memset((x), (y), sizeof(x))
#define X first
#define Y second
typedef std::pair<int,int> pii;
const int MAXC = 30;
int   BIT[MAXC][MAXC][MAXC]{ }; // Prefix of char C: [C][i][j]
char buff[MAXC][MAXC]{ };
char  out[MAXC][MAXC]{ };
pii   loc[MAXC]{ };
int M, N, T;
bool done;

void tree_add(int YY, int XX, int k, int V)
{
	for(int y = YY; y <= N; y += y & -y)
		for(int x = XX; x <= M; x += x & -x)
			BIT[k][y][x] += V;
}

int tree_get(int YY, int XX, int k)
{
	int ret = 0;
	for(int y = YY; y >= 1; y -= y & -y)
		for(int x = XX; x >= 1; x -= x & -x)
			ret += BIT[k][y][x];
	return ret;
}

int getSum(int i, int j, int k, int l, int C)
{
	return tree_get(k, l, C) - tree_get(i-1, l, C) - tree_get(k, j-1, C) + tree_get(i-1, j-1, C);
}

bool uni(int i, int j, int k, int l, int C)
{
	return getSum(i, j, k, l, C) == getSum(i, j, k, l, 26);
}

#include <cassert>

bool dfs(int idx, int cost)
{
	if(!cost)
		return true;
	else if(loc[idx].X > 0)
	{
		char C = idx+'A';
		// printf("Char %c\n", C);
		for(int i = 1; i <= N; ++i) // Y-Coord of TL
		for(int j = 1; j <= M; ++j) if((buff[i][j] == C) || (buff[i][j] == '?'))
		{	// X-Coord of TL
			for(int k = i; k <= N; ++k) if(uni(i, j, k, j, idx))
			{	// Y-Coord of BR
				int maxL = M;
				for(int l = j; l <= M; ++l)
					if(uni(i, j, k, l, idx))
					{	// X-Coord of BR
						for(int m = i; m <= k; ++m)
							if(buff[m][l] != C)
							{
								assert(buff[m][l] == '?');
								tree_add(m, l, idx, 1);
								tree_add(m, l,  26, 1);
								out[m][l] = C;
							}
						// printf("[%d,%d] to [%d,%d]     cost=%d\n", i, j, k, l, cost - (k-i+1)*(l-j+1));
						// for(int i = 1; i <= N; ++i)
						//	puts(out[i]+1);
						if(dfs(idx+1, cost - (k-i+1)*(l-j+1) ))
							return true; // Solution Found
					}
					else
					{	// break for-l
						maxL = l-1;
						break;
					}
				// Overwrite
				for(int l = j; l <= maxL; ++l)
					for(int m = i; m <= k; ++m)
						if(buff[m][l] != C)
						{
							assert(buff[m][l] == '?');
							tree_add(m, l, idx, -1);
							tree_add(m, l,  26, -1);
							out[m][l] = '?';
						}
			}
			else	// Break for-k
				break;
		}
		// printf("Char %c [END]\n", C);
	}
	else if(idx >= 'Z'-'A')
		return false; // Filled Everything
	return dfs(++idx, cost); // Letter doesn't Exist
}

int main()
{
	freopen(CODE ".in", "r", stdin);
	freopen(CODE ".out", "w", stdout);
	scanf("%d", &T);
	for(int _T = 1; _T <= T; ++_T)
	{
		scanf(" %d%d", &N, &M);
		for(int i = 1; i <= N; ++i)
			scanf(" %s", buff[i]+1);
		for(int i = 0; i < MAXC; ++i)
			loc[i] = { 0, 0 };
		MEM(BIT, 0);
		memcpy(out, buff, sizeof(char)*MAXC*MAXC);
		for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= M; ++j)
			if(buff[i][j] != '?')
			{
				loc[buff[i][j]-'A'] = { j, i };
				tree_add(i, j, buff[i][j]-'A', 1);
				tree_add(i, j, 26, 1);
			}
		// Print Code
		/* for(int k = 0; k <= 26; ++k) if(loc[k].X > 0 || k==26)
		{
			printf("Char %c:\n", k+'A');
			for(int i = 1; i <= N; ++i)
				for(int j = 1; j <= M; ++j)
					printf("%d%c", tree_get(i, j, k), (j==M)?'\n':' ');
		} */
		dfs(0, M*N);
		printf("Case #%d: \n", _T);
		for(int i = 1; i <= N; ++i)
			puts(out[i]+1);
	}
	return 0;
}
#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

const int A = 0;
const int B = 1;
const int N = 24 * 60;
const int HN = 720;
const int INF = 1 << 25;

int NA, NB;
int T;
bool ocp[N + 5][2];
int f[N + 5][N][2][2];
int ts, te;

int kase;
FILE* fc;

inline int Min(int a, int b)
{
	return a < b ? a : b;
}

inline void case_init()
{
	printf("Case #%d: ", ++kase);
	scanf("%d%d", &NA, &NB);
	for (int i = 0; i <= N; ++i)
	{
		ocp[i][A] = ocp[i][B] = false;
		for (int j = 0; j <= HN; ++j)
		{
			f[i][j][A][A] = f[i][j][A][B] = INF;
			f[i][j][B][A] = f[i][j][B][B] = INF;
		}
	}
	for (int i = 1; i <= NA; ++i)
	{
		scanf("%d%d", &ts, &te);
		for (int j = ts + 1; j <= te; ++j) ocp[j][A] = true;
	}
	for (int i = 1; i <= NB; ++i)
	{
		scanf("%d%d", &ts, &te);
		for (int j = ts + 1; j <= te; ++j) ocp[j][B] = true;
	}
	f[1][1][A][A] = 0;
	f[1][0][B][B] = 0;
	if (ocp[1][A]) f[1][1][A][A] = INF;
	if (ocp[1][B]) f[1][0][B][B] = INF;
}
inline void case_solve()
{
	for (int i = 2; i <= N; ++i)
	{
	//	if(i==N) printf("%d\n", i);
		for (int j = 0; j <= i && j <= HN; ++j)
		{
			//printf("%d %d\n", i, j);
			//proc f[i][j][A][O]
			if (!ocp[i][A])
			{
				for (int k = 1; k < i && k <= j; ++k)
				{
					if (ocp[i - k + 1][A]) break;
					f[i][j][A][A] = Min(f[i][j][A][A], f[i - k][j - k][A][A]);
					f[i][j][A][A] = Min(f[i][j][A][A], f[i - k][j - k][B][A] + 1);

					f[i][j][A][B] = Min(f[i][j][A][B], f[i - k][j - k][A][B]);
					f[i][j][A][B] = Min(f[i][j][A][B], f[i - k][j - k][B][B] + 1);
				}
			}
			if (!ocp[i][B])
			{
				for (int k = 1; k <= i - j && k <= HN && k < i; ++k)
				{
					if (ocp[i - k + 1][B]) break;
					f[i][j][B][A] = Min(f[i][j][B][A], f[i - k][j][B][A]);
					f[i][j][B][A] = Min(f[i][j][B][A], f[i - k][j][A][A] + 1);

					f[i][j][B][B] = Min(f[i][j][B][B], f[i - k][j][B][B]);
					f[i][j][B][B] = Min(f[i][j][B][B], f[i - k][j][A][B] + 1);
				}
			}
			//printf("%d %d\n", i, j);
		}
	}
//	puts("dfghjkl");
	//fprintf(fc,"%d\n", kase);
	printf("%d\n", Min(Min(f[N][HN][A][A], f[N][HN][B][B]), Min(f[N][HN][A][B], f[N][HN][B][A]) + 1));
} 

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//fc = fopen("con", "w");
	for (scanf("%d", &T); T; --T)
	{
		case_init();
		//printf("%d", kase);
		case_solve();
	}
	return 0;
}
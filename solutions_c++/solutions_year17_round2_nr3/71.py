#include <cstdio>
#include <algorithm>
#include <limits>

const int N = 105;
const long long INF = 1LL << 60LL;
long long dist[N][N];
double dist_t[N][N];
int range[N], speed[N];
int n;

void floyd()
{
    for(int k = 0; k < n; k++)
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
		dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
}

void floyd_t()
{
    for(int k = 0; k < n; k++)
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
		dist_t[i][j] = std::min(dist_t[i][j], dist_t[i][k] + dist_t[k][j]);
}

int main()
{
    int tests;
    scanf("%d", &tests);

    for(int test = 1; test <= tests; test++)
    {
	int q;
	scanf("%d %d", &n, &q);
	for(int i = 0; i < n; i++)
	    scanf("%d %d", &range[i], &speed[i]);

	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
	    {
		int x;
		scanf("%d", &x);
		dist[i][j] = (x == -1) ? INF : x;
	    }

	floyd();

	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
		if(dist[i][j] <= range[i])
		    dist_t[i][j] = (double)dist[i][j] / (double)speed[i];
		else dist_t[i][j] = 1e50;

	floyd_t();

	printf("Case #%d: ", test);
	while(q--)
	{
	    int u, v;
	    scanf("%d %d", &u, &v);
	    printf("%.7lf%c", dist_t[u - 1][v - 1], q ? ' ' : '\n');
	}
    }

    return 0;
}

#pragma region Header
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <queue>
#include <complex>
#include <bitset>
#include <random>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for(int i = 0; i < len; ++i) cerr << arr[i] << ' '; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for(const auto& e : it) cerr << e << ' '; cerr << endl << endl;}
#define print_2d_array(arr, len1, len2) {cerr << #arr << ':' << endl;\
for(int i = 0; i < len1; ++i, cerr << endl) \
for(int j = 0; j < len2; ++j)\
cerr << arr[i][j] << ' '; \
cerr << endl; }
#define print_endl() cerr << endl
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0;
#define print_iterable(it) (void)0;
#define print_2d_array(arr, len1, len2) (void)0;
#define print_endl() (void)0
#endif

#pragma endregion

typedef long long ll;
typedef pair<double, int> pii;

const int N = 105;
const double INF = 1e18;
int lim[N], speed[N];
ll g[N][N];
double dist[N];
priority_queue<pair<double, int>> q;
int n;

double solve(int s, int f)
{
	fill(dist, dist + n, INF);
	dist[s] = 0;
	q.push(pii(0, s));

	while (!q.empty())
	{
		int v = q.top().second;
		double dv = -q.top().first;
		q.pop();

		if (dist[v] < dv)
			continue;

		for (int u = 0; u < n; u++)
		{
			if (g[v][u] == -1)
				continue;
			if (g[v][u] > lim[v])
				continue;

			double t = dv + 1.0 * g[v][u] / speed[v];

			if (dist[u] > t)
			{
				dist[u] = t;
				q.push(pii(-t, u));
			}
		}
	}

	return dist[f];
}

void solve()
{
	int tasks;
	scanf("%d%d", &n, &tasks);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &lim[i], &speed[i]);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%lld", &g[i][j]);

	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				if (g[i][k] == -1 || g[k][j] == -1)
					continue;

				ll val = g[i][k] + g[k][j];
				if (g[i][j] == -1 || g[i][j] > val)
					g[i][j] = val;
			}


	for (int e = 0; e < tasks; e++)
	{
		int u, v;
		scanf("%d%d", &u, &v);
		u--; v--;

		double ans = solve(u, v);
		printf("%.12lf ", ans);
	}	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		solve();
		cout << endl;

		eprintf("DONE %d/%d in %.2lf\n", test, tests, (double)clock() / CLOCKS_PER_SEC);

	}

	eprintf("\n\ntime: %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
	return 0;
}
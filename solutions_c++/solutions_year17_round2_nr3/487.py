#include <cstdlib>
#include <iostream>
#include <queue>
#include <cstring>
#include <iomanip>

using namespace std;

typedef long long LL;
const int MAXN = 105;

int N, Q;
LL dis[MAXN], vel[MAXN];
LL d[MAXN][MAXN];
double ans[MAXN];
bool vis[MAXN];
void Solve()
{
	cin >> N >> Q;
	for (int i = 1; i <= N; ++i)
		cin >> dis[i] >> vel[i];
	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= N; ++j)
			cin >> d[i][j];
	for (int k = 1; k <= N; ++k)
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				if (d[i][k] != -1 && d[k][j] != -1)
				{
					if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j])
						d[i][j] = d[i][k] + d[k][j];
				}
	for (int Case = 1, u, v; Case <= Q; ++Case)
	{
		cin >> u >> v;
		for (int i = 1; i <= N; ++i)
			ans[i] = -1;
		ans[u] = 0;
		memset(vis, 0, sizeof(vis));
		priority_queue<int> pq;
		pq.push(u);
		while (!pq.empty())
		{
			int i = pq.top();
			pq.pop();
			vis[i] = 0;
			for (int j = 1; j <= N; ++j)
				if (d[i][j] != -1 && d[i][j] <= dis[i])
					if (ans[j] < 0 || ans[j] > ans[i] + (d[i][j] * 1.0 / vel[i]))
					{
						ans[j] = ans[i] + (d[i][j] * 1.0 / vel[i]);
						if (!vis[j])
						{
							vis[j] = 1;
							pq.push(j);
						}
					}
		}
		cout << setprecision(6) << ans[v] << " ";
	}
	cout << endl;
}

int T;
int main()
{
	cout << setiosflags(ios::fixed);
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}

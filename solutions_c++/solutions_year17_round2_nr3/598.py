#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr, args)

typedef long double LD;
typedef pair <LD, int> pii;
const int maxn = 2e3 + 10;
const LD INF = 1e17;

int N, Q;
LD E[maxn], S[maxn];
LD D[maxn][maxn];

int U[maxn], V[maxn];

LD dist[maxn];
bool mrk[maxn];

LD dijkstra (int source, int destiny)
{
	for (int i = 1; i <= N; ++i)
	{
		dist[i] = INF;
		mrk[i] = false;
	}

	dist[source] = 0;

	set <pii> Set;

	Set.insert (pii (dist[source], source));

	while (!Set.empty())
	{
		int v = Set.begin()->second;
		Set.erase (Set.begin());

		if (mrk[v])
			continue;

		mrk[v] = true;

		for (int i = 1; i <= N; ++i)
			if (!mrk[i] && D[v][i] <= E[v] && dist[i] > dist[v] + (D[v][i] / S[v]))
			{
				dist[i] = dist[v] + (D[v][i] / S[v]);
				Set.insert (pii (dist[i], i));
			}
	}


	return dist[destiny];
}

void FW ()
{
	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= N; ++j)
			if (D[i][j] == -1)
				D[i][j] = INF;
	
	for (int i = 1; i <= N; ++i)
		D[i][i] = 0.0;

	for (int k = 1; k <= N; ++k)
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				D[i][j] = min (D[i][j], D[i][k] + D[k][j]);
}

int main ()
{
	freopen ("output.txt", "w", stdout);

	int T;
	cin >> T;

	int test = 0;

	while (T--)
	{
		cin >> N >> Q;

		for (int i = 1; i <= N; ++i)
			cin >> E[i] >> S[i];

		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				cin >> D[i][j];

		FW ();

		cout << "Case #" << ++test << ": ";

		for (int i = 1; i <= Q; ++i)
		{
			int u, v;
			cin >> u >> v;
			cout << fixed << setprecision (15) << dijkstra(u, v);
			if (i != Q)
				cout << " ";
			else
				cout << '\n';
		}
	}

	return 0;
}
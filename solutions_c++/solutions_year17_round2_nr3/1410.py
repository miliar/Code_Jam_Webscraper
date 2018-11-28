#include <iostream>
#include <vector>
#include <cstdio>
#include <limits>
#include <cassert>
#include <experimental/optional>
#include <algorithm>

using namespace std;
using namespace std::experimental;

typedef pair <long, long> pii;

#define y first
#define x second

#define all(n) n.begin(), n.end()
#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())

double go(vector <vector <optional <double>>> &G, int n, const vector <int> &L, const vector <long> &D, const vector <int> &S, int w, int h)
{
	// cerr << n << ' ' << w << ' ' << h << endl;
	if (w == n)
		return 0;

	if (L[h] < w)
		return numeric_limits<double>::infinity();

	if (G[w][h])
		return *G[w][h];

	G[w][h] = min(go(G, n, L, D, S, w + 1, h) + D[w] / double(S[h]), go(G, n, L, D, S, w + 1, w) + D[w] / double(S[w]));
	return *G[w][h];
}

double solve(int n, const vector <int> &E, const vector <int> &S, const vector <long> &D)
{
	vector <long> K(n);
	K[0] = 0;

	forsn(i, 1, K.size())
		K[i] = K[i - 1] + D[i - 1];

	vector <int> L(n, -1);
	fore(i, L)
	{
		forsn(j, i, n)
		{
			if (E[i] < K[j] - K[i])
			{
				L[i] = j - 1;
				break;
			}
		}

		if (L[i] == -1)
			L[i] = n;
	}

	vector <vector <optional<double>>> G(n, vector <optional <double>> (n));
	return go(G, n, L, D, S, 0, 0);
}

int main()
{
	int t; cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int n, q; cin >> n >> q;
		assert(q == 1);

		vector <int> E(n), S(n);
		forn(i, n)
			cin >> E[i] >> S[i];

		vector <long> D(n);
		forn(i, n)
		{
			forn(j, n)
			{
				int a; cin >> a;
				if (i + 1 == j)
					D[i] = a;
				else
					assert(a == -1);
			}
		}

		int u, v;
		cin >> u >> v;

		printf("Case #%d: %f\n", z, solve(n, E, S, D));
	}
}

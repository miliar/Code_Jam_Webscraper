#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <cmath>

using namespace std;

typedef pair <int, int> pii;

pii limit(int y, int x)
{
	return make_pair(int(ceil(x / (y * 1.1))), int(floor(x / (y * .9))));
}

int solve(int n, int p, const vector <int> &R, const vector <vector <int>> &Q)
{
	vector <vector <pii>> L(n, vector <pii> (p));

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < p; j++)
			L[i][j] = limit(R[i], Q[i][j]);

		sort(L[i].begin(), L[i].end());
	}

	int r = 0;
	while (all_of(L.begin(), L.end(), [](auto p){ return !p.empty(); }))
	{
		auto m = min_element(L.begin(), L.end());
		
		if (all_of(L.begin(), L.end(), [&](auto p){ return p[0].first <= (*m)[0].second; }))
		{
			r += 1;
			for (auto &k : L)
				k.erase(k.begin());
		}
		else
		{
			m->erase(m->begin());
		}
	}

	return r;
}

int main()
{
	int n; cin >> n;
	for (int z = 1; z <= n; z++)
	{
		int n, p; cin >> n >> p;
		
		vector <int> R(n);
		for (auto &k : R)
			cin >> k;

		vector <vector <int>> Q(n, vector <int> (p));
		for (auto &y : Q)
		{
			for (auto &x : y)
				cin >> x;
		}

		printf("Case #%d: %d\n", z, solve(n, p, R, Q));
	}

	return 0;
}

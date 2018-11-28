#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>

#define MAXN 60
using namespace std;

double portions[60];
double ingr[60][60];
bool V[60][60];
int N, P;

inline void init()
{
	int i, j;

	cin >> N >> P;

	memset(V, 0, sizeof(V));

	for (i = 0; i < N; i++)
		cin >> portions[i];

	for (i = 0; i < N; i++)
	{
		for (j = 0; j < P; j++)
			cin >> ingr[i][j];

		sort(ingr[i], ingr[i] + P);
	}
}

inline double lo(double val)
{
	return val * 0.9;
}

inline double hi(double val)
{
	return val * 1.1;
}

inline pair<int, int> get_range(double val, double c)
{
	return make_pair(ceil(val / hi(c)), floor(val / lo(c)));
}

inline pair<int, int> intersect(pair<int, int> a, pair<int, int> b)
{
	pair<int, int> rval;

	rval.first = max(a.first, b.first);
	rval.second = min(a.second, b.second);

	return rval;
}

inline bool is_good(pair<int, int> a)
{
	return a.first <= a.second;
}

bool search(pair<int, int> r, int row)
{
	int i;
	pair<int, int> n;

	if (row == N)
		return 1;

	for (i = 0; i < P; i++)
		if (!V[row][i])
		{
			n = intersect(r, get_range(ingr[row][i], portions[row]));
			if (is_good(n))
			{
				V[row][i] = 1;
				if (search(n, row + 1))
					return 1;
				V[row][i] = 0;
			}
		}

	return 0;
}

inline int solve()
{
	int k;
	int rval = 0;

	for (k = 0; k < P; k++)
	{
		pair<int, int> r = get_range(ingr[0][k], portions[0]);
		if (is_good(r) && search(r, 1))
			rval++;
	}

	return rval;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int T, i;

	cin >> T;

	for (i = 1; i <= T; i++)
	{
		init();
		cout << "Case #" << i << ": " << solve() << "\n";
		solve();

	}

	return 0;
}
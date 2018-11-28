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
typedef pair<int, int> pii;

const int N = 5000;
bool used[N];

void solve()
{
	int n, k;
	cin >> n >> k;
	n += 2;
	fill(used, used + n, false);
	used[0] = used[n - 1] = true;

	int ls, rs;
	for (int i = 0; i < k; i++)
	{
		ls = -1, rs = -1;
		int best = -1;

		for (int pos = 0; pos < n; pos++)
		{
			if (used[pos])
				continue;

			int l = 0, r = 0;
			while (!used[pos - l - 1])
				l++;
			while (!used[pos + r + 1])
				r++;

			bool better = false;

			if (min(ls, rs) != min(l, r))
			{
				if (min(ls, rs) < min(l, r))
					better = true;
			}
			else
			{
				if (max(ls, rs) != max(l, r))
				{
					if (max(ls, rs) < max(l, r))
						better = true;
				}
			}

			if (better)
			{
				ls = l;
				rs = r;
				best = pos;
			}
		}

		used[best] = true;
	}

	cout << max(ls, rs) << " " << min(ls, rs);
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
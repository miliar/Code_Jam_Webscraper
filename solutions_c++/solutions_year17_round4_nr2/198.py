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

const int N = 1005;
int pos[N], who[N];
int cnt[N];
int goes[N];

void solve()
{
	for (int i = 0; i < N; i++)
		goes[i] = cnt[i] = 0;

	int n, mans, tickets;
	int ans = 1;
	scanf("%d%d%d", &n, &mans, &tickets);
	for (int i = 0; i < tickets; i++)
	{
		scanf("%d%d", &pos[i], &who[i]);
		pos[i]--;
		who[i]--;
		cnt[pos[i]]++;
		goes[who[i]]++;

		ans = max(ans, goes[who[i]]);
	}

	for (; ; ans++)
	{
		bool ok = true;
		int sum = 0;
		int promo = 0;

		for (int i = 0; i < n; i++)
		{
			if (cnt[i] > ans)
				promo += cnt[i] - ans;
			sum += cnt[i];

			if (sum > ans * (i + 1))
				ok = false;
		}

		if (ok)
		{
			printf("%d %d", ans, promo);
			return;
		}
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
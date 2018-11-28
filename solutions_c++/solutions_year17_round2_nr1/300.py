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
pii a[N];

void solve()
{
	int n, d;
	scanf("%d%d", &d, &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &a[i].first, &a[i].second);
	sort(a, a + n);

	double t = 0;
	for (int i = 0; i < n; i++)
		t = max(t, 1.0 * (d - a[i].first) / a[i].second);

	/*for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
		{
			double dist = a[j].first - a[i].first;
			double v = a[i].second - a[j].second;
			if (v <= 0)
				continue;

			double t1 = dist / v;
			double t2 = 1.0 * ((d - a[j].first) - (t1 * a[j].second)) / a[j].second;
			if (t2 >= 0)
				t = max(t, t1 + t2);
		}*/
	printf("%.12lf", d / t);
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
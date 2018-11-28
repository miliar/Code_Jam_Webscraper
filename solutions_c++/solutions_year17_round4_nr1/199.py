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

const int P = 4;
const int N = 105;
int cnt[P];
int dp[N][N][N];

void relaxTo(int &a, int b)
{
	a = max(a, b);
}

void solve()
{
	for (int i = 0; i < P; i++)
		cnt[i] = 0;
	for (int r1 = 0; r1 < N; r1++)
		for (int r2 = 0; r2 < N; r2++)
			for (int r3 = 0; r3 < N; r3++)
				dp[r1][r2][r3] = 0;

	int n, p;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		cnt[x % p]++;
	}
	
	dp[0][0][0] = cnt[0];
	for (int r1 = 0; r1 <= cnt[1]; r1++)
		for (int r2 = 0; r2 <= cnt[2]; r2++)
			for (int r3 = 0; r3 <= cnt[3]; r3++)
			{
				int cur = 1 * r1 + 2 * r2 + 3 * r3;
				cur %= p;
				int got = dp[r1][r2][r3];
				if (cur == 0)
					got++;
				
				relaxTo(dp[r1 + 1][r2][r3], got);
				relaxTo(dp[r1][r2 + 1][r3], got);
				relaxTo(dp[r1][r2][r3 + 1], got);
			}

	int ans = dp[cnt[1]][cnt[2]][cnt[3]];
	printf("%d", ans);
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
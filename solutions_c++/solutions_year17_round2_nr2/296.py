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
typedef pair<int, char> pii;

const int N = 1005;
char s[N];
int n;

void mv(int &ptr)
{
	while (s[ptr] != '_')
		ptr = (ptr + 1) % n;
}

//RYB
void solve(int r, int y, int b)
{
	vector<pii> v;
	v.push_back(pii(r, 'R'));
	v.push_back(pii(y, 'Y'));
	v.push_back(pii(b, 'B'));
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());

	n = r + y + b;
	fill(s, s + n, '_');
	int ptr = 0;

	for (int i = 0; i < v[0].first; i++)
	{
		mv(ptr);
		s[ptr] = v[0].second;
		ptr = (ptr + 2) % n;
	}

	ptr = (ptr - 2 + n) % n;
	for (int i = 0; i < v[1].first; i++)
	{
		mv(ptr);
		s[ptr] = v[1].second;
		ptr = (ptr + 2) % n;
	}

	ptr = (ptr - 2 + n) % n;
	for (int i = 0; i < v[2].first; i++)
	{
		mv(ptr);
		s[ptr] = v[2].second;
		ptr = (ptr + 2) % n;
	}

	bool ok = true;
	for (int i = 0; i < n; i++)
		ok &= (s[i] != s[(i + 1) % n]);

	s[n] = '\0';
	if (ok)
		printf("%s", s);
	else
		printf("IMPOSSIBLE");
}

void solve()
{
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	solve(r, y, b);
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
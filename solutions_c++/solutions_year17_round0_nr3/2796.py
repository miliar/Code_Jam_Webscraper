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
void alt_solve(int n, int k)
{
	multiset<int> s;
	s.insert(-n);
	for (int i = 0; i < k - 1; ++i)
	{
		int x = -(*s.begin());
		s.erase(s.begin());
		s.insert(-(x - 1) / 2);
		s.insert(-x / 2);
	}
	int x = -(*s.begin());
	printf("%d %d .. ", x / 2, (x - 1) / 2);
}

void solve()
{
	ll n, k;
	cin >> n >> k;
	//alt_solve(n, k);
	--k;
	ll mn = (n - 1) / 2, mx = n / 2;
	if (k == 0)
	{
		printf("%lld %lld\n", mx, mn);
		return;
	}
	ll cntn = 1, cntx = 1;
	ll pow_ = 1;
	ll cnt = 1;
	while (k - (1LL << pow_) > 0)
	{
		k -= (1LL << pow_);
		cnt += (1LL << pow_);
		if (mn % 2 == 0 && mx % 2 == 0)
		{
			mx = mn / 2;
			mn = (mn - 1) / 2;
			ll sum = (cntx + cntn);
			cntx = sum;
			cntn = sum;
		}
		else if (mn % 2 == 0)
		{
			mx = mn / 2;
			mn = (mn - 1) / 2;
			cntx = cntx * 2 + cntn;
		}
		else
		{
			mn = (mx - 1) / 2;
			mx = mx / 2;
			cntn = cntn * 2 + cntx;
		}
		if (cnt + mx * cntx + mn * cntn != n)
		{
			int a = 0;
		}
		++pow_;
	}
	if (k <= cntx)
	{
		printf("%lld %lld\n", mx / 2, (mx - 1) / 2);
		return;
	}
	else
	{
		printf("%lld %lld\n", mn / 2, (mn - 1) / 2);
	}
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}

	eprintf("\n\ntime: %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
	return 0;
}
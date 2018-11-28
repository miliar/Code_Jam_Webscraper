#include <climits>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <functional>
#define fi first
#define se second
#define FO(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, a, b) for (int x = a; x < b; ++x)
#define RFO(x, n) for (int x = n - 1; x >= 0; --x)
#define RFOR(x, a, b) for (int x = b - 1; x >= a; --x)
using namespace std;
typedef unsigned char byte;
typedef long long llong;
typedef unsigned long long ullong;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<llong, llong> pll;
inline bool feq(const double& a, const double& b) { return fabs(a - b) < 1e-10; }

int N, P;
int nums[110];

int do2()
{
	int cnt[2] = { 0 };
	FO(i, N)
		++cnt[nums[i] % 2];
	int res = cnt[0];
	res += cnt[1] / 2;
	cnt[1] %= 2;
	return res + cnt[1];
}
int do3()
{
	int cnt[3] = { 0 };
	FO(i, N)
		++cnt[nums[i] % 3];
	int res = cnt[0];
	int p12 = min(cnt[1], cnt[2]);
	res += p12;
	cnt[1] -= p12;
	cnt[2] -= p12;
	res += cnt[1] / 3;
	cnt[1] %= 3;
	res += cnt[2] / 3;
	cnt[2] %= 3;
	return res + (cnt[1] != 0 || cnt[2] != 0);
}
int do4()
{
	int cnt[4] = { 0 };
	FO(i, N)
		++cnt[nums[i] % 4];
	int res = cnt[0];
	// 13
	int p13 = min(cnt[1], cnt[3]);
	res += p13;
	cnt[1] -= p13;
	cnt[3] -= p13;
	// 21
	if (cnt[1] > 0 && cnt[2] > 0)
	{
		int p12 = min(cnt[1] / 2, cnt[2]);
		res += p12;
		cnt[1] -= 2 * p12;
		cnt[2] -= p12;
	}
	// 23
	if (cnt[3] > 0 && cnt[2] > 0)
	{
		int p23 = min(cnt[3] / 2, cnt[2]);
		res += p23;
		cnt[3] -= 2 * p23;
		cnt[2] -= p23;
	}
	// 22
	res += cnt[2] / 2;
	cnt[2] %= 2;
	// 11
	res += cnt[1] / 4;
	cnt[1] %= 4;
	// 33
	res += cnt[3] / 4;
	cnt[3] %= 4;
	// rest
	return res + (cnt[1] != 0 || cnt[2] != 0 || cnt[3] != 0);
}

int main()
{
	int T;
	cin >> T;
	FOR (t, 1, T + 1)
	{
		cin >> N >> P;
		FO(i, N)
			cin >> nums[i];
		int res;
		if (P == 2)
			res = do2();
		else if (P == 3)
			res = do3();
		else
			res = do4();
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
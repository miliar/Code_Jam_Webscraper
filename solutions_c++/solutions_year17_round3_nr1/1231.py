#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdio.h>
#include <cstdio>
#include <stdlib.h>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <climits>
#include <set>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <sstream>
#include <functional>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>
#include <complex>

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef std::pair<int, int> pii;
template <typename T> using min_heap = std::priority_queue<T, std::vector<T>, std::greater<T>>;
template <typename T> using max_heap = std::priority_queue<T, std::vector<T>, std::less<T>>;

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define TESTS(t) int NUMBER_OF_TESTS; cin >> NUMBER_OF_TESTS; for(int t = 1; t <= NUMBER_OF_TESTS; t++)
#define FOR(i, start, end) for(int i = (start); i < (end); i++)
#define ROF(i, start, end) for(int i = (start); i >= (end); i--)
#define all(x) (x).begin(), (x).end()
#define endl "\n"
#define PI asin(1)*2
#define OO (1LL<<31)-1
#define eps 1e-12
#define in(a, b)   ((b).find(a) != (b).end())
#define mp(a, b)   make_pair((a), (b))
#define min(a, b)  ((a) < (b) ? (a) :  (b))
#define max(a, b)  ((a) > (b) ? (a) :  (b))
#define abs(a)     ((a) > 0   ? (a) : -(a))
#define sgn(a)     ((a) > eps ? 1 : ((a) < -eps ? -1 : 0))
#define cl1(x)     ((x)&((x)-1)) // clear lowest 1 bit
#define cl0(x)     ((x)|((x)+1)) // clear lowest 0 bit
#define ct1(x)     ((x)&((x)+1)) // clear all trailing 1 bits
#define pb push_back
#define MOD 1000000007
#define MAX_N 1000
using namespace std;

tuple<ll, ll, int> pc[MAX_N];
tuple<ll, ll, int> cpy[MAX_N];
int n, k;

ll getScore(int idx)
{
	auto first = cpy[idx];
	ll R = get<0>(first);
	ll H = get<1>(first);
	ll ID = get<2>(first);
	sort(pc, pc+n, [](tuple<ll, ll, int> a, tuple<ll, ll, int> b) -> bool
	{
		return get<0>(a)*get<1>(a) > get<0>(b)*get<1>(b);
	});
	int minR = OO, maxR = -1;

	ll score = R*R + 2*R*H;
	int got = 1;
	FOR(i, 0, n)
	{
		if (got == k)
			break;
		ll r = get<0>(pc[i]);
		ll h = get<1>(pc[i]);
		int id = get<2>(pc[i]);
		if (id == ID)
			continue;
		if (r > R)
			continue;
		minR = min(minR, r);
		maxR = max(maxR, r);
		score += 2 * r*h;
		got++;
	}
	if (got != k)
		return -1;
	return score;
}

ld solve()
{
	sort(pc, pc + n, [](tuple<ll, ll, int> a, tuple<ll, ll, int> b) -> bool
	{
		return get<0>(a) > get<0>(b);
	});
	FOR(i, 0, n)
		cpy[i] = pc[i];

	ll mx = -1;
	FOR(i, 0, n)
	{
		ll score = getScore(i);
		mx = max(mx, score);
	}
	return PI * mx;
}

int main()
{
	FAST_IO
#ifdef _DEBUG
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	TESTS(t)
	{
		cin >> n >> k;
		FOR(i, 0, n)
		{
			int r, h;
			cin >> r >> h;
			pc[i] = { r,h,i };
		}
		cout << "Case #" << t << ": " << fixed << setprecision(12) <<  solve() << endl;
	}
    return 0;
}


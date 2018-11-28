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

pii cInt[MAX_N], jInt[MAX_N];

int main()
{
	FAST_IO
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	TESTS(t)
	{
		int ac, aj;
		cin >> ac >> aj;
		FOR(i, 0, ac)
		{
			cin >> cInt[i].first >> cInt[i].second;
		}
		FOR(i, 0, aj)
		{
			cin >> jInt[i].first >> jInt[i].second;
		}
		sort(cInt, cInt + ac, [](pii a, pii b) -> bool
		{
			return a.first < b.first;
		});
		sort(jInt, jInt + aj, [](pii a, pii b) -> bool
		{
			return a.first < b.first;
		});
		cout << "Case #" << t << ": ";
		if (ac + aj == 1)
		{
			cout << 2 << endl;
			continue;
		}
		else if (ac + aj == 2)
		{
			if (ac == 1 && aj == 1)
			{
				cout << 2 << endl;
			}
			else
			{
				int ans = 2;
				if (ac == 2)
				{
					int len1 = cInt[0].second - cInt[0].first;
					int len2 = cInt[1].second - cInt[1].first;
					int lenMid = cInt[1].first - cInt[0].second;
					int lenEnd = cInt[0].first + (1440-cInt[1].second);
					int mn = min(lenMid, lenEnd);
					if (mn + len1 + len2 > 720)
						ans = 4;
				}
				else
				{
					int len1 = jInt[0].second - jInt[0].first;
					int len2 = jInt[1].second - jInt[1].first;
					int lenMid = jInt[1].first - jInt[0].second;
					int lenEnd = jInt[0].first + (1440 - jInt[1].second);
					int mn = min(lenMid, lenEnd);
					if (mn + len1 + len2 > 720)
						ans = 4;
				}
				cout << ans << endl;
			}
			continue;
		}
		else
		{
			cout << "???" << endl;
		}
	}
    return 0;
}


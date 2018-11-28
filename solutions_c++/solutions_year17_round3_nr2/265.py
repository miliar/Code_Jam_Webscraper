#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;
const int T = 24 * 60 + 3;

int n, m;
bool can[2][T];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2)
		return false;

	memset(can, true, sizeof(can));

	forn(i, n)
	{
		int l, r;
		assert(scanf("%d%d", &l, &r) == 2);
		assert(0 <= l && l <= r && r <= 24 * 60);

		fore(j, l, r - 1)
			can[0][j] = false;
	}

	forn(i, m)
	{
		int l, r;
		assert(scanf("%d%d", &l, &r) == 2);
		assert(0 <= l && l <= r && r <= 24 * 60);

		fore(j, l, r - 1)
			can[1][j] = false;
	}

	int cnt[2] = { 0, 0 };
	forn(i, 2)
		fore(j, 0, 24 * 60)
			cnt[i] += int(can[i][j]);
	//cerr << cnt[0] << " " << cnt[1] << endl;
	assert(cnt[0] >= 720 && cnt[1] >= 720);
	
	return true;
}

int z[T][T][2][2];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	memset(z, 63, sizeof(z));

	z[1][1][0][0] = 0;
	z[1][0][1][1] = 0;

	fore(t, 1, 24 * 60 - 1)
		fore(ta, 0, 720)
			forn(first, 2)
				forn(last, 2)
				{
					int& dv = z[t][ta][first][last];
					if (dv > INF / 2)
						continue;

					forn(nlast, 2)
					{
						int nt = t + 1;
						int nta = ta;
						int ntb = t - ta;
						if (nlast == 0)
							nta++;
						else
							ntb++;
						int nfirst = first;

						if (nta > 720 || ntb > 720)
							continue;

						if (!can[nlast][t])
							continue;

						int nv = dv;
						if (last != nlast)
							nv++;

						if (t + 1 == 24 * 60)
						{
							if (nlast != first)
								nv++;
						}

						z[nt][nta][nfirst][nlast] = min(z[nt][nta][nfirst][nlast], nv);
					}
				}

	int ans = INF;
	forn(first, 2)
		forn(last, 2)
			ans = min(ans, z[24 * 60][720][first][last]);	

	assert(ans < INF / 2);
	cout << ans << endl;
}

int main()
{
#ifdef HP
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
		assert(read());
		solve(test);
	}
	
	return 0;
}


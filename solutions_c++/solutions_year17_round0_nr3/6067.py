
// Author: Tiago Togores

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(a) ((int)((a).size()))
#define ALL(a) (a).begin(), (a).end()
#define CLR(a, x) memset(a, x, sizeof a)
#define REP(i, n) for (auto i = 0; i < (n); i++)
#define FORT(it, l) for (auto it = (l).begin(); it != (l).end(); it++)
#define READLINE(line) cin.getline((line), sizeof (line))
#define VALID(i, j, n, m) (0 <= (i) && (i) < (n) && 0 <= (j) && (j) < (m))
#define PI M_PI
#define EPSILON 1e-6
#define INF 1000000000
#define MOD 1000000007
#define endl '\n'
//NOTE: append ll to name if using long long
#define BITCOUNT __builtin_popcount
#define BITLEAD0 __builtin_clz
#define BITTRAIL0 __builtin_ctz
#define BITPARITY __builtin_parity

typedef unsigned int uint;
typedef long long int int64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

///////////////////////////////

typedef pair<int, pair<int, int> > interval;

struct customless
{
	bool operator()(const interval& lhs, const interval& rhs) const
	{
		return lhs.ST < rhs.ST || (lhs.ST == rhs.ST && lhs.ND.ST > rhs.ND.ST);
	}
};

#define N 1000010
int v[N];

void init()
{
	
}

void solve()
{
	int n, k, last;
	priority_queue<interval, vector<interval>, customless> pq;

	cin >> n >> k;

	v[0] = v[n + 1] = 1;
	REP (i, n)
		v[i + 1] = 0;
	pq.push(MP(n, MP(1, n)));

	for (int put = 0; put < k; ++put)
	{
		auto largest = pq.top();
		pq.pop();
		int a = largest.ND.ST, b = largest.ND.ND;
		int m = (a + b)/2;
		v[m] = 1;
		pq.push(MP((m - 1) - a + 1, MP(a, m - 1)));
		pq.push(MP(b - (m + 1) + 1, MP(m + 1, b)));
		last = m;
	}

	int l = 0, r = 0;
	for (int i = last - 1; i >= 0 && v[i] == 0; --i)
		++l;
	for (int i = last + 1; i <= n && v[i] == 0; ++i)
		++r;

	cout << max(l, r) << ' ' << min(l, r);
}

int main()
{ _
	init();
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cout << "Case #" << tc << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

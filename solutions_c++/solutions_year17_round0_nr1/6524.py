
// Author: Tiago Togores

#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
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

void init()
{
	
}

void solve()
{
	string s;
	int k, ans = 0;
	cin >> s >> k;
	int n = SZ(s);
	for (int i = 0; i < n - k; ++i)
	{
		if (s[i] == '-')
		{
			++ans;
			for (int j = i; j < i + k; ++j)
				s[j] = (s[j] == '+') ? '-' : '+';
		}
	}
	char c = s[n - k];
	for (int i = n - k + 1; i < n; ++i)
	{
		if (s[i] != c)
		{
			cout << "IMPOSSIBLE";
			return;
		}
	}
	if (c == '-')
		++ans;
	cout << ans;
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

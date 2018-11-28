
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef set<int> SI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;

const int INF = 1000000001;
const int EPS = 1e-9;
const int MOD = 1000000007;
const LL LLINF = 1000000000000000001;

//813437586

#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define FORD(i, b, e) for(int i = b; i >= e; i--)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define VAR(v, n) auto v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define GGL(x) "Case #" << x << ": "


/*************************** END OF TEMPLATE ***************************/




int main()
{
	ios_base::sync_with_stdio(false);

	int W;
	cin >> W;
	FOR(cc, 1, W)
	{
		LL D, n;
		cin >> D >> n;

		double t = -1;
		FOR(i, 1, n)
		{
			double k, s;
			cin >> k >> s;

			t = max((D-k)/s, t);
		}
		cout << GGL(cc) << fixed << setprecision(10) << (double)D/t << '\n';
	}

}
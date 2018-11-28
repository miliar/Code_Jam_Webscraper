
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef set<int> SI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;

const int INF = 1000000001;
const int EPS = 1e-9;
const int MOD = 1000000007;
const LL LLINF = 1000000000000000001;
const long double PI = 3.14159265358979323846;

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
		int n, k;
		cin >> n >> k;
		pair<LD, LD> pan[1042];

		FOR(i, 1, n)
		{
			LD r, h;
			cin >> r >> h;
			pan[i].ST = PI *r * r;
			pan[i].ND = 2 * PI * r * h;
		}

		sort(pan + 1, pan+n+1);
		reverse(pan+1, pan+n+1);
		/*
		FOR(i, 1, n)
		{
			cout << pan[i].ST + pan[i].ND << endl;
		}
		*/

		LD ans = 0;
		FOR(i, 1, n)
		{
			if(n-i+1 >= k)
			{
				LD loc = pan[i].ST + pan[i].ND;
				vector<LD> vec;
				vec.clear();
				FOR(j, i+1, n)
					vec.PB(pan[j].ND);
				sort(ALL(vec));
				reverse(ALL(vec));
				FOR(j, 0, k-2)
					loc += vec[j];
				ans = max(ans, loc);
			}
		}

		cout << GGL(cc) << fixed << setprecision(10) << ans << endl;
	}


}
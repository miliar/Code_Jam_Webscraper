
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


const int maxn = 200;

LL dst[maxn];
LL horsd[maxn];
long double horss[maxn];
long double tim[maxn];
LL gr[maxn][maxn];

int main()
{
	ios_base::sync_with_stdio(false);

	int W;
	cin >> W;
	FOR(cc, 1, W)
	{
		int n, q;
		cin >> n >> q;

		FOR(i, 1, n)
		{
			cin >> horsd[i] >> horss[i];
		}

		dst[1] = 0;
		FOR(i, 1, n-1)
		{
			int a;
			FOR(j, 1, i)
				cin >> a;
			cin >> a;
			dst[i+1] = dst[i] + a;
			FOR(j, i+2, n)
				cin >> a;
		}
		int a;
		FOR(i, 1, n)
			cin >> a;
		/*
		FOR(i, 1, n)
			cout << dst[i] << ' ';
		cout << endl;
		*/
		tim[1] = 0;

		LL st, en;
		cin >> st >> en;

		FOR(i, 2, n)
		{
			tim[i] = 1e100;
			//cout << tim[i] << " best inf" << endl;

			FOR(j, 1, i-1)
			{
				if((dst[i] - dst[j]) <= horsd[j])
				{
					//cout << "horse from " << j << " to " << i << " time " << tim[j] + (dst[i] - dst[j]) / horss[j] << endl;
					tim[i] = min(tim[i], tim[j] + (dst[i] - dst[j]) / horss[j]);
				}
			}
		}
		/*
		FOR(i, 1, n)
			cout << tim[i] << ' ';
		cout << endl;
		*/
		cout << GGL(cc) << fixed << setprecision(10) << tim[n] << endl;
	}
}
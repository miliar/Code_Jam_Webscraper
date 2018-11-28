
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
const double EPS = 1e-9;
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
		int n, k;
		cin >> n >> k;
		LD un;
		cin >> un;
		LD pro[100];
		FOR(i, 1, n)
			cin >> pro[i];

		sort(pro+1, pro+1+n);

		int i = 1;
		while(i < n && un > EPS && i*(pro[i+1] - pro[i]) - un <= EPS)
		{
			un -= i*(pro[i+1] - pro[i]);
			i++;
		}
		FOR(j, 1, i)
			pro[j] = pro[i] + un/i;

		LD ans = 1;
		FOR(i, 1, n)
			ans *= pro[i];

		cout << GGL(cc) << fixed << setprecision(10) << ans << endl;
	}

}
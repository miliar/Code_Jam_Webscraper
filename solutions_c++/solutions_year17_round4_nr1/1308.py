
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
const LD EPS = 1e-9;
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
	while(W--)
	{
		LL x, y, p, q;
		cin >> x >> y >> p >> q;

		if(p == q && p == 1)
		{
			if(x == y)
				cout << 0 << '\n';
			else
				cout << -1 << '\n';
		}
		else if(p == 0)
		{
			if(x > 0)
				cout << -1 << '\n';
			if(x == 0)
				cout << 0 << '\n';
		}
		else
		{
			LL b = 1;
			LL e = INF;
			while(b <= e)
			{
				int m = b + (e-b)/2;
				if(m*p >= x && m*q >= y+(m*p - x))
					e = m-1;
				else
					b = m+1;
			}
			//cout << b << endl;
			cout << b*q - y << '\n';
		}


	}
	
	
}
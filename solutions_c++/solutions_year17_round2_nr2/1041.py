
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
		int n;
		cin >> n;
		int r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		/*
		int oor = rand()%3;
		int ooy = rand()%4;
		int oob = rand()%5;
		r = oor;
		y = ooy;
		b = oob;
		n = r+y+b;
		*/
		char ans[10000];

		FOR(i, 1, b)
			ans[i] = 'B';
		FOR(i, b+1, r+b)
			ans[i] = 'R';
		FOR(i, r+b+1, n)
			ans[i] = 'Y';

		int it = 1;
		char kol[10000];
		FOR(i, 1, 3)
		{
			if(r >= y && r >= b)
			{
				FOR(j, 1, r)
					kol[it++] = 'R';
				r = 0;
			}
			else if(y >= r && y >= b)
			{
				FOR(j, 1, y)
					kol[it++] = 'Y';
				y = 0;
			}
			else if(b >= r && b >= y)
			{
				FOR(j, 1, b)
					kol[it++] = 'B';
				b = 0;
			}
		}

		cout << GGL(cc);
		/*
		bool possiblebrut = false;
		do
		{
			cout << "brut :";
			FOR(i, 1, n)
				cout << ans[i];
			cout << endl;
			bool pos = true;
			if(ans[1] == ans[n])
				pos = false;
			FOR(i, 1, n-1)
				if(ans[i] == ans[i+1])
					pos = false;
			if(pos)
				possiblebrut = true;
		}while(next_permutation(ans+1, ans+n+1));
		*/
		it = 1;
		FOR(i, 1, n)
		{
			if(i%2 == 1)
			{
				ans[i] = kol[it++];
			}
		}
		FOR(i, 1, n)
		{
			if(i%2 == 0)
			{
				ans[i] = kol[it++];
			}
		}

		bool possible = true;
		if(ans[1] == ans[n])
			possible = false;
		FOR(i, 1, n-1)
			if(ans[i] == ans[i+1])
				possible = false;
		//cout << W++ << endl;

		
		//cout << oob << ' ' << oor << ' ' <<  ooy << endl;
		if(!possible)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			FOR(i, 1, n)
				cout << ans[i];
			cout << endl;
		}
	}

}
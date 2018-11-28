#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); --i)
#define ITER(it,a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define FILL(a,value) memset(a, value, sizeof(a))

#define SZ(a) (int)a.size()
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000 + 7;
const LL LINF = 1LL * INF * INF;

const int MAX = 110;

int E[MAX];
int S[MAX];

int G[MAX][MAX];

double D[MAX][MAX];

void solve()
{
	int n, q;
	cin>>n>>q;
	FOR (i, 0, n)
	{
		cin>>E[i]>>S[i];
	}

	FOR (i, 0, n)
	{
		FOR (j, 0, n)
		{
			int x;
			cin>>x;
			if (x == -1) x = INF;
			G[i][j] = x;
			D[i][j] = 1e47;
		}
	}

	FOR (k, 0, n)
	{
		FOR (i, 0, n)
		{
			FOR (j, 0, n)
			{
				if (G[i][j] > G[i][k] + G[k][j]) G[i][j] = G[i][k] + G[k][j];
			}
		}
	}

	FOR (i, 0, n)
	{
		FOR (j, 0, n)
		{
			if (G[i][j] > E[i]) continue;
			D[i][j] = G[i][j] / (double)S[i];
		}
	}

	FOR (k, 0, n)
	{
		FOR (i, 0, n)
		{
			FOR (j, 0, n)
			{
				if (D[i][j] > D[i][k] + D[k][j]) D[i][j] = D[i][k] + D[k][j];
			}
		}
	}

	cout.precision(11);
	FOR (i, 0, q)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		x--;
		y--;
		cout<<fixed<<D[x][y]<<' ';
	}
	cout<<endl;



}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false); cin.tie(0);

	int tt;
	cin>>tt;
	FOR (ttt, 0, tt)
	{
		cout<<"Case #"<<ttt+1<<": ";
		cerr<<"Case #"<<ttt+1<<": ";
		solve();
		cerr<<"Done"<<endl;
	}
}

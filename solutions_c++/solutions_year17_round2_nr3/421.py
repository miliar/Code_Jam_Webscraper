#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); i--)
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
const LL LINF = INF * (LL) INF;

const int MAX = 111;

int n;
LL D[MAX][MAX];
double T[MAX][MAX];
LL DST[MAX];
LL V[MAX];

int main()
{
//	freopen("in.txt", "r", stdin);
	freopen("C-l.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin>>tests;
	FOR(test,1,tests+1)
	{
		int q;
		cin>>n>>q;
		FOR(i,0,n)
		{
			cin>>DST[i]>>V[i];
		}

		FOR(i,0,n)
		FOR(j,0,n)
		{
			cin>>D[i][j];
			if(D[i][j] == -1) D[i][j] = LINF;
		}

		FOR(k,0,n)
		FOR(i,0,n)
		FOR(j,0,n)
		{
			D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
		}

		FOR(i,0,n)
		FOR(j,0,n)
		{
			T[i][j] = 1e+47;
		}

		FOR(i,0,n)
		FOR(j,0,n)
		if(D[i][j] <= DST[i])
		{
			T[i][j] = min(T[i][j], D[i][j]*1.0/V[i]);
		}

		FOR(k,0,n)
		FOR(i,0,n)
		FOR(j,0,n)
		{
			T[i][j] = min(T[i][j],T[i][k] + T[k][j]);
		}


		printf("Case #%d:",test);

		FOR(i,0,q)
		{
			int a,b;
			cin>>a>>b;
			--a;--b;

			printf(" %.8lf",T[a][b]);
		}
		printf("\n");
		cerr<<test<<endl;
	}
}

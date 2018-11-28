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

const int MAX = 100100;
int n;
pair<int,double> K[MAX];
double T[MAX];
double d;
int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("A-l.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin>>tests;
	FOR(tt,1,tests+1)
	{
		cin>>d>>n;
		FOR(i,0,n)
		{
			cin>>K[i].first>>K[i].second;
		}

		sort(K,K+n);

		RFOR(i,n,0)
		{
			T[i] = (d-K[i].first)/K[i].second;
			if(i<n-1)T[i] = max(T[i],T[i+1]);
		}

		double v = d/T[0];

		printf("Case #%d: %.9lf\n",tt,v);
	}
}

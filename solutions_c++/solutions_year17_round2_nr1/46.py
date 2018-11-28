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

void solve()
{
	int d, n;
	cin>>d>>n;
	double mx = 0;
	FOR (i, 0, n)
	{
		int k, s;
		cin>>k>>s;

		int dist = d - k;
		double time = dist / (double)s;
		mx = max(mx, time);
	}

	double s = d / mx;

	cout.precision(11);
	cout<<fixed<<s<<endl;
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

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

typedef unsigned long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000 + 7;
const LL LINF = INF * (LL) INF;

map<LL, LL, greater<LL> > M;

void solve()
{
	LL n, k;
	cin>>n>>k;
	M.clear();
	M[n] = 1;

	while(k)
	{
		pair<LL, LL> b = *M.begin();
		M.erase(M.begin());

		if (b.second >= k)
		{
			M[b.first] = b.second;
			k = 0;
			break;
		}

		k -= b.second;

		LL L = (b.first - 1) / 2;
		LL R = b.first - 1 - L;

		M[L] += b.second;
		M[R] += b.second;
	}

	LL len = M.begin() -> first;

	LL mn = (len - 1) / 2;
	LL mx = len - 1 - mn;
	cout<<mx<<' '<<mn<<endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	//ios::sync_with_stdio(false); cin.tie(0);

	freopen("out.txt", "w", stdout);

	int tt;
	cin>>tt;
	FOR (ttt, 0, tt)
	{
		cout<<"Case #"<<ttt+1<<": ";
		cerr<<"Case #"<<ttt+1<<"/"<<tt<<":"<<endl<<"..."<<endl;
		solve();
		cerr<<"Done"<<endl;
	}


}

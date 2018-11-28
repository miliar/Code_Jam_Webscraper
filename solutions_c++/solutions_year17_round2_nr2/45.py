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

int A[6];
int V[6];
string S = "ROYGBV";

void solve()
{
	int n;
	cin>>n;
	FOR (i, 0, 6)
	{
		cin>>A[i];
	}

	FOR (i, 0, 6)
	{
		V[i] = A[i] - A[(i+3) % 6];
	}

	string res = "";

	int st = -1;
	FOR (i, 0, 6)
	{
		if (i & 1) continue;
		if (A[i] == 0) continue;
		st = i;
		break;
	}

	int fst = st;
	int lst = -1;

	while(true)
	{
		if (!A[st])
		{
			break;
		}
		lst = st;
		A[st]--;
		V[st]--;
		res += S[st];

		if (st & 1)
		{
			st = (st + 3) % 6;
			continue;
		}

		if (A[(st+3) % 6])
		{
			V[st]++;
			st = (st + 3) % 6;
			continue;
		}

		int v1 = V[(st + 2) % 6];
		int v2 = V[(st + 4) % 6];

		if (v1 == v2)
		{
			if ((st + 2) % 6 == fst) st = (st + 2) % 6;
			else st = (st + 4) % 6;
		}
		else
		{
			if (v1 > v2) st = (st + 2) % 6;
			else st = (st + 4) % 6;
		}
	}

	cerr<<res<<endl;

	if (lst == fst) cout<<"IMPOSSIBLE"<<endl;
	else
	{
		if (SZ(res) != n) cout<<"IMPOSSIBLE"<<endl;
		else cout<<res<<endl;
	}
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

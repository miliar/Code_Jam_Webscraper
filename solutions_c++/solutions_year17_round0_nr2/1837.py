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

bool ok(string s)
{
	FOR (i, 0, SZ(s))
	{
		if (s[i] < '0' || s[i] > '9') return false;
	}

	if (s[0] == '0') return false;

	FOR (i, 1, SZ(s))
	{
		if (s[i] < s[i-1]) return false;
	}
	return true;
}

void solve()
{
	string s;
	cin>>s;
	if (ok(s))
	{
		cout<<s<<endl;
		return;
	}

	RFOR(i, SZ(s), 0)
	{
		s[i]--;
		if (ok(s))
		{
			cout<<s<<endl;
			return;
		}

		s[i] = '9';
	}

	s = string(SZ(s)-1, '9');
	cout<<s<<endl;
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

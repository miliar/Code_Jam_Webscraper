#include <bits/stdc++.h>
using namespace std;
//look at my code my code is amazing
#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define FOREACH(it, a) for (typeof(a.begin()) it = (a).begin(); it != (a).end(); it++)
#define ROF(i, a, b) for (int i = int(a); i >= int(b); i--)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define ALL(x) x.begin(), x.end()
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second
#define EPS 1e-9
#define DEBUG(x)   cerr << #x << ": " << x << " "
#define DEBUGLN(x) cerr << #x << ": " << x << " \n"
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<bool> vb;
//ios_base::sync_with_stdio(0);//fast entrada/salida ;-)
//cin.tie(NULL); cout.tie(NULL);


bool isTiddy(ll n)
{
	if(n == 0LL)
		return true;

	while(true)
	{
		ll u = n%10LL;
		n /= 10LL;
		ll d = n%10LL;

		if(n == 0LL)
			return true;

		if(d > u)
			return false;
	}

	return true;
}

ll dec_pot[20], nines[20];

void solve()
{
	ll n;

	cin >> n;

	ll i = 0LL;
	while( not isTiddy(n) )
	{
		n /= dec_pot[i];
		n--;
		n = (n*dec_pot[i]) + nines[i];
		++i;
	}

	static int caso = 0;
	cout << "Case #" << ++caso << ": " << n << "\n";
}

int main()
{
	int T;

	cin >> T;

	dec_pot[0] = 10LL;
	nines[0] = 9;
	REP(i, 18)
	{
		dec_pot[i+1] = dec_pot[i] * 10LL;
		nines[i+1]   = (nines[i]*10LL) + 9LL;
		DEBUG(i);
		DEBUG(dec_pot[i]);
		DEBUGLN(nines[i]);
	}

	REP(i, T)
		solve();

	return 0;
}
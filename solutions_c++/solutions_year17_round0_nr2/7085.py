#include <bits/stdc++.h>
using namespace std;
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define ABS(x) ((x) < 0 ? -1*(x) : (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define INF 2000000000
#define BINF 20000000000000000LL
#define trace(x)                 cerr << #x << ": " << x << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;
const ld PI = acos(-1.0);

ll lastTidy(ll n)
{
	ll numDigs, i = 0, tmp = n;
	while(tmp)
	{
		tmp /= 10;
		++i;
	}
	numDigs = i;
	ll digs[numDigs];
	for(i = numDigs-1; i >= 0; --i)
	{
		digs[i] = n % 10;
		n /= 10;
	}

	/*for(i = 0; i < numDigs; ++i)
		cout << digs[i];
	cout << endl;*/

	bool flag;
	while(1)
	{
		flag = true;
		for(i = 1; i < numDigs; ++i)
		{
			if(digs[i-1] > digs[i])
			{
				flag = false;
				--digs[i-1];
				break;
			}
		}
		if(flag)
			break;
		else
		{
			for(; i < numDigs; ++i)
				digs[i] = 9;
		}
	}
	ll ans = 0;
	for(i = 0; i < numDigs; ++i)
	{
		ans = 10*ans + digs[i];
	}
	return ans;
}

int main()
{
	//fastScan;
	ll T,N,i,l;
	cin >> T;
	for(l = 1; l <= T; ++l)
	{
		cin >> N;
		cout << "Case #" << l << ": " << lastTidy(N) << endl;
	}
	return 0;
}
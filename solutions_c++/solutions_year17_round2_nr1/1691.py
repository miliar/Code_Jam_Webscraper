#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
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
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;
const ld PI = acos(-1.0);

int main()
{
	fastScan;
	int T,N,i,l,D,K,S;
	cin >> T;
	for(l = 1; l <= T; ++l)
	{
		cin >> D >> N;
		double maxT = -1;
		for(i = 0; i < N; ++i)
		{
			cin >> K >> S;
			maxT = MAX(maxT,((D-K)*1.0)/S);
		}
		cout << "Case #" << l << ": " << setprecision(15) << D/maxT << endl;
	}
	
	return 0;
}
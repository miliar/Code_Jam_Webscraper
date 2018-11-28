#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define eps 1e-13
#define PI 3.141592653589793238L
#define INF 1000000011
#define INFLL 1000000000000000011LL
#define space printf(" ")
#define endl printf("\n")
#define vi vector<int>
#define vll vector<long long>
#define vc vector<char>
#define vs vector<string>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pil pair<int, long long>
#define pli pair<long long, int>
#define pcc pair<char, char>
#define mp make_pair
#define F first
#define S second
#define pb(x) push_back(x)
#define fo(i,a,n) for(i = (a); i < (n); i++)
#define sd(x) scanf("%d", &(x))
#define pd(x) printf("%d", (x))
#define pdn(x) printf("%d\n", (x))
#define slld(x) scanf("%lld", &(x))
#define plld(x) printf("%lld", (x))
#define plldn(x) printf("%lld\n", (x))
#define sllf(x) scanf("%llf", &(x))
#define pllf(x) printf("%.9llf", (x))
#define pllfn(x) printf("%.9llf\n", (x))
#define sch(x) scanf("%c", &(x))
#define pch(x) printf("%c", (x))
#define pchn(x) printf("%c\n", (x))
#define gtl(x) getline(cin, (x))
#define flsh fflush(stdout)
#define sws ios_base::sync_with_stdio(false); cin.tie(0)
#define gcd __gcd
#define clr(x) memset(x,0,sizeof(x))
#define all(a) (a).begin(), (a).end()
#define foreach(i,a) for(__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define sz(a) (int)((a).size())
#define io_file freopen("A-small-attempt0.in", "r", stdin);freopen("A-small-attempt0.out", "w", stdout)

/*ll gcd(ll a, ll b)
{
	if(b == 0)
		return a;
	return gcd(b, a%b);
}*/

ll modx(ll Base, ll exponent)
{
	ll ans = 1;
	if(Base == 1)
		return Base;
	while(exponent)
	{
		if(exponent & 1)
			ans = (ans * Base)%mod;
		Base = (Base * Base)%mod;
		exponent = exponent >> 1;
	}
	return ans;
}

ll inmodx(ll num)
{
	return (modx(num, mod-2LL));
}

struct node
{
	node()
	{

	}
};

bool cmp(pll a, pll b)
{
	bool ans = 0;
	if(a.S*a.F >= b.S*b.F)
		ans = 1;
	return ans;
}

const int N = (1e5)+9;
const int M = (1e3)+9;

pll p[M];
vector < pll > x;

int main()
{
	sws;
	// clock_t clk;
	// clk = clock();
	io_file;
	// srand (time(NULL));

	//Code here
	int t, cs, i, n, k, j;
	double o;
	ll ans, temp;
	cin >> t;
	fo(cs,1,t+1)
	{
		cout << "Case #" << cs << ": ";
		cin >> n >> k;
		fo(i,1,n+1)
			cin >> p[i].F >> p[i].S;
		sort(p+1,p+n+1,greater< pll >());
		ans = 0LL;
		fo(i,1,n+1)
		{
			temp = p[i].F*p[i].F + 2LL*p[i].F*p[i].S;
			x.clear();
			fo(j,i+1,n+1)
				x.pb(p[j]);
			sort(all(x),cmp);
			fo(j,0,min(sz(x),k-1))
				temp += (2LL*x[j].F*x[j].S);
			ans = max(ans, temp);
		}
		// cout << ans << '\n';
		o = PI*((double)ans);
		cout << fixed << setprecision(9) << o << '\n';
	}
	// Code ends here

	// clk = clock() - clk;
	// cout << fixed << setprecision(6) << "Time: " << ((double)clk)/CLOCKS_PER_SEC << "\n";
	return 0;
}
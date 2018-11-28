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
#define io_file freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout)

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

bool cmp()
{
	bool ans = 0;
	return ans;
}

const int N = (1e2)+9;
const int M = (2e3)+9;

string s[N], ans[N];
vector < char > v[N];
queue < int > q;
bool vis[N];

int main()
{
	sws;
	// clock_t clk;
	// clk = clock();
	io_file;
	// srand (time(NULL));

	//Code here
	int t, cs, n, m, i, j, k, z;
	cin >> t;
	fo(cs,1,t+1)
	{
		cout << "Case #" << cs << ":\n";
		cin >> n >> m;
		fo(i,0,n)
		{
			cin >> s[i];
			ans[i] = s[i];
			fo(j,0,m)
			{
				if(s[i][j] != '?')
					v[i].pb(s[i][j]);
			}
		}
		fo(i,0,n)
		{
			j = k = 0;
			while(j < m && k < sz(v[i]))
			{
				if(s[i][j] != v[i][k] && s[i][j] != '?')
				{
					ans[i][j] = s[i][j];
					k++;
					j++;
				}
				else
				{
					ans[i][j] = v[i][k];
					j++;
				}
			}
		}
		while(!q.empty())
			q.pop();
		fo(i,0,n)
		{
			if(!v[i].empty())
			{
				vis[i] = 1;
				q.push(i);
			}
		}
		while(!q.empty())
		{
			z = q.front();
			q.pop();
			if(z > 0)
			{
				if(!vis[z-1])
				{
					vis[z-1] = 1;
					ans[z-1] = ans[z];
					q.push(z-1);
				}
			}
			if(z < n-1)
			{
				if(!vis[z+1])
				{
					vis[z+1] = 1;
					ans[z+1] = ans[z];
					q.push(z+1);
				}
			}
		}
		fo(i,0,n)
			cout << ans[i] << '\n';
		fo(i,0,n+1)
		{
			v[i].clear();
			vis[i] = 0;
			ans[i] = s[i] = "";
		}
	}
	// Code ends here

	// clk = clock() - clk;
	// cout << fixed << setprecision(6) << "Time: " << ((double)clk)/CLOCKS_PER_SEC << "\n";
	return 0;
}
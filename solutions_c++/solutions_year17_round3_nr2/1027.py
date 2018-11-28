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
#define io_file freopen("B-large.in", "r", stdin);freopen("B-large.out", "w", stdout)

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

bool cmp()//true for a before b
{
	bool ans = 0;
	return ans;
}

const int N = (1e5)+9;
const int M = (1440)+9;

pii a[109], b[109];
int tm_[M];
int dp[725][725][2][2];

void func(int a1, int a2, int a3, int a4, int b1, int b2, int b3, int b4, int val)
{
	dp[a1][a2][a3][a4] = min(dp[a1][a2][a3][a4],dp[b1][b2][b3][b4]+val);
	return;
}

int main()
{
	sws;
	// clock_t clk;
	// clk = clock();
	io_file;
	// srand (time(NULL));

	//Code here
	int t, i, j, cs, n, m, s, e, k, l, ans;
	cin >> t;
	fo(cs,1,t+1)
	{
		cout << "Case #" << cs << ": ";
		cin >> n >> m;
		fo(i,0,1441)
			tm_[i] = 0;
		fo(i,1,n+1)
		{
			cin >> s >> e;
			fo(j,s+1,e+1)
				tm_[j] = 1;
		}
		fo(i,1,m+1)
		{
			cin >> s >> e;
			fo(j,s+1,e+1)
				tm_[j] = 2;
		}
		fo(i,0,721)
		{
			fo(j,0,721)
				dp[i][j][0][0] = dp[i][j][0][1] = dp[i][j][1][0] = dp[i][j][1][1] = INF;
		}
		if(tm_[1] == 0)
		{
			dp[1][0][0][0] = 0;
			dp[0][1][1][1] = 0;
		}
		else if(tm_[1] == 1)
			dp[1][0][0][0] = 0;
		else
			dp[0][1][1][1] = 0;
		fo(i,0,721)
		{
			fo(j,0,721)
			{
				fo(k,0,2)
				{
					if(i == 0 && j == 0)
						continue;
					fo(l,0,2)
					{
						if(dp[i][j][k][l] < INF)
						{
							if(tm_[i+j+1] == 0)
							{
								//e = 0
								if(k == 0 && l == 0) func(i+1,j,k,0,i,j,k,l,0);
								else if(k == 0 && l == 1) func(i+1,j,k,0,i,j,k,l,0);
								else if(k == 1 && l == 0) func(i+1,j,k,0,i,j,k,l,0);
								else func(i+1,j,k,0,i,j,k,l,2);
								//e = 1
								if(k == 0 && l == 0) func(i,j+1,k,1,i,j,k,l,2);
								else if(k == 0 && l == 1) func(i,j+1,k,1,i,j,k,l,0);
								else if(k == 1 && l == 0) func(i,j+1,k,1,i,j,k,l,0);
								else func(i,j+1,k,1,i,j,k,l,0);
							}
							else if(tm_[i+j+1] == 1)
							{//e = 0
								if(k == 0 && l == 0) func(i+1,j,k,0,i,j,k,l,0);
								else if(k == 0 && l == 1) func(i+1,j,k,0,i,j,k,l,0);
								else if(k == 1 && l == 0) func(i+1,j,k,0,i,j,k,l,0);
								else func(i+1,j,k,0,i,j,k,l,2);
							}
							else
							{//e = 1
								if(k == 0 && l == 0) func(i,j+1,k,1,i,j,k,l,2);
								else if(k == 0 && l == 1) func(i,j+1,k,1,i,j,k,l,0);
								else if(k == 1 && l == 0) func(i,j+1,k,1,i,j,k,l,0);
								else func(i,j+1,k,1,i,j,k,l,0);
							}
						}
						// cout << i << " " << j << " " << k << " " << l <<  " : " << dp[i][j][k][l] << '\n';
					}
				}
			}
		}
		ans = min(min(dp[720][720][0][0],dp[720][720][0][1]),min(dp[720][720][1][0],dp[720][720][1][1]));
		cout << ans << '\n';
	}
	// Code ends here

	// clk = clock() - clk;
	// cout << fixed << setprecision(6) << "Time: " << ((double)clk)/CLOCKS_PER_SEC << "\n";
	return 0;
}
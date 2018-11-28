//~ mail ID : neernpatel@gmail.com 
//~ Author : DrexDelta 
//~ codechef : drexdelta , hackerRank : drexdelta , codeforces : drexdelta1 
//~ Contact Info : neernpatel@gmail.com , +91-80898 25745

#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define MP make_pair
#define PB push_back
#define UB upper_bound
#define LB lower_bound
#define ER erase
#define EN end()
#define B begin()
#define I insert
#define OPTIMIZE ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define int ll
#define endl "\n"
#define CO cout << 
#define CI cin >> 
#define NL cout << endl;
#define DBG cin >> debug;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;

const ll maxn=2e2 +5;
const ll MOD = 1e9+7;

bool comparator(int i , int j)
{
    return (i < j);
}

ll power(ll x, ll i)
{
	ll ans = 1;
	while(i > 0)
	{
		if(i&1)
			ans = (ans*x)%MOD;
		i >>=1;
		x = (x*x)%MOD;
	}
	return ans;
}

ll power(ll x, ll i,ll mod)
{
	ll ans = 1;
	while(i > 0)
	{
		if(i&1)
			ans = (ans*x)%mod;
		i >>=1;
		x = (x*x)%mod;
	}
	return ans;
}

ll modInverse(ll x, ll mod)
{
	return power(x , mod-2,mod);
}

bool isPalindrome(string s)
{
	int limit = s.length()/2;
	for(int i =  0 ; i < limit ; i++)
	{
		if(s[i] != s[s.length()-i-1])
			return 0;
	}
	return true;
}

ll gcd(ll x, ll y)
{
	ll t;
	while(y != 0)
	{
		t = x%y;
		x = y;
		y = t;
	}
	return x;
}
bool isPrime(int n)
{
	int root = sqrt(n);
	for(int i = 2 ; i <= root ; i++) if(n%i == 0) return 0;
	return 1;
}	
///////////////////////////////////
// declaration section ////////////
///////////////////////////////////
double capacity[maxn],speed[maxn];
double dis[maxn][maxn],n,q,u,v;
double ans;
void getInput()
{
	cin >> n >> q;
	for(int i = 1 ; i <= n; i++)
		cin >> capacity[i] >> speed[i];
	
	for(int i = 1; i <= n ;i++)
		for(int j = 1 ; j <= n ; j++)
			cin >> dis[i][j];
	cin >> u >> v;	
}

set<pair<pair<double,double>,double>> dp[maxn];
void solve()
{
	for(int i = 1 ; i <= n ;i++)
		dp[i].clear();
	dp[2].I({ {(dis[1][2])/speed[1],capacity[1]-dis[1][2]}, speed[1]});// { time , rem} , speed
	double curTime,rem,curSpeed,minTime;
	
	for(int i = 2; i < n ; i++)
	{
		minTime = 1000000000000;
		for(auto j : dp[i])
		{
			curTime = j.F.F;
			rem = j.F.S;
			curSpeed = j.S;
			if(curTime < minTime) minTime = curTime;
			if(rem >= dis[i][i+1])
			{
				dp[i+1].I( {  {curTime + (dis[i][i+1])/curSpeed , rem - dis[i][i+1] } , curSpeed } );
				
			}
		}
		dp[i+1].I({ { minTime + dis[i][i+1]/speed[i] , capacity[i]-dis[i][i+1] } , speed[i] });
	}
	ans = 1000000000000;
	for(auto i : dp[(int)n])
		if(i.F.F < ans)
			ans = i.F.F;
	return;
}

signed main()
{
	OPTIMIZE
	int t;
	cin >> t;
	for(int i =1 ; i <= t ; i++)
	{
		cout << "Case #" << i << ": " ;
		getInput();
		solve();
		cout <<fixed << setprecision(8) << ans << endl;
	}
	return 0;
}

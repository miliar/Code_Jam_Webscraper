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
#define PI 3.1415926535897932384
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;

const ll maxn=1e3 +5;
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
ld dp[maxn][maxn],ans;
vector<pair<ld , ld >> cakes;
ld n , K;
bool cmp(pair<ld , ld > i , pair<ld , ld > j)
{
	if(i.F != j.F)
		return (i.F < j.F);
	else
		return i.S < j.S;
}
void getInput()
{
	CI n >> K;
	for(int i = 1 ; i <= n ; i++)
	{
		ld x , y;
		CI x >> y;
		cakes.PB({x , y});
	}
	sort( cakes.begin(), cakes.end() , cmp);
}
ld topArea(ld r , ld h)
{
	return ( PI * 2.0 * r * h + PI*(r*r));
}
ld middleArea(ld r , ld h , ld pre)
{
	return ( PI * 2.0 * r * h + PI * (r*r - pre*pre));
}
void solve()
{
	cakes.clear();
	getInput();
	for(int i = 0 ; i < maxn ; i++)
		for(int j = 0 ; j < maxn ; j++)
			dp[i][j] = -5555555;
			
	for(int i = 0 ; i < n ; i++)
	{
		dp[i][1] = topArea(cakes[i].F  , cakes[i].S);
		for(int j = 2 ; j <= K && j <= i+1; j++)
		{
			dp[i][j] = 0;
			for(int k = i-1 ; k >= 0 && k >= (j-2) ; k--)
			{
				dp[i][j] = max(dp[k][j-1] + middleArea(cakes[i].F , cakes[i].S , cakes[k].F ) , dp[i][j]);
			}
		}
	}
	
	ld ans = 0;
	for(int i = 0 ; i < n ; i++)
		ans = max(ans , dp[i][(int)K]);
	
	CO setprecision(12) << fixed << ans , NL
}
signed main()
{
	OPTIMIZE
	int testCases;
	CI testCases;
	for(int curTest = 1 ; curTest <= testCases ; curTest++)
		CO "Case #" << curTest << ": " , solve();
	
	return 0;
}
